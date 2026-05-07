import math
import time
import Jetson.GPIO as GPIO
from config import ARM, PINS

STEPS_PER_DEG = (ARM["STEPS_PER_REV"] * ARM["MICROSTEP"]) / 360.0

SERVO_PIN = PINS["GRIPPER"]
SERVO_OPEN_ANGLE = 10
SERVO_CLOSE_ANGLE = 90

_current_angles = [0.0, 0.0]

def setup():
    GPIO.setmode(GPIO.BOARD)

    for pin in PINS.values():
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    global pwm
    GPIO.setup(SERVO_PIN, GPIO.OUT)

    pwm = GPIO.PWM(SERVO_PIN, 50)
    pwm.start(0)

def cleanup():
    pwm.stop()
    GPIO.cleanup()

# ---------- IK ----------

def is_reachable(x, y):
    L1, L2 = ARM["L1"], ARM["L2"]
    return (x**2 + y**2) <= (L1 + L2)**2

def inverse_kinematics(x, y):
    L1, L2 = ARM["L1"], ARM["L2"]

    d = math.sqrt(x**2 + y**2)

    if d > L1 + L2:
        raise ValueError("Out of reach")

    cos2 = (d**2 - L1**2 - L2**2) / (2 * L1 * L2)
    cos2 = max(-1, min(1, cos2))

    theta2 = math.degrees(math.acos(cos2))

    alpha = math.atan2(y, x)
    beta = math.acos((d**2 + L1**2 - L2**2) / (2 * d * L1))

    theta1 = math.degrees(alpha - beta)

    return theta1, theta2

# ---------- STEPPERS ----------

def _pulse(step_pin, steps, delay):
    for _ in range(abs(steps)):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(delay)

        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(delay)

def move_joint(step_pin, dir_pin, delta_deg):
    steps = int(abs(delta_deg) * STEPS_PER_DEG)

    GPIO.output(dir_pin, GPIO.HIGH if delta_deg >= 0 else GPIO.LOW)

    _pulse(step_pin, steps, ARM["STEP_DELAY"])

def move_z(delta_mm):
    mm_per_rev = 8

    steps_per_mm = (
        ARM["STEPS_PER_REV"] * ARM["MICROSTEP"]
    ) / mm_per_rev

    steps = int(abs(delta_mm) * steps_per_mm)

    GPIO.output(
        PINS["Z_DIR"],
        GPIO.HIGH if delta_mm >= 0 else GPIO.LOW
    )

    _pulse(PINS["Z_STEP"], steps, ARM["STEP_DELAY"])

# ---------- SERVO ----------

def set_servo(angle):
    duty = 2 + angle / 18

    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)

    time.sleep(0.4)

    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

def gripper(open_close):
    if open_close:
        set_servo(SERVO_OPEN_ANGLE)
    else:
        set_servo(SERVO_CLOSE_ANGLE)

# ---------- MOTION ----------

def goto_xy(x, y):
    if not is_reachable(x, y):
        print("Out of reach")
        return

    t1, t2 = inverse_kinematics(x, y)

    move_joint(
        PINS["J1_STEP"],
        PINS["J1_DIR"],
        t1 - _current_angles[0]
    )

    move_joint(
        PINS["J2_STEP"],
        PINS["J2_DIR"],
        t2 - _current_angles[1]
    )

    _current_angles[0] = t1
    _current_angles[1] = t2

# ---------- HIGH LEVEL ----------

def pick_at(x, y):
    print(f"Picking at ({x:.1f}, {y:.1f})")

    gripper(True)
    time.sleep(0.3)

    goto_xy(x, y)
    time.sleep(0.3)

    move_z(ARM["PICK_Z_MM"])
    time.sleep(0.3)

    gripper(False)
    time.sleep(0.5)

    move_z(-ARM["PICK_Z_MM"])
    time.sleep(0.3)

def place_at(x, y):
    print(f"Placing at ({x:.1f}, {y:.1f})")

    goto_xy(x, y)
    time.sleep(0.3)

    move_z(ARM["PICK_Z_MM"])
    time.sleep(0.3)

    gripper(True)
    time.sleep(0.4)

    move_z(-ARM["PICK_Z_MM"])
    time.sleep(0.3)
