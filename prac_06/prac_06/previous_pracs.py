"""Add Functions to Previous Pracs"""


# Calculate salary for worker level
# def get_valid_worker_level():
#     while True:
#         worker_level = int(input("Enter your worker level (1-10): "))
#         if 1 <= worker_level <= 10:
#             return worker_level
#         else:
#             print("Worker level must be between 1 and 10 inclusive")
#
#
# def calculate_salary(worker_level):
#     return worker_level * 5000
#
#
# def main():
#     worker_level = get_valid_worker_level()
#     salary = calculate_salary(worker_level)
#     print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")
#
#
# main()

def get_user_input():
    rows = int(input("Rows: "))
    columns = int(input("Columns: "))
    return rows, columns


def print_number_grid(rows, columns):
    for i in range(rows):
        for j in range(columns):
            print(j, end=' ')
        print()


def main():
    rows, columns = get_user_input()
    print_number_grid(rows, columns)


main()
