"""
CP1401 2023 TR3 Assignment 1
Program 1 – Pay Calculator
Student Name: <your name>
Date started: <date>
Pseudocode:

Prompt for hours of sleep from user
validate the values and loop till correct value is assigned
Calculate total hours subtract from desired hours
get the debt print string depending on the value of debt
"""
print("Sleep Tracker")

BASE_SLEEP = 8
BASE_DAYS = 5
sum_hours = 0

for i in range(1, BASE_DAYS + 1):
    hour_slept = float(input(f"Night {i} hours sleep: "))
    while True:
        if hour_slept < 0 or hour_slept > 24:
            print("Invalid number of hours.")
            hour_slept = float(input(f"Night {i} hours sleep: "))
        else:
            break
    sum_hours += hour_slept

rec_hours = BASE_SLEEP * BASE_DAYS
sleep_debt = rec_hours - sum_hours

print("\nRecommended total sleep is: {}".format(rec_hours))
print("Your total hours of sleep : {}".format(sum_hours))
if sleep_debt != 0:
    print('Your sleep debt over this time is: {}'.format(sleep_debt))
else:
    print("You are getting enough sleep. Keep it up!")
