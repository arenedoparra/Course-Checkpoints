#Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
string_exercise='Exercise number One'
number_exercise= 1
list_exercise= [1, 2, 3, 4, 5]
boolean_exercise= True

print(string_exercise)
print(number_exercise)
print(list_exercise)
print(boolean_exercise)

#Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 
my_text= 'This is an example text'
print(my_text[:3])

#Exercise 3: Use an index to grab the first element from your list.
list_exercise= [1, 2, 3, 4, 5]
print(list_exercise[0])


#Exercise 4: Create a new number variable that adds 10 to your original number.
original_number= 20
original_number +=10
print(original_number)

#Exercise 5: Use an index to get the last element in your list.
my_list= [4,6,8,10,12,14]
print(my_list[-1 ])


#Exercise 6: Use split to transform the following string into a list. names = 'harry,alex,susie,jared,gail,conner'
names = 'harry,alex,susie,jared,gail,conner'
list_of_names= names.split(',')
print(list_of_names)

#Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.
names = 'harry,alex,susie,jared,gail,conner'
first_name = names.split(",")[0]
first_name_upper = first_name.upper()
new_name = first_name_upper + names[len(first_name):] #en esta última linea he usado ayuda porque no me salía
print(new_name)

#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
age= 27
my_text= f'I am {age} years old'
print(my_text)

#Exercise 9: Print “hello world”.
#Option 1
greeting= 'hello world'
print(greeting)
#option 2
print('hello world')

#Además necesito que me crees una cadena que contenga la palabra "Hola". Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena. Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".
greeting= 'Hola, buenas tardes este es un mensaje de prueba'
find= 'Hola' in greeting
greeting= greeting.replace ('Hola', 'adiós')
print(greeting)