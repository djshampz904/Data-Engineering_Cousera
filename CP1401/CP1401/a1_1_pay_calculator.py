"""
CP1401 2023 TR3 Assignment 1
Program 1 – Pay Calculator
Student Name: <your name>
Date started: <date>
Pseudocode:

Ask user for the input for the hours and input for work experience
get the hourly rate by multiplying experience by 0.05 which in increment in pay as experience level rises
get the total pay by multiplying hourly rate and hours

"""
BASE_PAY = 45
print("Experience Counts Pay Calculator")
hours = int(input("Number of hours worked: "))
exp = int(input("\t  Experience level: "))

hourly_rate = BASE_PAY + (BASE_PAY * (0.05 * exp))
total_pay = hourly_rate * hours

print("Based on your experience level ({})".format(exp))
print("Your hourly pay rate is ${:.2f}".format(hourly_rate))
print("Your total pay is ${:.2f}".format(total_pay))
