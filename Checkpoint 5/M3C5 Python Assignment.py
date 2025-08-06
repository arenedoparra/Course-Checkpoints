#Cree un bucle For de Python
for num in range(1, 11):
    print(num)

#Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
def suma(a, b, c):
    return a + b + c

resultado = suma(10, 20, 30)
print(resultado) 


#Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
suma = lambda a, b, c: a + b + c

resultado = suma(10, 20, 30)
print(resultado) 

#Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.

nombre = 'Enrique'

lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

if nombre in lista_nombre:
    print(f"{nombre} está en la lista.")
else:
    print(f"{nombre} no está en la lista.")
