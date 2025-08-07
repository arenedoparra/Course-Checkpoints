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
los

# ¿Es MongoDB una base de datos SQL o NoSQL?

# ¿Qué es una API?

# ¿Qué es Postman?
## Concepto general

[**Postman**](https://www.postman.com/) es una **herramienta de desarrollo** muy útil que se utiliza para proibar, trabahr

que permite **probar, crear, documentar y compartir APIs** de una forma rápida y visual, **sin tener que escribir código o crear una interfaz de usuario** para construir una interfaz o una aplicación desde cero.
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
Un método dunder se refiere a Double UNDERSCORE es un método que empieza y termina con dos guiones bajos.

# ¿Qué es un decorador de python?
Un **decorador** es una forma de modificar el comportamiento de una función sin cambiar su código original. Es una función que toma otra función como argumento, le añade alguna funcionalidad extra y luego la devuelve. 
> Se usa el símbolo **@** antes del nombre de la función


### **Ejemplo** 
````
def decorador(funcion):
    def nueva_funcion():
        print("Antes de ejecutar la función")
        funcion()
        print("Después de ejecutar la función")
    return nueva_funcion

@decorador
def saludo():
    print("Hola Mundo!")

saludo()
# Resultado:
# Antes de ejecutar la función
# Hola Mundo!
# Después de ejecutar la función
`````

