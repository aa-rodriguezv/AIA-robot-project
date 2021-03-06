# AIA-robot-project

Path of the Project already configured in the Nano Jetson Server of the university: /home/disciotlab/thesis/aa-rodriguezv/AIA-robot-project
Result files in Nano Jetson Server of the univeristy: /home/disciotlab/jetson-inference/data/coloredbags & /home/disciotlab/jetson-inference/data/bags_final.txt

## Prerequisites

### Prepare All Hardware

1. Ensure that the RFID server is on and connected to the Antenna. 
2. Turn on the Nano Jetson and connect it to a Camera (which has to be looking at the bands). The Nano Jetson also has to be connected via LAN to a local network.
3. Make sure the Robot is turned on and has an available IP.
4. Turn on the band mechanism with the OneStopUltrasound.py code.
5. Make sure you have a json config file with an API Key for accessing BigQuery. This file is provided in the Google Cloud Console. More on the documentation for connecting with BigQuery here: [BigQuery-Python Open Source Module](https://github.com/tylertreat/BigQuery-Python)

### Prepare Communication

All of the different devices should be connected under the same network. 

1. On the RFID code (RFID_module_communication.py): Modify the IP on line 21 to match the one on the Nano Jetson, for this check it with 'ip address' on a terminal and check for the 'LAN' section of the output.
2. On the Nano Jetson code (nano_jetson_final_integration.py): Modify the robot_ip on line 29 and the bands_txt_controller_ip on line 40.

## Execution

### Start Up the Services

Please start up in the order that they are listed: 

1. Make sure the RFID server is running and the cursor is placed on the terminal. 
This can be achieved by either running "python PATH_TO_REPO/communication_trials/RFID_module_communication.py" via a terminal (cursor is already placed for input) 
or, if the program is running in an IDE, you have to mannualy place the cursor on the terminal.
2. Ensure the Docker Container on the Nano Jetson is running. For this you have open up a terminal on the Nano, cd into 'jetson-inference/' and run 'sudo docker/run_perisist_detection_dir.sh'. (This has to be done exactly as stated, the docker bash won't run if you cd into the folder that is placed. It has to be run from the parent folder).
3. IN A NEW TERMINAL: Run the Nano Jetson server. 'python PATH_TO_REPO/communication_trials/nano_jetson_final_integration.py'.
4. Place the bags on the bands.

### Run the entire System

Once everything is ready you can run RFID tags through the antenna and everything should be working smoothly.

### During the First Execution

**PLEASE, DO NOT SKIP THIS PART.**

As a one time thing for the Bands TXT Controller you have to 'OK' the connection with the Nano. This is done on the visual interface of the controller for the first connection only (once the first tag is run through the antenna).


## For Only Trying Out the Object Detection Model

Camera Placement: Run 'camera-capture /dev/video0' to see what the camera sees and adjust it.

1. Turn on the Nano Jetson and connect it to a Camera (which has to be looking at the bands).
2. Ensure the Docker Container on the Nano Jetson is running. For this you have open up a terminal on the Nano, cd into 'jetson-inference/' and run 'sudo docker/run_perisist_detection_dir.sh'. (This has to be done exactly as stated, the docker bash won't run if you cd into the folder that the code is placed. It has to be run from the parent folder).
3. Place the bags on the bands.
4. Run, on the same terminal where the Docker Container is runnig, the inside_docker_container.py file. First cd into 'cd /jetson-inference/python/training/detection/ssd' and then run 'python3 inside_docker_container.py'. 

This should show you the Inference Time and the Objects Detected.

**PS**: The docker subprocess activated by the Nano, once the system is ready, is the code documented here: [Inside Docker Container](https://github.com/aa-rodriguezv/pytorch-ssd-modified-AIA-thesis/blob/master/inside_docker_container_final.py). Which, in turn, was forked from  [Pytorch SSD Repository](https://github.com/dusty-nv/pytorch-ssd) to manage Neural Networks with Pytorch.

**PSS**: The Nano Jetson SHOULD ALWAYS be connected to a Keyboard, a Mouse and a Monitor.






