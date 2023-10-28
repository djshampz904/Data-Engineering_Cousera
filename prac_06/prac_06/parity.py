"""2. Parity"""


def run_tests():
    print_parity(2)
    print_parity(4)
    print_parity(41)


def print_parity(number):
    print('Parity of {:.0f} should be {:.0f}: {:.0f}'.format(number, get_parity(number), get_parity(number)))


def get_parity(number):
    return number % 2


def is_odd(number):
    if get_parity(number) == 0:
        return False
    return True


def main():
    number = float(input("Number: "))
    print_parity(number)
    print(is_odd(number))


# run_tests()

main()
