# print("Lamp doesn't work. What should we do?")
#
# plug = input("Is the lamp plugged in? ('Y'/'y' for 'Yes', 'N'/'n' for 'No')\n")
# if plug.lower() =='y':
#     bulb = input("Is the bulb burnt out? ('Y'/'y' for 'Yes', 'N'/'n' for 'No')\n")
#     if bulb.lower() =='y':
#         print("Replace the bulb!")
#     else:
#         print("I'm sorry, we have to change the lamp ;(")
# else:
#     print("Plug in the lamp!")

# for i in range(1850, 2123):
#     if i % 4 == 0 and i % 9 == 0:
#         print(i)
#
# print()
#
# for i in range(1850, 2124l,9):
#     if i % 4 != 0 or i % 9 != 0:
#         continue
#     else:
#         print(i)

# month = input('Write the name of the month: ')
#
# if month.lower() in ['january', 'march', 'may', 'july', 'august', 'october', 'december']:
#     print('This month has 31 days.')
# elif month.lower() in ['april', 'june', 'september', 'november']:
#     print('This month has 30 days.')
# elif month.lower() == 'february':
#     print('This month has 28 or 29 days in different years.')
# else:
#     print('There is no such month.')

numbers = []

num = input("Enter your numbers (Press 'Enter' to put in each next number. Enter 0 to finish):\n")
while num != '0':
    numbers.append(int(num))
    num = input()

sum = 0
length = 0
for number in numbers:
    sum += number
    length += 1

average = sum / length
print("Sum:", sum)
print("Average:", round(average, 2))