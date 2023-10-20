"""
CP1401 2023 TR3 Assignment 1
Program 1 – Pay Calculator
Student Name: <your name>
Date started: <date>
Pseudocode:

Ask for number of practises as input from user
ask for input for whether they mow the lawn
check if its at least 7 practises
options allowed are yes and no
"""

BASE_TIME = 15
print("Device Time Determinator")

num_practises = int(input("Number of practices: "))
mow_lawn = input("Did you mow? ").lower()

device_time = BASE_TIME * num_practises

if mow_lawn == 'no':
    print("No device time :(")
elif mow_lawn == "yes" and num_practises >= 7:
    print("You get {} minutes of device time :)\nAnd you get a cupcake!".format(device_time))
else:
    print("You get {} minutes of device time :)".format(device_time))
