var_list = []
print(var_list)
var_list = [1, 2, 3]
print(var_list)

# var_list = list([1,2,3])
# print(var_list)


# copy by reference example of list
var_list_main = [2, 4, 6, 8, 10]

print(var_list_main)

var_list_copy = var_list_main

print(var_list_copy)
var_list_copy.pop()

print(var_list_copy)
print(var_list_main)

# copy by value example of list
var_list_main = [2, 4,4, 6, 8, 10]
var_list_copy = var_list_main.copy()

# to append some value
var_list_main.append(123)
print(var_list_main)

# to remove last value
var_list_main.pop()
print(var_list_main)

# to remove specific value
var_list_main.remove(4)
print(var_list_main)

# to remove value at specific index
var_list_main.pop(0)

# how append and extend are different
generic_list = [1, 1.0, 'string', True, [1,2], {'key':'value'}]
print(generic_list[3])
print(generic_list[4])

generic_list.append([1,2,3])
print(generic_list)

# for extend

main_list = []

main_list.append([1,2,3])
main_list.append([4,5,6])
main_list.append([7,8,9])

print(main_list)

main_list = []  

main_list.extend([1,2,3])
main_list.extend([4,5,6])
main_list.extend([7,8,9])
# main_list.extend({'key':'value'})
print(main_list)


var_str = 'mike tyson'
print(var_str.title())
print(var_str)

var_list_main = [2, 4, 6, 8, 10]
print(var_list_main)
var_list_copy = var_list_main.copy()
print(var_list_copy)
var_list_copy.pop()
print(var_list_copy)
print(var_list_main)



list_of_all_dt = ['Alpha', 1, 1.1, True, [1,2]]
print(list_of_all_dt)


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

names = ['string', 1, True, 1.0, ['list', 'one'], {'age':20}]
print(names)

copy_bicycles = bicycles

copy_bicycles.pop()
print(copy_bicycles)
print(bicycles)

copy_bicycles = bicycles.copy()
copy_bicycles.pop()
print(copy_bicycles)
print(bicycles)




copy_bicycles[0] = 'bmw'
print(copy_bicycles)
print(bicycles)


# Accessing Elements in a List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
names = ['string', 1, True, 1.0, ['list', 'one'], {'age':20}]
print(names)

list_within_list = [
    [1,2,[1,2,3]]
    ]

list_within_list[0][2][0]

# how to access elements in a list
names[5]

# slicing in list 
list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
list_of_numbers[3:]
list_of_numbers[:7]

list_of_numbers[3:7]

list_of_numbers[1::2]


print(bicycles[0])

print(names[4][1])
# print(names[5]['age'])

print(bicycles[0].title())

"muhammad mike tyson ".title()

# Using Individual Values from a List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
name = 'mike tyson'
age = 28
name_list = ['mike', 'tyson']
# print(f"hi, my name is: {name_list[0]} {name_list[1]}")

print(f"my name is {name}, age {age}")

print(f"hi, my name is: {name} and age is: {age}")


print(f"hi this is {name} {names}")

message = f"this is my message: {bicycles[0]} {bicycles[1]} {names[0]}"
print(message)

message = f"this is my message: {bicycles[0]}, {bicycles[1]}"
print(message)

message = f"My first bicycle was a {bicycles[0].title()}."

print(message)

string = 'abcdef efg'
list_ = [1, 2, 3, 4, 5, 6]
string[0]
string[6]
string[0:5]
string[:5]
string[0:]
string[:]

list_[0:3]
list_[2:3]

# iterate over something



for i in range(1,10,2):
    print(f"this is value {i}")

print()

for i in range(0, 10, 2):
    print(f"this is index {i}")
    
for i in range(10, 0, -1):
    print(f"this is index {i}")


for i in range(10):
    print(i)
    
for i in range(4,10):
    print(i)
    
for i in range(10,4,-2):
    print(i)

list_ = [1,2,3,4,5,6,7,8,9,10]
list_[1::2]


names = ['mike', 'usama', 'waqar']
ages = [28, 26, 30]
for name in names:
    print(name)

for i in range(len(names)):
    print(f"my name is {names[i].title()} and age is {ages[i]}")
    # print(names[i])

for char in 'mike'[:2]:
    print(char)

# len(names)
len(name)
len('name')
names[0]
names[1]

for i in range(len(names)):
    # print(i, names[i])
    print(f"at index: {i}, name is {names[i]}")
    
for name in names:
    print(name)

# [(0,'mike'), (1, 'usama') ....]

for i, name in enumerate(names):
    print(f"index: {i} value: {name}")


for i, name in enumerate(names):
    print(f'hello {name}, at index {i}')
    # print(f'hello {name} at index: {i}')

for index, name in enumerate(names):
    if index <= 2:
        continue
    print(index, name)

a,b,c,d,e = 'aaa', 'bbb', '', '', ''
print(a)
print(b)


i, j = (0,'mike')

print(i,j)

for obj in enumerate(names):
    print(obj)

name = 'mike'

# Try these short programs to get some firsthand experience with Python’s lists. You might want to create a 

# 3-1. Names: Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, 
# print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, 
# and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

# Changing, Adding, and Removing Elements

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
motorcycles[0] = 'ducati' 
print(motorcycles)

# Adding Elements to a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

popped_value = motorcycles.pop()
print(motorcycles)
# Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(2, 'ducati')
print(motorcycles)

# Removing Elements from a List
# Removing an Item Using the del Statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)

del motorcycles[0]
print(motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Removing an Item Using the pop() with index Method
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle)

# Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
motorcycles.remove('ducati')


# Sorting a List Permanently with the sort() Method

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

print(cars)

sorted_cars = sorted(cars)

for i in sorted(cars, reverse=True):
    print(i)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) 
print(cars)

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:") 
print(cars)
print("\nHere is the sorted list:") 
print(sorted(cars))
print("\nHere is the original list again:") 
print(cars)

# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

index = [2, 0, 3, 1]
temp = []
for i in index:
    temp.append(cars[i])
print(temp)

print(cars)

print(', '.join(cars))

print(', '.join(cars))
type(', '.join(cars))

print('m mike tyson'.capitalize())
'mike tyson'.title()
'mike tyson'.upper()

for i in range(len(cars)):
    print(i, len(cars[i]))

for i in range(10, 0, -1):
    print(i)

cars[:]

cars[::-1]
print(cars)
cars[0:4:4]