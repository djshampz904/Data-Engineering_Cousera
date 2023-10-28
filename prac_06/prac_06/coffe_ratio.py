"""1. Coffee Brew Ratio"""

"""
defining functions to calculate the brew ratio, 
determine the coffee style based on the ratio, and get a valid number within a specified range. 
prompt the user to input the dose (ground coffee) and yield (brewed coffee) 
within the range of 0 to 100. It calculates the brew ratio and determines the coffee style 
(ristretto, normale, or lungo) based on the ratio.print in the format 
"1:{ratio} is considered {style}."
"""


def run_tests():
    style = determine_coffee_style(1)
    print(style)  # This should be a ristretto
    style = determine_coffee_style(2)
    print(style)  # This should be normal
    style = determine_coffee_style(13.5)
    print(style)  # This should be lungo


def calculate_ratio(plyeild, dose):
    ratio = plyeild / dose
    return ratio


def determine_coffee_style(ratio):
    if ratio < 2:
        return "ristretto"
    if ratio < 3:
        return "normale"
    if ratio >= 3:
        return "lungo"


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def main():
    dose = get_valid_number("Dose: ", 0, 100)
    plant_yield = get_valid_number("Yield: ", 0, 100)
    ratio = calculate_ratio(plant_yield, dose)
    style = determine_coffee_style(ratio)
    print("1:{:.1f} is considered {}".format(ratio, style))


# run_tests()
main()
