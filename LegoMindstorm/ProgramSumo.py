#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
import time

# Play a sound
brick.sound.beep()

# Initialize a motor at port A and B.
rightMotor = Motor(Port.A)
leftMotor = Motor(Port.B)

# Initialize a colour sensor on port 1
color = ColorSensor(Port.S1)

while True:
    print("Color "+str(color.color()))

# If color is not black 
    if color.color() != Color.BLACK:

# Move forward
    rightMotor.run(300)
    leftMotor.run(300)

# Wait one twentieth of a second
    time.sleep(0.05)

# If color is black
    else:

# Play a sound
    brick.sound.beep(200)

# Backup
    rightMotor.run(-300)
    leftMotor.run(-300)

# Waie one second
    time.sleep(1)

# Spin
    rightMotor.run(-300)
    leftMotor.run(300)

# Wait one second
    time.sleep(1)