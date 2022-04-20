# SPOT-navigation

The project is divided into both social and navigation focused teams, both producing a database of
SPOT’s data. This project aims to establish systems for data collection that can be used in future
research projects in the INSITE lab related to SPOT.

## Setup Dependencies
See requirements.txt for the dependencies required for this example. Using pip, these dependencies can be installed using:
```
python3 -m pip install -r requirements.txt
```

## Overview
To run the Command Line Interface, use the following command:

```
python3.7 mission_recorder.py ROBOT_IP DIRECTORY_TO_SAVE_MISSION
```

The program allows you to control Spot using the keyboard, record a mission, and collect data. All
files collected will be stored in the 'DIRECTORY_TO_SAVE_MISSION' directory specified above. This
must be a new folder.

## How to Record a Mission
NOTE: All keyboard commands are case-sensitive.
1. Place at least one fiducial marker in a position that is visible to Spot’s cameras.  More than one fiducial can be used (but each must be unique).
2. OPTIONAL: The robot's camera view can be monitored using the OBSERVE mode on the tablet.
3. Make sure that Spot’s hardware power switch is on and Spot’s hardware E-Stop is disabled.
4. Run the mission_recorder script:

```
python3.7 mission_recorder.py ROBOT_IP DIRECTORY_TO_SAVE_MISSION
```

5. Press the spacebar to release the software E-Stop.
6. Press ‘P’ to power on the robot.
7. Press ‘f’ to command the robot to stand up.
8. Move the robot using the [wasd keys](../wasd/README.md) to the desired starting point of the mission, which must have line-of-sight to the fiducial.
9. The text interface should indicate that the number of fiducials visible is at least 1.
10. If this number is 0, move the robot using the wasd keys until it can see the fiducial.
11. Press ‘m’ to start recording a mission.
12. Drive the robot along the desired path, using ‘w’ and ‘s’ to drive forward and back, ‘a’ and ‘d’ to strafe left and right, and ‘q’ and ‘e’ to turn left and right.
13. When you have finished training the path, press ‘g’ to save the mission and exit the mission_recorder.
