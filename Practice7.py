import math

# Task 1
# class BankAccount:
#     def __init__(self, account_holder_name, account_number, balance=0):
#         self.account_holder_name = account_holder_name
#         self.account_number = account_number
#         self.balance = balance
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance -= amount
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def display_balance(self):
#         print("You, {}, have {}$ on your bank account #{}.".format(self.account_holder_name, self.balance, self.account_number))
#
# bank_account = BankAccount('Yehor Papkovych', '12345', 10000)
# bank_account.withdraw(500)
# bank_account.deposit(800)
# bank_account.display_balance()


# Task 2
# class Vector:
#     def __init__(self, components):
#         self.components = components
#
#     def magnitude(self):
#         sum = 0
#         for component in self.components:
#             sum += component ** 2
#         return math.sqrt(sum)
#
#     def add(self, vector):
#         new_vector = Vector([])
#         for i in range(len(self.components)):
#             new_vector.components.append(self.components[i] + vector.components[i])
#         return new_vector
#
#     def dot_product(self, vector):
#         dot_product = 0
#         for i in range(len(self.components)):
#             dot_product += self.components[i]*vector.components[i]
#         return dot_product
#
# v1 = Vector([1, 2, 3])
# v2 = Vector([2, 3, 4])
# print(v1.add(v2).magnitude())
# print(v1.dot_product(v2))

# Task 3
class Employee():
    def __init__(self, name, id_number, department):
        self.name = name
        self.id_number = id_number
        self.department = department


    def display(self):
        print("This is {}. Their id number is {}. They work at {} department.".format(self.name, self.id_number, self.department))

employee = Employee("John", "123", "IT")
employee.display()