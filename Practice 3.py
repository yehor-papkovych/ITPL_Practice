# Problem 1

# print("Please enter your number. Make sure it is an integer value.")
#
# num = int(input())
#
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# Problem 2

# score = int(input("Please enter the exam score: "))
#
# if score > 100 or score < 0:
#     print("There cannot be such a grade.")
# elif score >= 90 and score <= 100:
#     print("The grade is A.")
# elif score >= 80:
#     print("The grade is B.")
# elif score >= 70:
#     print("The grade is C")
# elif score >= 60:
#     print("The grade is D.")
# else:
#     print("The grade is F.")

# Problem 3

# def fibonacci(number):
#     a = 0
#     b = 1
#
#     for i in range(2, n + 1):
#         a, b = b, a + b
#
#     return a
#
#
# n = int(input("Which number of the sequence you would like to output?\n"))
#
# print(fibonacci(n))

# Problem 4

# n = int(input("Which factorial you would like to output?\n"))
#
# result = 1
# for i in range(1, n + 1):
#     result *= i
#
# print(result)

# Problem 5:

rows = int(input("Input the number of rows you want (if the number is even, 1 row will be added): "))

if rows % 2 == 0:
    rows += 1

for i in range(1, rows // 2 + 1):
    spaces = rows // 2 - i
    print(" " * spaces, end='')
    print("*" * (2*i - 1), end='')
    print(" " * spaces)

for i in range(rows // 2 - 1, 0, -1):
    spaces = rows // 2 - i
    print(" " * spaces, end='')
    print("*" * (2*i - 1), end='')
    print(" " * spaces)
