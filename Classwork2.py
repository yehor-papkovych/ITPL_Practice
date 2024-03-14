# n = int(input("Input how many last lines you want: "))
#
# with open('file.txt', 'r') as file:
#     file_lines = file.readlines()
#     file_lines_reversed = file_lines[::-1]
#     for i in range(n):
#         print(file_lines_reversed[i])

word = input("Enter the word: ")
with open('file.txt', 'r') as file:
    file_lines = file.readlines()
    count = 0
    for line in file_lines:
        words = line.split()
        for i in words:
            if i == word:
                count += 1
    print(count)