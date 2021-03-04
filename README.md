```
# main_program.py

This is the script that actually implement all the control loop designed for the behavior of the robot.

During the script, if you are in the INTERACTION LOOP, you can simulate the actions that the child could do with the robot.

Press: 'a' -> Touch, 's' -> push, 'd' -> hit, 'f' -> hug, 'g' -> strongHug, 'h' -> none, 'j' -> MusicalActivity.

## AudioActivity.py

Enables to perform the Musical Activity for the Music Therapy to perform.
Recognition of the beat time.

## Clap.py

Compare the elapsed time of the beats performed by the child with the set frame and recognizes if it corresponds to the beat
timing of the expected song.

## functions_main.py

Credits to Ane San Martin.
It manages all the functions that involve the communication with Arduino (outward) and the functions that manages the
correct response based on the previous action of the child. Also sounds are managed here.

## connections_arduinos.py

Credits to Ane San Martin.
It manages the initialization of the communication between both Arduino Uno/Mega and Raspberry. Also manages all the
inward communication from sonars of the Mega and its status: position of the obstacle (left, front, right), distance, movement 
of the robot (forward, backward, stopped)
