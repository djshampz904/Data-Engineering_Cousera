""" 3. JCU Grades"""
import random


def run_tests():
    print(get_grade(50))
    print(get_grade(85))
    print(get_grade(65))
    print(get_grade(75))


def get_grade(score):
    if score < 50:
        return "F"
    elif score < 65:
        return "P"
    elif score < 75:
        return "C"
    elif score < 85:
        return "D"
    else:
        return "HD"


def print_scores(grade, rand_num):
    print("{} = {}".format(rand_num, grade))


def main():
    score = float(input("Enter score: "))
    while score > 0:
        grade = get_grade(score)
        print("The score {:.1f} is {}".format(score, grade))
        score = float(input("Enter score: "))
    num_scores = int(input("How many random scores: "))
    for i in range(num_scores):
        random_num = random.randint(0, 100)
        grade = get_grade(random_num)
        print_scores(grade, random_num)


main()
