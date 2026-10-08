# numbers = (10, 20, 5, 15, 20, 30, 5, 40, 10)

# duplicates = []

# for num in numbers:
#     if numbers.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)

# for n in duplicates:
#     print(n)

# duplicates = tuple(sorted(duplicates))

# print("Duplicate Values :", duplicates)
# print("Sum of Duplicate Values :", sum(duplicates))



# try:
#     a = 100
#     b = int(input("Enter second value: "))
#     c=a/b
#     print(c)
# except ValueError:
#     print("Invalid number")

# except ZeroDivisionError:
#     print("Cannot divide by zero")



# sentence = input("Enter a sentence: ")

# words = sentence.lower().split()


# print("Number of Words :", len(words))


# longest = words[0]
# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print("Longest Word :", longest)


# frequency = {}

# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1

# print("\nWord Frequency:")
# for word, count in frequency.items():
#     print(word, ":", count)


# print("\nRepeated Words:")
# for word, count in frequency.items():
#     if count > 1:
#         print(word)