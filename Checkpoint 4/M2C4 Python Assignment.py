#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
my_list = ['apple', 'banana', 'pear']
print(my_list)

my_tuple = ('red', 'green', 'blue')
print(my_tuple)

my_float=19.99
print(my_float)

my_integer= 200
print(my_integer)

from decimal import Decimal
my_decimal = Decimal('19.99')
print(my_decimal)

my_dictionary = {
    "apple": "red",
    "banana": "yellow",
    "orange": "orange",
    "kiwi": "green"
}
print(my_dictionary)


#Exercise 2: Round your float up.
import math
my_float = 19.99
print (math.ceil(my_float))


#Exercise 3: Get the square root of your float.
import math
my_float = 19.99
print (math.sqrt(my_float))


#Exercise 4: Select the first element from your dictionary.
my_dictionary = {
    "apple": "red",
    "banana": "yellow",
    "orange": "orange",
}
print(list(my_dictionary.items())[0])


#Exercise 5: Select the second element from your tuple.
my_tuple = ('red', 'green', 'blue')
print(my_tuple[1])

#Exercise 6: Add an element to the end of your list.
my_list = ['apple', 'banana', 'pear']
my_list.append("kiwi")
print(my_list)


#Exercise 7: Replace the first element in your list.
my_list = ['apple', 'banana', 'pear']
my_list[0] = "orange"
print(my_list)


#Exercise 8: Sort your list alphabetically.
my_list = ['apple', 'banana', 'pear']
my_list.sort()
print(my_list)


#Exercise 9: Use reassignment to add an element to your tuple.
my_tuple = ('red', 'green', 'blue')
my_tuple += ('yellow',)
print(my_tuple)

