# SPOT-navigation

The project is divided into both social and navigation focused teams, both producing a database of
SPOT’s data. This project aims to establish systems for data collection that can be used in future
research projects in the INSITE lab related to SPOT.

<!--
Copyright (c) 2021 Boston Dynamics, Inc.  All rights reserved.

Downloading, reproducing, distributing or otherwise using the SDK Software
is subject to the terms and conditions of the Boston Dynamics Software
Development Kit License (20191101-BDSDK-SL).
-->

# E-Stop

To run the E-Stop as a GUI:
```
python3 estop_gui.py --username USER --password PASSWORD ROBOT_IP
```
To run the E-Stop without a GUI:
```
python3 estop_nogui.py --username USER --password PASSWORD ROBOT_IP
```

### GUI Version
The GUI version of the example has two buttons. The red `STOP` button
engages the robot's E-Stop system, which cuts off power to all the motors. This operation also
changes the E-Stop status to `ESTOP_LEVEL_CUT`. To release the E-Stop and transition the robot to
an operational state, press the green `Release` button.

### Command-line version without a GUI
Similar to the usage of the GUI version, the non-GUI version of the example uses `Space` for
engaging the E-Stop system and `r` for releasing it. 