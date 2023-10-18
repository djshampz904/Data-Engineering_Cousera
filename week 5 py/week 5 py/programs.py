# 1. Percentage Change
# original = float(input("Original: "))
# change = float(input("Change: "))
# result = original * (1 + change)
#
# print(f"Original: {original}, Change: {change}, Result {result}")

# 2. Time of day
# time = int(input("Time: "))
# action = input("Action (coming or going): ")
# time_string = "before noon" if time < 12 else "after noon"
# action_string = "Hi" if action == "coming" else "Bye"
#
# print(f"It is {time_string} and you are {action}. {action_string}!")

# 3. Coffee Orders
# coffee_type = input("black or white coffee?: ").lower()
# coffee_size = input("Coffee size (small, medium, large): ").lower()
# cost = 4 if coffee_size == "small" else (5 if coffee_size == "medium" else 6)
# if coffee_type == "black":
#     cost -= 1
# print(f"{coffee_type}: {coffee_size} = ${cost}")

# 4. Coffee orders with error-checking
# while True:
#     coffee_type = input("black or white coffee?: ").lower()
#     if coffee_type not in ["black", "white"]:
#         continue
#
#     while True:
#         coffee_size = input("Coffee size (small, medium, large): ").lower()
#         if coffee_size not in ["small", "medium", "large"]:
#             continue
#         else:
#             break
#
#     cost = 4 if coffee_size == "small" else (5 if coffee_size == "medium" else 6)
#
#     if coffee_type == "black":
#         cost -= 1
#
#     print(f"{coffee_type}: {coffee_size} = ${cost}")
#     break

# 5. Accumulation
# low_val = int(input("Low Value: "))
# while True:
#     high_val = int(input("High Value "))
#     if high_val < low_val:
#         print(f"Value should be higher than {low_val}")
#     else:
#         break
# sum_total = 0
# for i in range(low_val, high_val + 1):
#     print(f"{i} ", end="")
#     sum_total = sum_total + i
# print(f"\n{sum_total}", end="")
