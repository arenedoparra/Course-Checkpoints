---
description: ¿Qué es la palabra clave "this" en JS?
---

# 👉 'This' Keyword

### Introducción

En JavaScript, la palabra clave **`this`** es una de las más importantes… y también una de las que más confusión genera, incluso en programadores experimentados.\
Se utiliza para **hacer referencia a un objeto específico** dentro de un contexto, pero **su valor puede cambiar dependiendo de dónde y cómo se use**.\
`this` **no siempre significa lo mismo**. Su significado depende del **contexto**.

* Es **una palabra reservada** en JavaScript.
* No se puede cambiar su nombre (no podemos usar `let this = ...`).
* Su valor **se determina en tiempo de ejecución**, no cuando escribimos el código.

### Usos

* Para **cceder a propiedades o métodos** del mismo objeto sin escribir su nombre directamente.
* Hacemos código **reutilizable** en funciones o clases.
* **Programamos en POO (Programación Orientada a Objetos)** para referirnos al objeto actual.

### Ejemplo

```javascript
const persona = {
  nombre: "Ane",
  saludar: function () {
    console.log("Hola, soy " + this.nombre);
  }
};

persona.saludar(); // Resultado: Hola, soy Ane

```

### Contextos de This

El valor de `this` depende de **cómo** y **dónde** se usa.

| En un objeto (método)       | El propio objeto                                          |
| --------------------------- | --------------------------------------------------------- |
| En una función simple       | `undefined` (modo estricto) o `window` (modo no estricto) |
| En una clase                | La instancia creada                                       |
| En un evento HTML           | El elemento HTML que disparó el evento                    |
| Con `bind`, `call`, `apply` | Lo que se le asigne explícitamente                        |

