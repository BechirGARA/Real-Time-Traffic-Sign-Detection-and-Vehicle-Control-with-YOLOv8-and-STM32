# Real-Time-Traffic-Sign-Detection-and-Vehicle-Control-with-YOLOv8-and-STM32
This project integrates advanced AI and embedded systems to achieve real-time traffic sign detection and vehicle control. It employs a YOLOv8 model for detecting traffic signs (e.g., stop panels, red signals, and green signals) and utilizes an STM32 microcontroller for vehicle control through serial communication.

├── .idea/               # IDE configuration files

├── AI project/          # Folder containing STM32 code

│   ├── USB port configuration for serial communication

│   ├── PWM signal configuration via Timer 1 and Timer 8 (4 channels in total)

├── main.py              # Main Python script for detection and sending commands

├── model.pt             # Trained YOLOv8 model for sign detection

├── README.md            # Project documentation

Component Details
1. AI project/ folder

    Contains the code for the STM32F407 microcontroller.
    Configures:
        The USB port for serial communication.
        PWM signals via timers 1 and 8 to control the motors.

2. main.py

    Python script used to run the YOLOv8 model.
    Features:
        Real-time video capture via a PC camera.
        Detection of traffic signs.
        Sending corresponding commands ("FORWARD", "STOP") via a serial port.

3. model.pt

    Trained model for detecting traffic signs (based on YOLOv8).

Project Workflow

    The camera captures real-time images.
    The model (model.pt) detects traffic signs (e.g., "STOP").
    A corresponding command is sent to the STM32 via a serial port.
    The STM32 receives the command and generates PWM signals to control the motors.

Dependencies

    Python 3.8+
    Pyserial library
    OpenCV
    YOLOv8 library (ultralytics)
    STM32CubeIDE (for STM32 configuration)
