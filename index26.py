

numbers = [12, 5, 8, 12, 15, 7, 5, 20, 8, 10]
def find_largest():
    largest = 999
    for num in numbers:
        if num < largest:
            largest = num
    print("Largest Value:", largest)

find_largest()