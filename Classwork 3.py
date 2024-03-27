from math import pi

# class Numeral:
#
#     def __init__(self, int_num):
#         self.int_num = int_num
#
#     def int_to_roman(self):
#         list_of_transitions = [(1000, 'M'), (900, 'CM'), (500, 'D'),
#                  (400, 'CD'), (100, 'C'), (90, 'XC'),
#                  (50, 'L'), (40, 'XL'), (10, 'X'),
#                  (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
#
#         i = 0
#         while self.int_num > 0 and i < len(list_of_transitions):
#             div = self.int_num // list_of_transitions[i][0]
#             self.int_num %= list_of_transitions[i][0]
#
#             while div > 0:
#                 print(list_of_transitions[i][1], end = '')
#                 div -= 1
#
#             i += 1
#
# num1 = Numeral(23)
# num1.int_to_roman()

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return pi * self.radius * self.radius
#
#     def perimeter(self):
#         return 2 * pi * self.radius
#
# circle = Circle(5)
# print(circle.area())
# print(circle.perimeter())
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
# rectangle = Rectangle(5, 10)
# print(rectangle.area())

# class Rectangle: