# start with an empty list
my_list = []

# add some numbers
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# put 15 in the second spot
my_list.insert(1, 15)

# add more numbers from another list
my_list.extend([50, 60, 70])

# get rid of the last one
my_list.pop()

# sort them smallest to biggest
my_list.sort()

# find where 30 is
pos = my_list.index(30)
print("Index of 30:", pos)

# see the final list
print(my_list)