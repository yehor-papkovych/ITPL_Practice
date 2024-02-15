import math

# Problem 1
a = 5
b = 6
sum = a + b
print(sum)

a_spare = 5
a = b
b = a_spare
print(a, b)

# a, b - sides of the rectangle
perimeter = 2*a + 2*b
area = a*b
print("Perimeter:", perimeter, ", Area:", area)

# Problem 2
radius = 2
circumference = 2*3.14*radius
area_circle = 3.14*(radius**2)
print("Circumference:", circumference,", Area circle", area_circle)

temp_celcius = 30
temp_fahrenheit = 9/5*temp_celcius+32
print("Fahrenheit:", temp_fahrenheit)

a = 1
b = 4
c = 3
discriminant = b**2 - 4*a*c
if discriminant < 0:
    print("Can't do complex numbers")
elif discriminant == 0:
    root = -b/(2*a)
    print("Root:", root)
else:
    root1 = (-b + discriminant ** (1/2)) / (2*a)
    root2 = (-b - discriminant ** (1/2)) / 2
    print("Root1:", round(root1, 2), ", Root2:", round(root2, 2))

principal = 1000
APR = 0.03
years = 10
amount = principal*((1+ APR/100)**years)
print("Compound interest:", round(amount, 2))