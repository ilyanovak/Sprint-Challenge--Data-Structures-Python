import time
from linkedlist import LinkedList
from stack import Stack

# start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
count = 0
for name_1 in names_1:
    for name_2 in names_2:
        count += 1
        if name_1 == name_2:
            duplicates.append(name_1)
print('count', count)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# Created linked lists

start_time = time.time()

ll_names_1 = LinkedList()
for name_1 in names_1:
    ll_names_1.add_to_tail(name_1)
assert(len(names_1) == ll_names_1.__len__())

ll_names_2 = LinkedList()
for name_2 in names_2:
    ll_names_2.add_to_tail(name_2)
assert (len(names_2) == ll_names_2.__len__())

# # Compare linked lists
name_1 = ll_names_1.head # start name_1 at its head
name_2 = ll_names_2.head  # start name_21 at its head

duplicates = []

# while name_1 value is not None
count = 0
while name_1:
    # while name_2 is not None
    count2 = 0
    while name_2:
        count += 1
        # if name_1 value matches name_2 value
        if name_1.get_value() == name_2.get_value():
            # add matching value to duplicates list
            duplicates.append(name_1.get_value())
            # end current loop
            break
        else:
            # move to next name_2
            name_2 = name_2.get_next()

    # move to next name_1
    name_1 = name_1.get_next()
    # return name_2 to head value
    name_2 = ll_names_2.head

print('count', count)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

start_time = time.time()

duplicates = set(names_1).intersection(names_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# Create stacks

start_time = time.time()

stack_names_2 = Stack()
for name_2 in names_2:
    stack_names_2.push(name_2)
assert (len(names_2) == stack_names_2.__len__())

duplicates = []

# while list of names_2 has not reached None yet
while stack_names_2.storage.tail:
    # loop through all names in names_1
    for name_1 in names_1:
        # if name_1 matches name_2
        if name_1 == stack_names_2.storage.tail.get_value():
            # append name_1 value to duplicates and pop it
            duplicates.append(name_1)
            # end the loop
            break

    stack_names_2.pop()

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
