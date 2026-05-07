# Arm dimensions and motion settings

ARM = {
    "L1": 150,                 # Link 1 length (mm)
    "L2": 150,                 # Link 2 length (mm)

    "STEPS_PER_REV": 200,
    "MICROSTEP": 16,

    "STEP_DELAY": 0.001,

    "PICK_Z_MM": 40
}

# GPIO pin mapping

PINS = {
    "J1_STEP": 2,
    "J1_DIR": 5,

    "J2_STEP": 3,
    "J2_DIR": 6,

    "Z_STEP": 4,
    "Z_DIR": 7,

    "GRIPPER": 11
}

# Camera

CAMERA_INDEX = 0

# Place position

PLACE_XY_MM = (180, 100)
