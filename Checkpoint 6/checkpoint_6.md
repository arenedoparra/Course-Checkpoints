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

# ¿Es MongoDB una base de datos SQL o NoSQL?

# ¿Qué es una API?

# ¿Qué es Postman?
*Postman* es una herramienta que se utiliza para probar y desarrollar APIs, sin tener que crear una interfaz de usuario. Los desarrolladores pueden enviar solicitudes a una API y ver la respuesta. 
Sirve para enviar **peticiones HTTP (GET, POST, PUT, DELETE)** y ver las respuestas.
Es usado por desarrolladores backend o testers.
> [Postman](https://www.postman.com/) se usa para hacer pruebas y asegurarte de que tu API funciona correctamente.



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

