# Author: Oguntuase Victor
# Description: Week 2 Assiginment for PLP python course

my_list = []    # Create an empty list called my_list.
appendables = [10, 20, 30, 40]

# Append the following elements to my_list: 10, 20, 30, 40.
for element in appendables:
    my_list.append(element)

# Insert the value 15 at the second position in the list.
my_list.insert(1, 15)

# Extend my_list with another list: [50, 60, 70].
extendable = [50, 60, 70]
my_list.extend(extendable)

# Remove the last element from my_list.
my_list.pop()

# Sort my_list in ascending order (although List is already sorted in asc order).
my_list.sort()

# Find and print the index of the value 30 in my_list.
print(my_list.index(30))
