# CONDICIONALES EN PYTHON

## ¿Qué es un condicional?

Los condicionales son una de las estructuras fundamentales en cualquier lenguaje de programación.  
Se utilizan para **tomar decisiones** dentro de nuestro código.  
En pocas palabras, nos permiten ejecutar un bloque de código **solo si** se cumple una condición específica.

Los **condicionales** son de los elementos fundamentales que hacen python dinámico, hacen que el programa  que crees pueda empezar a tomar decisiones. Estos permiten que nuestro programa tome decisiones y ejecute acciones diferentes según ciertas condiciones. Esta estructura, permite ejecutar un bloque de código u otro dependiendo de si una condición se cumple (True) o no, son tipos de respuestas de SI o NO.
Los condicionales pueden tener direntes niveles, siguiendo una estructura de arbol, donde existen diferentes escenarios y acciones.

 > _Si ocurre X situación, quiero que como programa, quiero que realices X tarea, pero si ocurre Y quiero que realices ortra tarea_

### Componentes básicos

- **Expresión booleana**: algo que Python puede evaluar a `True` (verdadero) o `False` (falso).

- **Palabras clave**: `if`, `elif` (else if), `else`.

- **Bloques indentados**: el código que se ejecuta cuando la condición es verdadera.

- **Dos puntos `:`**: indican el inicio de un bloque.

### Sintaxis
>
> En Python, los bloques se definen **por sangría** (4 espacios es el estándar). No mezcles tabs y espacios.

```python
if condición:
    # Si la condición es verdadera
else:
    # Si ninguna condición anterior se cumple
elif otra_condición:
    # Si la primera condición no se cumple pero esta sí
```

### Diagrama visual ( `if / elif / else`)

```mermaid
    A[Inicio] --> B {¿condición 1?}
    B -- Sí --> C [Ejecutar bloque if]
    B -- No --> D {¿condición 2?}
    D -- Sí --> E [Ejecutar bloque elif]
    D -- No --> F [Ejecutar bloque else]
    C --> G[Fin]
    E --> G
    F --> G
```

### Qué es una **condición**?

Una **condición** es cualquier expresión que Python pueda reducir a `True` o `False`.  

- **Comparaciones**: `x > 10`, `edad == 18`, `precio <= 100`
- **Operadores lógicos**: `x > 0 and y > 0`, `is_admin or is_staff`
- **Pertenencia**: `'py' in 'python'`, `item in lista`
- **Identidad**: `x is None`, `a is b`
- **Verdad implícita (truthiness)**: `if lista:` (True si **no** está vacía)

### Ejemplo

    ``` python
    edad = 30
    if edad < 25:
        print("Lo siento, necesitas tener 25 años")
    else:
        print("Adceptado, tienes{edad} años")
    elif temperatura < 100:
        print("Lo siento {edad} es muy viejo") 
    #Ya que en elif hay dos condiciones, esta deberá ir en medio, porque primero comprobará estas dos y si son falsas ejecutará una tercera.
    ```

### Operadores mas usados de comparación

| Operador | Significado   | Ejemplo  | Resultado |
| -------- | ------------- | -------- | --------- |
| `==`     | Igualdad      | `3 == 3` | `True`    |
| `!=`     | Distinto      | `3 != 4` | `True`    |
| `>`      | Mayor que     | `5 > 2`  | `True`    |
| `<`      | Menor que     | `2 < 5`  | `True`    |
| `>=`     | Mayor o igual | `5 >= 5` | `True`    |
| `<=`     | Menor o igual | `3 <= 2` | `False`   |

### Errores comunes

1. **Confundir `=` con `==`**

    - `=` asigna, `==` compara.

    - En Python **no puedes** usar `=` dentro de una condición.

2. **Usar `is` en lugar de `==` para valores**

    ```python
    a = 500
    b = 500
    print(a == b)  # True (mismo valor)
    print(a is b)  # False en general (objetos distintos)
    ```

3. **Olvidar el `:`** al final de `if/elif/else`.

4. **Mala indentación** (mezclar tabs/espacios).
    - Configura tu editor a **4 espacios**.

5. **Comparar floats con `==`** → usa `math.isclose`.

6. **Usar `and`/`or` con bits (`&`, `|`)** por error.

    - Para lógica, usa `and`, `or`, `not`.

7. **Escribir `if x == True:`**

    - Prefiere `if x:` o `if not x:`.

8. **No considerar el orden de `elif`**

    - Pon primero las condiciones **más restrictivas** o **más probables**.

### Cheat sheet

- `if / elif / else` decisiones con múltiples casos.
- Usa **4 espacios** para indentación.
- `and` / `or` / `not` lógica booleana.
- `in` / `not in` pertenencia en cadenas, listas, etc.
- `is` / `is not` identidad de objetos (usa `is None`).
- `0 < x < 10` comparaciones encadenadas.
- Ternario: `x if cond else y`.
- Flotantes: `math.isclose(a, b)`

### Buenas prácticas

- Mantén las condiciones **cortas y legibles**.
- Extrae condiciones complicadas a funciones con nombres claros:
- Prefiere **guard clauses** a grandes estructuras anidadas.
- Ordena `elif` de lo **más específico** a lo **más general**.
- Escribe **tests** para condiciones críticas.

# BUCLES EN PYTHON (_LOOPS_)

## ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

Un **bucle** es una estructura de control que permite **ejecutar repetidamente** un bloque de código mientras se cumpla una condición o hasta agotar una secuencia. Los bucles son esenciales cuando queremos:

- Procesar todos los elementos de una lista, archivo o colección.
- Repetir una acción hasta que ocurra cierta condición (ej.: reintentos de conexión).
- Generar estructuras (tablas, matrices) o hacer cálculos acumulativos (sumas, promedios).
- Automatizar tareas repetitivas (renombrar archivos, enviar correos, validar datos).

**Ejemplo:** queremos imprimir los números del 1 al 5 sin escribir 5 `print` separados. Un bucle nos permite hacerlo con unas pocas líneas.
Resumiendo, Los **bucles** son herramientas de codigo que nos permiten repetir instrucciones multiples veces sin tener que escribir el mismo codigo.
 Hay dos tipos de _loops_ en python:

- For...In
- While

Ambos se pueden usar para iterar colecciones, un rango de numeros, listas etc. Ambos bucles son útiles para automatizar tareas como recorrer listas, repetir cálculos, etc.

### Tipos de bucles

#### 1) `for...in` — el bucle más usado

`for` itera sobre _iterables_ (listas, tuplas, strings, diccionarios, rangos, archivos, generadores, etc.). Es el estándar para recorrer colecciones. Por ejemplo; si tenemos una máquina con bolas de juguete dentro, este tipo de bucle, sería la capacidad de darle vueltas a la rueda, tantas veces como bolas de juguete haya. Tenemos un principio y un final bien definidos.

**Sintaxis**

   ```python
for elemento in iterable:
    # hacer algo con elemento
```

**Ejemplo**

```python

# recorrer lista
nombres = ["Ana", "Luis", "María"]
for nombre in nombres:
    print(nombre)
# recorrer string
for letra in "Python":
    print(letra)
# usar range para contar
for num in range(6):
    print(num)
```

#### 2) `while` — repetir mientras una condición sea verdadera

Repite una acción **mientras** se cumpla una condición. No es tan inteligente como el for..in loop. este, continuará ejecutandose cuando llega al final hasta entrar en un bucle infinito si no se configura correctamente. Es por ello que a un _While_ loop hay que decirle cuando parar y a esto se le llama _centinel value_. `while` repite un bloque **mientras** la condición sea `True`. Útil cuando no sabes de antemano cuántas veces repetirás (ej.: espera por un evento).

**Sintaxis**

```python
while condicion:
    # cuerpo
```

**Ejemplo**

```python
nums=list(range(1,100))
 while len(nums) > 0:  
    print(nums.pop())
```

> **Cuidaso:** `while` puede producir **bucles infinitos** si la condición nunca se hace `False`.

#### 3) Bucles anidados (nested loops)

Un bucle dentro de otro. Útil para matrices, combinaciones, tablas de multiplicar.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
```

**Cuidado con lacomplejidad** ya que anidar mucho puede crecer la cantidad de operaciones.

### Errores comunes

1. **Bucle infinito (`while True` sin `break`):**

    - Siempre asegúrate de que la condición pueda volverse `False` o hay un `break`.

2. **Modificar lista mientras la iteras:**

   ```python
   lista = [1,2,3,4]
for x in lista:
    if x % 2 == 0:
        lista.remove(x)  # peligroso: puede saltarse elementos
```

    -   **Solución:** itera sobre una copia (`for x in lista[:]`) o construye una nueva lista (comprensión).
        
3.  **Off-by-one (rango incorrecto):**

    -   `range(1, 6)` incluye 1..5; recuerda que `stop` es exclusivo.
        
4.  **Dependencia del valor de la variable de bucle fuera del bucle:**

    -   En Python la variable del bucle queda definida después del bucle (a diferencia de otros lenguajes), cuidado con reusar nombres.
        
5.  **Usar `is` para comparar valores (en vez de `==`):**

    -   `is` comprueba identidad de objeto, no igualdad de valor. Para comparar números o strings usa `==`.
        
6.  **Confundir `for-else`:**

    -   `else` se ejecuta solo si no hubo `break`. Esto puede confundir a quien lea tu código; documenta o evita si no añade claridad.

# LISTAS DE COMPRENSION

## ¿Qué es una lista por comprensión en Python?

Una **lista por comprensión** (list comprehension) es una forma concisa y expresiva de crear una lista a partir de otra secuencia (lista, rango, string, etc.) aplicando una expresión y opcionalmente un filtro.

Una **lista por comprensión** es una forma rápida de construir nuevas listas aplicando operaciones o condiciones sobre un iterable. Se pueden configurar una serie de for..in loops para funcionar en unsa sola linea y generar listas a partir de esas lineas de codigo, es un set de bubles.

**Ejemplo**

```python
# transformar cada x en x*2, para x en lista_original, si x es par
[x * 2 for x in lista_original if x % 2 == 0] 
```

**Sintaxis**

```python
[nueva_expresión for elemento in iterable if condición]
```

**Ejemplo**

```python
cuadrados = [x**2 for x in range(10)]
#Resultado: `[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`
```

```python
#También puedes incluir condiciones
pares = [x for x in range(10) if x % 2 == 0]

# Resultado: `[0, 2, 4, 6, 8]`

```
### ¿Por qué usarla? Ventajas frente a `for` tradicional
- **Sintaxis más compacta**: una sola línea expresa la idea de transformar y filtrar.
- **Lectura declarativa**: describe _qué_ quieres (map + filter), no _cómo_ (búcle, append).
- **A menudo más rápida** que el `for` con `append` porque está optimizada en C (en CPython).
- **Menos líneas de código** → menos posibilidad de errores simples (olvidar `append`, etc.)

### Cuándo **no** usar comprehensions (anti-patrones)

- **Cuando la lógica es compleja** (varias condiciones, operaciones con side-effects): una función con bucles y nombres descriptivos puuede ser más legible.
- **Comprehensions anidadas muy profundas** (más de 2 niveles) reducen la legibilidad.
- **Cuando necesitas depurar paso a paso**: bucles `for` permiten `print`/breakpoints más fáciles.
- **Cuando necesitas reutilizar parcial de la lista generada**: a vecrs separar en pasos mejora claridad.

**Regla práctica** si una comprensión no cabe cómodamente en una línea o te obliga a usar expresiones intrincadas, reescribe con `for`/funciones auxiliares.

### Buenas prácticas

- Prefiere comprehensions para transformaciones simples (map + filter).
- Si la comprensión tiene más de **dos cláusulas `for`** o un `if-else` complejo, reconsidera.
- No uses comprehensions solo por hacer `append` con side effects.
- Para grandes cantidades de datos, considera expresiones generadoras y funciones como `sum`, `any`, `all`.
- Documenta con un comentario si la comprensión hace algo no obvio.

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

# FUNCIONES LAMBDA

## ¿Qué es una función Lambda en Python?

Es una herramienta que nos permite empaquetar una función en general una funcion más pequeña y luego introducirla en otras funciones. Con ella, podemos unir un comportamiento, un proceso. SOn muy similares a una variable, moviles y faciles de usar.

    Una **lambda** nos permite empaquetar rápida y facilmente una funcionalidad, almacenarla en una variable y luego, inrtoducir ese valor, ese preceso, en otras funcioenes y en otras partes del programa. Es una forma rápida de definir funciones pequeñas en una sola línea.

## Sintaxis

```python
lambda argumentos: expresión
```

## Ejemplo

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

## Ejemplo

```
terminal -> pip install numpy
```

> Esto instalará la biblioteca `numpy`, usada para procesar numeros, records y objetos. Luego abrá que abrir python3 e importarlo.

```
phython3
import numpy
```
