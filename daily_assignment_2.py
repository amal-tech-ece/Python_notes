# marks = [95, 82, 76, 61, 48, 105, -10, 75]
# def calculate_grade(mark):
#     if 90 <= mark <= 100:
#         return "A+"
#     elif 80 <= mark <= 89:
#         return "A"
#     elif 70 <= mark <= 79:
#         return "B"
#     elif 60 <= mark <= 69:
#         return "C"
#     elif 50 <= mark <= 59:
#         return "D"
#     else:
#         return "F"

# valid_marks = []
# total = 0
# for mark in marks:
#     if 0 <= mark <= 100:      
#         grade = calculate_grade(mark)
#         print(mark, "->", grade)
#         valid_marks.append(mark)
#         total += mark

# print("Valid Marks :", len(valid_marks))
# print("Average :", total / len(valid_marks))




# sentence = input("Enter a sentence: ")
# words = sentence.split()
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