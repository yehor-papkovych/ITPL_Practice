# Part 1

# with open('learning_python.txt', 'r') as learn:
#     # print(learn.read())
#     # for line in learn:
#     #     print(line)
#     learn_list = learn.readlines()
#
# for line in learn_list:
#     print(line)

# Part 2

# name = input("Enter your name: ")
# while name.lower() != 'n':
#     print('Hello,', name)
#     with open('guests.txt', 'a') as guests:
#         guests.write(f"{name}\n")
#     name = input("Enter your name (if you want to stop, type 'N'/'n'): ")

# Part 3

def wc(file):
    with open(file, 'r') as file:
        count_lines = 0
        count_words = 0
        count_characters = 0
        for line in file:
            count_lines += 1
            for word in line.split():
                count_words += 1
                for char in word:
                    count_characters += 1
        return count_lines, count_words, count_characters

print("The numbers are:", wc("learning_python.txt"))