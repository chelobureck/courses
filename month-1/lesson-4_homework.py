# working with lists

data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')


# 1)
letters = []
numbers = []


# 2)
for data_tuple_vallue in data_tuple:
    if isinstance(data_tuple_vallue, str):
        letters.append(data_tuple_vallue)
    else:
        numbers.append(data_tuple_vallue)


# 3)
numbers.remove(6.13)

letters.append(numbers[0])
del numbers[0]

numbers.insert(1, 2)


# 4)
numbers.sort()
letters.reverse()
letters[-2] = "c"
letters[1] = "G"


# 5)
numbers = [num ** 2 for num in numbers]


# 6)
print(tuple(letters))
print(tuple(numbers))