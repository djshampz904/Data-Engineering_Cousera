def run_tests():
    bmi = calculate_bmi(2, 60)
    print(bmi)  # This should be 15.0
    bmi = calculate_bmi(1.5, 100)
    print(bmi)  # This should be 44.4
    bmi = calculate_bmi(1.75, 80)
    print(bmi)
    height = get_valid_number("Height (m): ", 0, 3)
    print(height)
    weight = get_valid_number("Weight (kg): ", 0, 300)
    print(weight)


def calculate_bmi(height, weight):
    return weight / (height ** 2)


def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    if bmi < 25:
        return "normal"
    if bmi < 30:
        return "overweight"
    return "obese"


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def main():
    height = get_valid_number("Height (m): ", 0, 3)
    print(height)
    weight = get_valid_number("Weight (kg): ", 0, 300)
    print(weight)
    age = get_valid_number("Age :", 0, 150)
    print(age)
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    print("Your age is {:.0f} BMI is {:.1f}, which is considered {}".format(age, bmi, category))


# run_tests()
# print(determine_weight_category(16.5))  # This should be underweight
# print(determine_weight_category(25))  # This should be overweight
main()
