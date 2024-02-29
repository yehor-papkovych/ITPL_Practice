# # Part 1
# n = int(input("Input the number: "))
# list1 = []
# for i in range(n):
#     t = int(input("Input number {} : ".format(i+1)))
#     list1.append(t)
#
# print(list1)
# sum = 0
# for i in list1:
#     sum += i
# average = sum / n
# print(average)

# Part 2
# n = int(input("Input the number: "))
# list1 = []
# for i in range(n):
#     t = int(input("Input number {} : ".format(i+1)))
#     list1.append(t)
# print(list1)
# m = int(input("Input the number by which all the numbers will be multiplied: "))
# list2 = [i * m for i in list1]
# print(list2)

# Part 3
# str1 = 'spam'
# str2 = 'ni!'
# print("The Knights who say, " + str2)
# print(3 * str1 + 2 * str2)
# print(str1[1])
# print(str1[1:3])
# print(str1[2] + str1[:2])
# print(str1 + str2[-1])
# print(str1.upper())
# print(str2.upper() * 3)

# Part 4
# for ch in 'aardvark':
#     print(ch)
#
# for w in " Now is the winter of our discontent...".split():
#     print (w)
#
# for w in "Mississippi".split("i"):
#     print(w, end=" ")
#
# msg = ""
# for s in "secret".split("e"):
#     msg = msg + s
#     print(msg)
#
# msg = ""
# for ch in "secret":
#     msg = msg + chr(ord(ch) + 1)
#     print(msg)

# Part 5
# person = {'Fist name': 'Man', 'Last Name': 'Human', 'Age': 20, 'City': 'Kyiv'}
# for key, value in person.items():
#     print(key, ':', value)

# Part 6:
glossary = {'Stack': 'Stacks are a data structure that follows the Last-in-First-Out (LIFO) principle',
            'Queues': 'Queues follow the First-in-First-Out (FIFO) principle',
            'Dictionaries': 'Dictionaries map keys to values and store them in an array or collection. The key-value pairs are commonly known as item',
            'Tuples': 'Tuples are immutable and can store a fixed number of items',
            'Lists': 'Python’s list is a flexible, versatile, powerful, and popular built-in data type. It allows you to create variable-length and mutable sequences of object.'}

for key, value in glossary.items():
    print(key, ':', value)
    print()