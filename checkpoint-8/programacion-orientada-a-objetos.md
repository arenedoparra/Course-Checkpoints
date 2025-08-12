---
description: ¿Qué es la programación orientada a objetos?
---

# Programación orientada a objetos

### Introducción

La **Programación Orientada a Objetos (POO)** es un **paradigma de programación** que organiza el código en torno a **objetos.** En inglés se conoce como **Object Oriented Programming (OOP)**. Un paradigma es **una forma de pensar y organizar el código**. La \*\*POO\*\* se basa en **crear y organizar el código usando “objetos”** que representan **cosas del mundo real o conceptos abstractos**. Un **objeto** es como una “caja” que agrupa **datos** (también llamados **atributos** o **propiedades**) y **funcionalidades** (también llamadas **métodos**). En lugar de escribir código suelto, en POO agrupamos todo lo relacionado en **estructuras lógicas** que imitan objetos del mundo real.

**Ejemplo**:\
Por ejemplo si quieres programar un catalogo donde hay coches. En vez de escribir una lista larga de variables para cada coche, **creas un objeto “Coche”** que tenga:

* **Propiedades (atributos)**: color, marca, modelo...
* **Acciones (métodos)**: arrancar(), frenar(), acelerar()...

En POO, ese “coche” sería un **objeto** dentro de nuestro programa. Cada coche que aparezca en el catalogo será **una copia (instancia)** del objeto “Coche”.

***

### Usos

**Ayuda a pensar como en la vida real**. Cuando organizas tu código en **objetos**, tienes las siguientes ventajas:

* **Organizar mejor el código**: el código está más estructurado ya que está agrupado en estructuras.
* **Reutilizar el codigo**: se puede crear una clase y reutilizarla en muchos proyectos. Es como una 'plantilla'.
* **Mantenimiento más fácil**: si necesitas cambiar algo, solo lo cambias en un lugar y afecta a todos los objetos
* **Escalabilidad a proyectos mas grandes**: ideal para proyectos grandes con muchos elementos y muchas lineas de codigo y equipos grandes.
* **Semejanza con el mundo real:** Es más fácil entender este codigo porque se parece a lo que conocemos del mundo real.

| Ventajas                          | Desventajas                                           |
| --------------------------------- | ----------------------------------------------------- |
| Código más organizado.            | Puede ser más difícil de entender para principiantes. |
| Reutilización de código.          | Puede añadir algo de complejidad extra.               |
| Facilita el mantenimiento.        | Un mal diseño en POO puede ser difícil de corregir.   |
| Escalable para proyectos grandes. | No siempre es necesaria para programas muy pequeños.  |

La POO se usa en **casi cualquier aplicación**  de hoy en día como:

* Desarrollo de videojuegos&#x20;
* Aplicaciones web y móviles&#x20;
* Sistemas bancarios&#x20;
* Inteligencia Artificial&#x20;

***

### Sintaxis

```javascript
// Definir una clase
class Persona {
  constructor(nombre, edad) {
    this.nombre = nombre;
    this.edad = edad;
  }

  saludar() {
    console.log(`Hola, me llamo ${this.nombre} y tengo ${this.edad} años`);
  }
}

// Crear un objeto (instancia)
const persona1 = new Persona("Ana", 25);
const persona2 = new Persona("Luis", 30);

// Usar métodos
persona1.saludar(); // Hola, me llamo Ana y tengo 25 años
persona2.saludar(); // Hola, me llamo Luis y tengo 30 años
```

***

### Conceptos clave de la POO

#### 1. Clase

Una **clase** es como un plano o plantilla para crear objetos. Define **qué propiedades y métodos** tendrán esos objetos.

**Ejemplo**

```javascript
class Coche {
  constructor(marca, color) {
    this.marca = marca; // Propiedad
    this.color = color; // Propiedad
  }

  acelerar() { // Método
    console.log("El coche está frenando");
  }
}
```

#### 2. Objeto

Un **objeto** es **una instancia** de una clase, es decir, algo creado a partir de ese plano.

**Ejemplo**

```javascript
const miCoche = new Coche("Toyota", "Rojo");
miCoche.acelerar(); // El coche está acelerando
```

#### 3. Atributos y Métodos

* **Atributos** → variables dentro de un objeto (ej. `marca`, `color`).
* **Métodos** → funciones dentro de un objeto (ej. `acelerar()`, `frenar()`).

#### 4. Principios o elemntos de la POO&#x20;

La POO tiene 4 principios fundamentales:

| Principio         | Descripción                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| **Encapsulación** | Agrupar datos y métodos dentro de un objeto, ocultando los detalles internos que no es necesario. |
| **Abstracción**   | Simplificar algo complejo mostrando solo lo importante.                                           |
| **Herencia**      | Crear nuevas clases basadas en otras existentes.                                                  |
| **Polimorfismo**  | Un mismo método puede comportarse de forma distinta según el contexto.                            |
