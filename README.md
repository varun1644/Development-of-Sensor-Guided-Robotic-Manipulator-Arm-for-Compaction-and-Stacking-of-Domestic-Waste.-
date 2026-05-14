# Development of Sensor Guided Robotic Manipulator Arm for Compaction and Stacking of Domestic Waste

A smart waste-handling robotic system designed to detect, pick, compact, and stack domestic waste using computer vision, robotic arm control, and sensor-guided automation.


## Complete System Setup 
<img width="626" height="470" alt="image" src="https://github.com/user-attachments/assets/e584f7d9-b98e-4217-a248-c6526c0cdb57" />


## Overview

This project focuses on automating domestic waste handling using a sensor-guided robotic manipulator. The system combines YOLOv5-based object detection, inverse kinematics, actuator control, and compacting mechanisms to improve waste management efficiency.

The robotic arm detects waste through a camera feed, calculates the target position, picks the object using a gripper, and transfers it for compaction and stacking.

## Features

- YOLOv5-based waste detection
- Robotic arm inverse kinematics
- Stepper motor motion control
- Servo-based gripper system
- Sensor-guided object handling
- Waste compaction mechanism
- Automated stacking workflow
- Jetson Nano / Arduino compatible
- Modular hardware and software design

## Compaction System 
<img width="741" height="593" alt="image" src="https://github.com/user-attachments/assets/4b23fe1d-f6a9-4f66-bec0-f7d812a28fd2" />

## Robotic Arm 
<img width="644" height="490" alt="image" src="https://github.com/user-attachments/assets/1687b14a-53cc-4b46-a5c9-a370b5bc6309" />

## Camera and Detection 
<img width="741" height="463" alt="image" src="https://github.com/user-attachments/assets/4c4acd3e-c873-494f-84fd-e045166ac0c5" />
## Gripper open and close 
<img width="662" height="430" alt="image" src="https://github.com/user-attachments/assets/8eaf0447-f6b1-4c66-9438-ee254b1ce56a" />


---




## System Block Diagram 

<img width="900" height="600" alt="image" src="https://github.com/user-attachments/assets/11aea2ce-5f4d-4081-99ce-2b3026e5e0a0" />







---
## Methodology
<img width="1229" height="745" alt="image" src="https://github.com/user-attachments/assets/5d7c150b-103f-44f5-b4ad-ee14a2fe9b7a" />





---
## CAD of the arm 
  <img width="455" height="757" alt="image" src="https://github.com/user-attachments/assets/5ffe821a-ed77-44ca-b904-97f0049f8c6d" />

## Hardware Used

- Jetson Nano / Arduino
- USB Webcam
- CNC Shield
- Stepper Motors
- Servo Motor
- Motor Drivers
- Linear Actuator
- Power Supply
- Sensors (IR / Ultrasonic / Limit Switches)

---

## Control System 

<img width="850" height="535" alt="image" src="https://github.com/user-attachments/assets/7bfb3ced-50c0-4881-a5fe-3d887e96e8bc" />


## Software Stack

- Python
- OpenCV
- YOLOv5
- Jetson GPIO
- Arduino IDE

---

## Project Structure

```bash
├── detect.py              # YOLOv5 object detection
├── ik.py                  # Inverse kinematics and arm control
├── config.py              # Configuration parameters
├── main.py                # Main automation pipeline
├── models/                # YOLOv5 models
├── datasets/              # Training/testing datasets
├── runs/                  # Detection outputs
├── hardware/              # CAD and hardware files
└── README.md
```

---

## System Workflow

1. Camera captures live feed  
2. YOLOv5 detects waste objects  
3. Coordinates are calculated  
4. Inverse kinematics determines arm movement  
5. Arm picks the waste object  
6. Waste is transferred for compaction  
7. Compacted waste is stacked/stored  

---


## Applications

- Smart waste management
- Automated recycling systems
- Domestic waste handling
- Industrial sorting assistance
- Robotics research and education

---

## Future Improvements

- AI-based waste classification
- Multi-bin segregation
- Real-time path planning
- IoT monitoring integration
- Autonomous mobile platform support

---

## Authors

Developed as a major project on intelligent robotic waste handling systems.
