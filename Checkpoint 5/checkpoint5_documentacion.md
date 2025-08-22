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

# ARGUMENTOS EN PYTHON
## ¿Qué es un argumento en Python?
Los **argumentos** son valores que enviamos a una función para que los utilice internamente. Es decir, un **argumento** es el valor (dato) que le pasas a una función cuando la llamas.  
El **parámetro** es el nombre que aparece en la definición de la función.  

### Ejemplo
```python
def saluda(nombre):      # `nombre` es un parámetro
    print("Hola", nombre)

saluda("Ane")           # "Ane" es un argumento
```

## Forma en la que Python pasa los argumentos

-   Python **no** usa “paso por valor” o “paso por referencia” exactamente como otros lenguajes; usa **paso por objeto-por-referencia** (a veces llamado _pass-by-assignment_):
    
    -   La **referencia** al objeto se pasa a la función.
        
    -   Si el objeto es **mutable** (lista, dict, objeto), la función puede modificarlo en sitio.
        
    -   Si el objeto es **inmutable** (int, str, tuple), la función no puede cambiar el objeto original — reasignaciones crean nuevos objetos.

## Tipos de argumentos
Python permite varias formas de pasar argumentos. Cada una resuelve necesidades distintas:
1.  **Posicionales** : el orden importa, se pasan en orden.
2.  **Nombrados (keyword arguments)**: se pasan con nombre  `clave=valor`, el orden no importa.
3.  **Con valor por defecto (default arguments)**: tienen un valor si no se indica otro, parámetros opcionales con valor por defecto.
4.  **Arbitrarios posicionales (`*args`)** — aceptar N argumentos posicionales.
5.  **Arbitrarios con nombre (`**kwargs`)** — aceptar N argumentos nombrados.
6.  **Keyword-only** — parámetros que sólo pueden recibirse por nombre (forzados por `*`).
7.  **Positional-only** — parámetros que sólo pueden recibirse por posición (señalados con `/`, Python ≥3.8).

### **Posicionales** 
```python
def suma(a, b):
    return a + b

print(suma(2, 3))  # 5  (2 → a, 3 → b)
```
    -   Si cambias el orden `suma(3, 2)` obtendrás `5` también, pero con roles invertidos.
   
### **Nombrados (keyword arguments)** 
````python
def presentarse(nombre, edad):
    print(f"{nombre} tiene {edad} años")

presentarse(edad=27, nombre="Ane")  # orden no importa
````
    
### **Con valor por defecto (default arguments)** 
``` python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}")

saludar("Ane")              # usa "Hola"
saludar("Ane", saludo="¡Hey")  # usa "¡Hey"
```

### **Arbitrarios posicionales (`*args`)** 
-   `args` es una tupla dentro de la función.
````python
def suma_todos(*args):
    return sum(args)

print(suma_todos(1, 2, 3, 4))  # 10
````    
### **Arbitrarios con nombre (`**kwargs`)** 
-   `kwargs` es un diccionario `{clave: valor}`.
``` python
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(clave, "=", valor)

mostrar_info(nombre="Ane", ciudad="Lima")
```
    
### **Keyword-only** 
-   El `*` en la firma hace que los parámetros a la derecha sean **keyword-only**.
``` python
def ejemplo(a, b, *, opcional=0):
    return a + b + opcional

ejemplo(1, 2, opcional=3)  # correcto
# ejemplo(1, 2, 3)         # ERROR: opcional debe ir por nombre
```    
### **Positional-only**
-   El `/` indica que todo a su izquierda solo puede pasarse por posición.
``` python
def dividir(x, y, /, precision=2):
    return round(x / y, precision)

dividir(10, 3)         # correcto
# dividir(x=10, y=3)  # ERROR: x e y son positional-only
```
## Cheat sheet 
``` python
# Posicional
f(1, 2)

# Nombrado
f(x=1, y=2)

# Default
def f(x, y=10): ...

# *args
def f(*args): print(args)   # args es tupla

# **kwargs
def f(**kwargs): print(kwargs)  # kwargs es dict

# Forzar keyword-only
def f(a, *, b=2): ...

# Positional-only (Python 3.8+)
def f(a, b, /, c): ...

# Desempaquetado al llamar
f(*[1,2,3])
f(**{'a':1, 'b':2})
```
## Buenas prácticas

-   Usa nombres de parámetros claros: `def calcular_area(base, altura):` en vez de `def f(a, b):`.
    
-   Prefiere **keyword arguments** en llamadas largas para mejorar legibilidad.
    
-   Evita valores por defecto mutables; usa `None` como sentinel.
    
-   Usa `*` para forzar keyword-only si deseas mayor claridad: `def crear_usuario(nombre, *, activo=True):`.
    
-   Documenta la función con docstring explicando qué argumentos recibe y qué tipo/valores espera.
    
-   Usa `inspect.signature` cuando crees APIs que trabajen con funciones ajenas.


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

**`pip`** es el gestor de paquetes oficial de Python. Te permite instalar bibliotecas externas para apliar las funcionalidades de tu programa. Estos paquetes externos se importan de la _PyPi Store_.
Para poder usar estos paquetes, primero tenemos que instalar pip en nuestro sistema. Es decir, es una herramienta que instala, actualiza y quita **paquetes** (bibliotecas) que se publican en repositorios como **PyPI** (Python Package Index).
    
-   Un **paquete** (o _package_) es una colección distribuible de código Python (módulos, datos, metadatos) que puedes instalar con `pip install nombre-paquete`.
    
-   **Ejemplo práctico:** `python -m pip install requests` descarga e instala la biblioteca `requests` en tu entorno Python.

```python
install -> get.pip.py -> guardarlo en el ordenador -> terminal -> ejecutarlo como un directorio normal de python.
Para comprobar que stá instalado: pip -- version
```
## ¿Por qué existe pip? y ¿Para qué se utiliza?
Cuando programas, casi nunca lo haces **solo**: reutilizas código hecho por otros (por ejemplo, para peticiones HTTP, trabajar con fechas, bases de datos, testing). `pip` facilita:
-   **Instalar** librerías publicadas (desde PyPI, GitHub, directorios locales).
-   **Desinstalar** librerías.
-   **Actualizar** a versiones más nuevas.
-   **Gestionar** dependencias (las librerías que requiere otra librería).
-   Integrarse con **entornos virtuales** (`venv`) para no “ensuciar” la instalación global de Python.

## Conceptos clavee
-   **PyPI**: repositorio central donde se publican la mayoría de paquetes Python.
-   **Paquete / distribución**: unidad que pip instala. Viene como:
    -   **wheel** (`.whl`) — formato binario empaquetado (instalación rápida).
    -   **sdist** (`.tar.gz` o `.zip`) — distribución fuente (puede compilar extensiones).
-   **Entorno virtual**: entorno aislado (ej. creado con `python -m venv venv`) donde instalas tus paquetes sin afectar al sistema.
-   **requirements.txt**: archivo que lista dependencias (y versiones) para replicar entornos.
-   **pyproject.toml / setup.py**: archivos que describen cómo construir/instalar un paquete.


### PyPi (_Cheeseshop_)

**`PyPi`** es una base de datos de todos los modulos que puedes importar. Del inglés _Python Package Index_. Dentro, encontramos muchas librerias de terceros. Para importarlas o conectarlas con nuestro programa, debreremos usar pip.

## Cheat sheet o comandos
``` bash
# Instalar un paquete
python pip install nombre-del-paquete

# Instalar con versión concreta
python pip install "requests==2.28.1"

# Actualizar un paquete
python -m pip install --upgrade requests
pip install --update nombre-del-paquete

# Desinstalar
pip uninstall nombre-del-paquete

# Instalar desde un archivo requirements.txt
python -m pip install -r requirements.txt

# Instalar desde GitHub (branch/tag)
python -m pip install git+https://github.com/usuario/repositorio.git@main

# Instalar local (carpeta con setup.py o pyproject.toml)
python -m pip install ./mi_proyecto

# Descargar paquetes sin instalar
python -m pip download requests

# Mostrar información
python -m pip show requests

# Listar paquetes instalados
python -m pip list

# Borrar cache
python -m pip cache purge
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


## Entornos virtuales

-   Evitan conflictos entre proyectos (cada proyecto tiene sus propias dependencias).
    
-   No necesitas permisos de administrador.
    
-   Facilitan desplegar/compartir proyectos con `requirements.txt`.
``` bash
python3 -m venv venv
source venv/bin/activate        # ahora el prompt cambia (venv)
python -m pip install -r requirements.txt
deactivate                      # salir del entorno
````

> si `pip` no se encuentra, siempre puedes usar `python -m pip` (usa el pip asociado con ese Python).
```bash 
## Instalar desde Git, archivos locales o URLs
# Desde GitHub (instala la rama main)
python -m pip install git+https://github.com/user/repo.git@main

# Desde un archivo wheel local
python -m pip install ./dist/mi_paquete-0.1-py3-none-any.whl

# Desde una URL directa a un .whl o .tar.gz
python -m pip install https://example.com/packages/mi_paquete.whl
```

## Instalaciones editables y desarrollo

`pip install -e .` instala el paquete en modo _editable_. Útil mientras desarrollas: los cambios en tu código se reflejan sin reinstalar.

Necesitas un `setup.py` o `pyproject.toml` bien configurado para que funcione.

## Errores comunes 

-   **`pip: command not found`**  
    Usa `python -m pip ...` o instala pip (la mayoría de Python modernos ya incluyen pip). En sistemas gestionados (macOS/Ubuntu), usa la instalación del sistema o `python -m ensurepip --upgrade`.
    
-   **Permisos denegados al instalar globalmente**  
    No uses `sudo pip install ...` en la mayoría de los casos. Mejor: usa `venv` o `--user`:
    ```bash
    python -m pip install --user paquete
    ```
-   **Compilación fallida (extensiones en C)**  
    Instala dependencias del sistema (por ejemplo, `build-essential`, `python3-dev` en Debian/Ubuntu) o usa una wheel ya construida.
    
-   **Version conflict / dependency resolver**  
    `pip` puede reportar conflictos entre versiones. Solución: fijar versiones, usar `pip-compile` o herramientas de administración de dependencias (Poetry).
    
-   **Cache corrupto / problemas de permisos con la caché de pip**  
    `python -m pip cache purge` o corregir permisos de `~/.cache/pip` con `chown`.


## Buenas prácticas

1.  **Siempre usa entornos virtuales** (`venv` o `virtualenv`).
    
2.  **Nunca uses `sudo pip install`** salvo caso extremo en sistemas gestionados.
    
3.  **Pinnea versiones** en producción (`requirements.txt`).
    
4.  **Usa wheels** cuando estén disponibles para evitar compilaciones largas.
    
5.  **Automatiza** la instalación en CI: `python -m pip install -r requirements.txt`.
    
6.  **Revisa dependencias de sistema** antes de instalar paquetes que compilan extensiones.
    
7.  **Actualiza pip**: `python -m pip install --upgrade pip setuptools wheel`.

## Preguntas frecuentes

**¿Necesito usar pip siempre?**  
Si usas Python, casi seguro necesitarás `pip` para instalar bibliotecas externas. En algunos entornos (conda) se usan otras herramientas, pero pip sigue siendo estándar para PyPI.

**¿Por qué prefiero `python -m pip install` sobre `pip install`?**  
Porque asegura que ejecutas el `pip` asociado con ese intérprete de Python (evita confusión entre múltiples Pythons).

**¿Qué es `pipx`?**  
Herramienta para instalar aplicaciones Python (CLI) globalmente en entornos aislados (ideal para herramientas como `cookiecutter`, `pre-commit`, etc.).
x