# Development of Sensor Guided Robotic Manipulator Arm for Compaction and Stacking of Domestic Waste

A smart waste-handling robotic system designed to detect, pick, compact, and stack domestic waste using computer vision, robotic arm control, and sensor-guided automation.

---

## Overview

This project focuses on automating domestic waste handling using a sensor-guided robotic manipulator. The system combines YOLOv5-based object detection, inverse kinematics, actuator control, and compacting mechanisms to improve waste management efficiency.

The robotic arm detects waste through a camera feed, calculates the target position, picks the object using a gripper, and transfers it for compaction and stacking.
## Project images




---
## Methodology
<img width="1229" height="745" alt="image" src="https://github.com/user-attachments/assets/5d7c150b-103f-44f5-b4ad-ee14a2fe9b7a" />

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
