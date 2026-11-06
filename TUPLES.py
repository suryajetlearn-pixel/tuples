stuDetails = ('Surabhi', 89)

# Packing
address = ('227', 'Brickfield Shelters', 'Bangalore', 'Karnataka', '562107')

for x in address:
    print(x, end=' ')

# Unpacking
houseno, apartName, city, state, pin = address

print()
print('HNO', houseno)
print('APT NO ', apartName)
print(city)
print(state)
print(pin)

# A tuple can also be created without using parentheses
my_tuple = 3, 4.6, "dog"
print(my_tuple)

# Nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# Nested index
print(n_tuple[0][3])    # 's'
print(n_tuple[1][1])    # 4

# Activity for the kids
# Accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# Elements 2nd to 4th
# Output: ('r', 'o', 'g')
print(my_tuple[1:4])

# Elements beginning at 2nd
# Output: ('r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[1:])

# Elements 8th to end
# Output: ('i', 'z')
print(my_tuple[7:])

# Elements beginning to end
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[:])

# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])

# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 9

# However, an item of a mutable element can be changed
my_tuple[3][0] = 9
# Output: (4, 2, 3, [9, 5])
print(my_tuple)

# Tuples can be reassigned
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple)