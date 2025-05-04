# CONDICIONALES EN PYTHON: 

## ¿Qué es un condicional?
Los **condicionales** son de los elementos fundamentales que hacen python dinámico, hacen que el programa  que crees pueda empezar a tomar decisiones. Estos permiten que nuestro programa tome decisiones y ejecute acciones diferentes según ciertas condiciones. Esta estructura, permite ejecutar un bloque de código u otro dependiendo de si una condición se cumple (True) o no, son tipos de respuestas de SI o NO.
Los condicionales pueden tener direntes niveles, siguiendo una estructura de arbol, donde existen diferentes escenarios y acciones.

 _Si ocurre X situación, quiero que como programa, quiero que realices X tarea, pero si ocurre Y quiero que realices ortra tarea_
 
## Sintaxis básica
```python
if condición:
    # Si la condición es verdadera
else:
    # Si ninguna condición anterior se cumple
elif otra_condición:
    # Si la primera condición no se cumple pero esta sí
```

### Ejemplo

```python
edad = 30

if edad < 25:
    print("Lo siento, necesitas tener 25 años")
else:
    print("Adceptado, tienes{edad} años")
elif temperatura < 100:
    print("Lo siento {edad} es muy viejo") #Ya que en elif hay dos condiciones, esta deberá ir en medio, porque primero comprobará estas dos y si son falsas ejecutará una tercera.

```

# BUCLES EN PYTHON (_LOOPS_)
## ¿Qué es un Bucle?
Los **bucles** son herramientas de codigo que nos permiten repetir instrucciones multiples veces sin tener que escribir el mismo codigo. Hay dos tipos de _loops_ en python:
- For...In
- While

Ambos se pueden usar para iterar colecciones, un rango de numeros, listas etc. Ambos bucles son útiles para automatizar tareas como recorrer listas, repetir cálculos, etc.


## Diferentes tipos de bucles
### Bucle `for...in`
Repite una acción sobre cada elemento de una secuencia (lista, string, rango...). Por ejemplo; si tenemos una máquina con bolas de juguete dentro, este tipo de bucle, sería la capacidad de darle vueltas a la rueda, tantas veces como bolas de juguete haya. Tenemos un principio y un final bien definidos.

**Ejemplo**
```python
for num in range(6):
    print(num)
```
**Salida**
> 0  
> 1  
> 2  
> 3  
> 4  
> 5

### Bucle `while`
Repite una acción **mientras** se cumpla una condición. No es tan inteligente como el for..in loop. este, continuará ejecutandose cuando llega al final hasta entrar en un bucle infinito si no se configura correctamente. Es por ello que a un _While_ loop hay que decirle cuando parar y a esto se le llama _centinel value_.

**Ejemplo**
```python
nums=list(range(1,100))
 while len(nums) > 0:  
    print(nums.pop())
```

# Listas por Comprensión
Una **lista por comprensión** es una forma rápida de construir nuevas listas aplicando operaciones o condiciones sobre un iterable. Se pueden configurar una serie de for..in loops para funcionar en unsa sola linea y generar listas a partir de esas lineas de codigo, es un set de bubles.

### Sintaxis

```python
[nueva_expresión for elemento in iterable if condición]
```

### Ejemplo

```python
cuadrados = [x**2 for x in range(10)]
```

> Resultado: `[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`

También puedes incluir condiciones:

```python
pares = [x for x in range(10) if x % 2 == 0]
```

> Resultado: `[0, 2, 4, 6, 8]`

# Argumentos en Python 
Los **argumentos** son valores que enviamos a una función para que los utilice internamente.

## Ejemplo
```python
def nombre_completo(nombre, apellido):
    print(f"Hola, {nombre}{apellido}!")

nombre_completo("Ane" , 'Renedo')
```

> Salida: `Hola, Ane Renedo`

## Tipos de argumentos

- **Posicionales**: se pasan en orden.
- **Nombrados**: se pasan con nombre.
- **Con valor por defecto**: tienen un valor si no se indica otro.

```python
def saludar(nombre="estudiante"):
    print(f"Hola, {nombre}!")
```

---

# FUNCIONES LAMBDA:
## ¿Qué es una función Lambda en Python?
Es una herramienta que nos permite empaquetar una función en general una funcion más pequeña y luego introducirla en otras funciones. Con ella, podemos unir un comportamiento, un proceso. SOn muy similares a una variable, moviles y faciles de usar. 

    Una **lambda** nos permite empaquetar rápida y facilmente una funcionalidad, almacenarla en una variable y luego, inrtoducir ese valor, ese preceso, en otras funcioenes y en otras partes del programa. Es una forma rápida de definir funciones pequeñas en una sola línea.

## Sintaxis:
```python
lambda argumentos: expresión
```

## Ejemplo:
```python
nombre_completo = lambda nombre, apellido: f '{nombre} {apellido}'
def greeting (nombre)
print(f'Hola {nombre})

saludo(nombre_completo('Ane', 'Renedo')) 
# Salida: Hola Ane Renedo

```
---

# pip: Instalación de paquetes en Python

## ¿Qué es un paquete pip?
**`pip`** es el sistema de gestión de paquetes de Python. Te permite instalar bibliotecas externas para apliar las funcionalidades de tu programa. Estos paquetes externos se importan de la _PyPi Store_.
Para poder usar estos paquetes, primero tenemos que instalar pip en nuestro sistema.
```
install -> get.pip.py -> guardarlo en el ordenador -> terminal -> ejecutarlo como un directorio normal de python.
Para comprobar que stá instalado: pip -- version
```

### PyPi (_Cheeseshop_)
**`PyPi`** es una base de datos de todos los modulos que puedes importar. Del inglés _Python Package Index_. Dentro, encontramos muchas librerias de terceros. Para importarlas o conectarlas con nuestro programa, debreremos usar pip.

## Comandos

- Instalar un paquete:
```
pip install nombre-del-paquete
```

- Ver paquetes instalados:
```
pip list
```

- Actualizar un paquete:
```
pip install --update nombre-del-paquete
```

- Desinstalar un paquete:
```
pip uninstall nombre-del-paquete
```

## Ejemplo:
```
terminal -> pip install numpy
```
> Esto instalará la biblioteca `numpy`, usada para procesar numeros, records y objetos. Luego abrá que abrir python3 e importarlo.
```
phython3
import numpy
```
