# ¿Para qué usamos Clases en Python?

Las **clases** en Python son la base de la **Programación Orientada a Objetos (POO)**. Nos permiten **organizar el código**, agrupar datos (atributos) y comportamientos (métodos) en una sola estructura.

### ¿Por qué son útiles las clases en Pyhon?
- Para la reutilización de código.
- Para crear múltiples objetos a partir de una sola definición.
- Para organizar proyectos grandes.

### **Ejemplo**

```
¡df
```



# ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

# ¿Cuáles son los tres verbos de API?
**Los verbos HTTP** (también conocidos como **métodos HTTP**) son acciones que nos dicen qué tipo de operación es la que queremos hacer sobre un dato o una colección de datos.

Los verbos de API están relacionados con las operaciones **CRUD** (Create, Read, Update, Delete)

Los **tres verbos más comunes** cuando se trabja con APIs son:
- GET
- POST
- DELETE
> También existen otros verbos como PUT y PATCH, que se usan para actualizar información.

## GET
**GET** se utiliza para **obtener datos** de un servidor. Se usa cuando quieres **leer** o **consultar** información de una base de datos a través de una API. Esta petición no modifica nada, solo nos permite leer los datos.

## POST
**POST** se utiliza para enviar datos al servidor y que este cree algo nuevo, por ejemplo un nuevo usuario. Se utiliza cuando quieres crear un nuevo recurso, en general por ejemplo se utiliza cuanod envias datos al rellenar un formulario.

## DELETE
**DELETE** sirve para borrar un recurso en el servidor. Por ejemplo si tienes que borrar un usuuario o un producto de una aplicación de Eccomerce.

### Esquema
```
APP / WEB      
       |
       |-----> [GET] ------> Obtener datos (Read)
       |
       |-----> [POST] -----> Enviar nuevos datos (Create)
       |
       |-----> [DELETE] ---> Eliminar datos (Delete)
       |
       V
    API / SERVIDOR
```

# ¿Es MongoDB una base de datos SQL o NoSQL?
## Introducción
**MongoDB** es una base de datos NoSQL. Es una base de datos de este tipo porque no utiliza el lenguaje SQL y tampoco guarda los datos en tablas como lo harían bases de datos relacionales, como MySQL. 

En vez de tablas, columnas y filas, utiliza colecciones y documentos para almacenar los datos en un formato parecido al **JSON**.
Cada documento puede tener una estructura diferente, esto lo hace flexible, especialmente en proyectos donde los datos no siempre tiene una estructura fija.


## Bases de datos
Una base de datos es una forma para **guardar, organizar y gestionar cualquier tipo de datos**. Esta información pueden ser usuarios, productos, mensajes, notas de alumnos...

Existen **dos tipos** de bases de datos, **SQL** y **NoSQL**

| Tipo         | Ejemplos                  | Estructura        | Lenguaje   |
|--------------|---------------------------|-------------------|------------|
| SQL (Relacional) | MySQL | Tablas y filas    | SQL        |
| NoSQL (No Relacional) | MongoDB | Documentos, pares clave-valor | Propio (no SQL) |

## SQL Vs NoSQL
| **SQL** (Bases de datos relacionales) | **NoSQL** (Bases de datos no relacionales) |
|--------------------------------------|--------------------------------------------|
| Usa lenguaje SQL para consultar datos | No usa SQL, puede usar otros métodos como consultas con JSON |
| Tiene una estructura de tablas, filas y columnas | Estructura flexible, documentos, colecciones, pares clave-valor |
| Para datos estructurados y relaciones complejas | Para datos semi-estructurados o no estructurados. |
| Requiere definir un esquema antes de insertar datos | No necesita un esquema fijo (puede cambiar entre documentos) |
| Ejemplo: MySQL | Ejemplo: MongoDB |

## Ventajas de MongoDB
- Si estas desarrollando una app donde la estructura de los datos puede cambiar con el tiempo.
- Necesitas almacenar grandes volúmenes de datos rapido.
- Trabajas con datos que se parecen a JSON.

## Ejemplo
```

      SQL                                   NoSQL 
+-------------------------+    +--------------------------------+
| Tabla: usuarios         |    | Colección: usuarios            |
|-------------------------|    |--------------------------------|
| id | nombre | edad      |    | { nombre: "Ander", edad: 21 }  |
|-------------------------|    | { nombre: "Ane", edad: 27 }    |
| 1  | Ander | 21         |    +--------------------------------+
| 2  | Ane   | 27         |    
+-------------------------+    
```




# ¿Qué es una API?
## Introducción
La palabra **API** significa **Application Programming Interface** (Interfaz de Programación de Aplicaciones). Es un **puente de comunicación** entre dos programas o sistemas.

Una **API** es un servicio, algo así como un sitio web o servidor con el que puedes comunicarte pero en vez de devolverte una página web te devuelve datos. Resumiendo, es un conjunto de reglas y datos que permiten que dos sitemas se comuniquen entre sí.

Las APIs son fundamentales en el desarrollo moderno de software porque permiten crear aplicaciones más rápidas y escalables.

Algunas APIs requieren autenticación, esto evita que cualquier persona haga peticiones sin control y obetenga datos reservados o de contenido sensible.

## Usos de las APIs
-  **Conectar las aplicaciones** con otras aplicaciones o servicios.
- **Obtener datos** desde un servidor (usuarios, productos, videos, imagenes...).
- **Enviar datos** al servidor (formularios...).
- **Automatizar tareas** entre diferentes plataformas (redes sociales, plataformas de pagos...).
- **Crear sistemas complejos** sin tener que desarrollar todo desde cero, simplemente concectandolos.

## HTTP en una API 
Cuando usas una API, Puedes hacer diferentes tipos de **solicitudes HTTP** con los siguientes verbos:


| HTTP | Función               | Ejemplo (Con un usuario)                                     |
|------------|--------------------------------|----------------------------------------------|
| `GET`      | **Obtener** datos                  | Obtener la lista de usuarios                 |
| `POST`     | **Enviar** datos nuevos            | Crear un nuevo usuario                       |
| `PUT`      | **Actualizar** datos     | Modificar información de un usuario          |
| `DELETE`   | **Eliminar** datos                 | Eliminar un usuario de la base de datos      |

## API y datos JSON
Muchas APIs devuelven los datos en formato JSON (JavaScript Object Notation).
### Ejemplo
```
{
  "nombre": "Ane",

  "email": "ane@example.com",

  "activo": true
}
```
## Esquema
```
+-------------------+          +------------------------+
|    Aplicación     | <------> |       API              |
|                   |          |                        |
+-------------------+          +------------------------+
                                        |
                                        v
                               +-----------------------+
                               |    Base de datos      |
                               |                       |
                               +-----------------------+
```


# ¿Qué es Postman?
## Introducción
[**Postman**](https://www.postman.com/) es una **herramienta de desarrollo** muy útil que se utiliza para  **probar, crear, documentar y compartir APIs** de una forma rápida y visual, **sin tener que escribir código o crear una interfaz de usuario** para construir una interfaz o una aplicación desde cero.
Postman te permite enviar solicitudes a un servidor, **peticiones HTTP (GET, POST, PUT, DELETE)** y ver la respuesta sin tener que programar una interfaz. 


Es muy utilizada por:
- Desarrolladores Backend
- Desarrolladores Full Stack
- Testers
- Equipos de QA (Quality Assurance)

## Entender una API

Antes de entender para qué sirve Postman, es importante saber qué es una API, ya que esta aplicación te permite comunicarte con APIs externas.

Una **API** (Aplication Programming Interface) es un servicio, algo así como un sitio web o servidor con el que puedes comunicarte pero en vez de devolverte una página web te devuelve datos. Resumiendo, es un conjunto de reglas y datos que permiten que dos sitemas se comuniquen entre sí.

### **Ejemplo**
Cuando utilizas la aplicación del tiempo, esta estará haciendo una **petición a una API del tiempo** que devolverá datos como la temperatura, las precipitaciones, la humedas, etc.

> Puedes hacer una solicitud **GET** a una API del tiempo y *Postman* te devolverá los datos del tiempo sin tener que escribir código.

## Usos de Postman
**Postman** sirve para:
- Probar si una API funciona correctamente y si los datos llegan correctamente.
- Hacer solicitudes a un servidor (como si fueras un navegador, pero de forma controlada).
- Ver las respuestas que te devuelve la API: datos, errores, estados, etc. Es recomendable para priincipiantes ya que permite ver los errores que devuelve una API y aprender a corregirlos.
- Automatizar pruebas.
- Simular peticiones y hacer pruebas sin tener que programar toda una aplicación completa.


## ¿Por qué usar Postman?
- **Facilita el trabajo en equipo**: puedes compartir colecciones de peticiones con tu equipo.
- **Ahorra tiempo**: no necesitas crear una aplicacion desde cero para hacer pruebas.
- **Es multiplataforma**: funciona en Windows, macOS y Linux.
- **No requiere conocimientos avanzados**: su interfaz es amigable para principiantes. Puedes aprender a manejar peticiones y respuestas HTTP sin necesidad de saber Frontend al completo.

> Colecciones: En Postman puedes guardar tus peticiones en carpetas llamadas colecciones. Esto te permite organizarlas por proyectos o funcionalidades, y compartirlas con otros compañeros de equipo.

## Que puedes hacer con Postman

Puedes hacer diferentes tipos de **solicitudes HTTP** a una API.

| HTTP | Función               | Ejemplo (Con un usuario)                                     |
|------------|--------------------------------|----------------------------------------------|
| `GET`      | **Obtener** datos                  | Obtener la lista de usuarios                 |
| `POST`     | **Enviar** datos nuevos            | Crear un nuevo usuario                       |
| `PUT`      | **Actualizar** datos     | Modificar información de un usuario          |
| `DELETE`   | **Eliminar** datos                 | Eliminar un usuario de la base de datos      |

### Estructura básica de una solicitud en Posman
1. Selecciona el método que vayas a usar: HTTP: GET, POST...
2. Introduce la URL del endpoint.
3. Haz clic en "Send".
4. Observa la respuesta que devuelve el servidor.

 
> *Necesitarás crear una cuenta en Postman para poder usarla y algunas funcionalidades más avanzadas no están dispinibles en la versión gratuita.



# ¿Qué es el polimorfismo?

# ¿Qué es un método dunder?
## Introducción
Un método **dunder** se refiere a la abreviatura del ingles **Double Underscore** (Doble guión bajo) es un método que empieza y termina con dos guiones bajos. Se usa para describir estos métodos que **permiten definir comportamientos personalizados para objetos y clases** en Python.

> Por ejemplo: `__init__`, `__str__`, `__len__`, `__add__`

Python es un lenguaje orientado a objetos con el que puedes **sobrescribir comportamientos internos del lenguaje** de manera flexible.  

- Personalizar cómo se comporta un objeto con los operadores (`+`, `==`, `>`, etc.)
- Controlar cómo se representa un objeto (`print`)
- Administrar cómo se crean e inicializan los objetos (`__init__`, `__new__`)
- Interactuar con funciones y construcciones de Python (`len()`, `iter()`, `next()`)

## Métodos dunder más comunes
| Método         | Propósito                                                | Ejemplo            |
| -------------- | -------------------------------------------------------- | ------------------ |
| `__init__`     | Constructor: inicializa un objeto                        | `obj = Clase()`    |
| `__str__`      | Representación legible para humanos                      | `print(obj)`       |
| `__repr__`     | Representación para desarrolladores                      | `repr(obj)`        |
| `__len__`      | Longitud de un objeto personalizado                      | `len(obj)`   




# ¿Qué es un decorador de python?
Un **decorador** es una forma de modificar el comportamiento de una función sin cambiar su código original. Es una función que toma otra función como argumento, le añade alguna funcionalidad extra y luego la devuelve. Los decoradores pueden ser utiles si tienes muchas funciones en tu codigo y quieres que realicen alguna accion extra como imprimir un mensaje. En lugar de ceditar cada funcion por individual manual, utilizando los decoradores, aplicas el comportmainto de forma limpia, ordemada y reutilizable.
> Se usa el símbolo **@** antes del nombre de la función para hacer el codigo más limpio.

 ````python
@decorator
def saludar():
    print("¡Hola!")
````

 ````python
def decorador(funcion_original):
   def nueva_funcion():
        print("Antes de ejecutar la función original")
        funcion_original()
        print("Después de ejecutar la función original")
    return nueva_funcion
````

## Conceptos para comprender los decoradores
En Python, las **funciones** pueden:
- Ser asignadas a variables
- Ser pasadas como argumento a otras funciones
- Ser devueltas por otras funciones
### Ejemplo:

```python
def saludar():
    return "¡Hola!"

mi_funcion = saludar  
print(mi_funcion()) 
```
```scss
Función original  --->  Decorador  --->  Función decorada
     f()                  @decorador        decorador(f)
```

