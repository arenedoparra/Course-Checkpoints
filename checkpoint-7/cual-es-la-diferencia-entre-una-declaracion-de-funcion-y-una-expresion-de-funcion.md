---
description: >-
  ¿Cuál es la diferencia entre una declaración de función y una expresión de
  función?
---

# 🆚 Declaración de función Vs Expresión de función

### Introducción

En JavaScript, **las funciones** son uno de los elementos más importantes y utilizados.\
Nos permiten **reutilizar código**, **organizarlo mejor** y **realizar tareas específicas** sin tener que repetir las mismas líneas una y otra vez.

Pero no todas las funciones se escriben de la misma forma. Existen varias maneras de crearlas, y dos de las más comunes son:

1. **Declaración de función** (`Function Declaration`)
2. **Expresión de función** (`Function Expression`)

Aunque ambas nos permiten **crear funciones**, tienen **diferencias importantes** que afectan a cómo y cuándo se pueden usar.

***

### &#x20;1. Declaración de Función (Function Declaration)

Una **declaración de función** es la forma más tradicional y directa de crear una función en JavaScript.\
Se utiliza la palabra clave `function` seguida del **nombre** de la función y los paréntesis `()` que pueden contener parámetros.

**Características principales:**

* Tiene **nombre obligatorio**.
* Se carga en memoria **antes** de que el código se ejecute (gracias al **hoisting**).
* Se puede llamar **antes o después** de ser definida en el código.

#### Sintaxis

```javascript
function nombreDeLaFuncion(parámetros) {
// Bloque de código que se ejecuta cuando llamamos a la función
}
```

### 2. Expresión de Función (Function Expression)

En una **expresión de función**, la función se crea y **se asigna a una variable**. Aquí, **la función no existe** hasta que la línea de código donde se crea es ejecutada.

**Características principales:**

* Puede ser **anónima** (sin nombre) o con nombre opcional.
* **No** se carga antes de que el código se ejecute (no hay hoisting para su valor).
* **Debe definirse antes de ser usada**.

#### Sintaxis

```javascript
const nombreDeLaFuncion = function(parámetros) {
  // Código que se ejecuta cuando se llama a la función
};
```

### Comparativa

| Característica              | Declaración de Función | Expresión de Función |
| --------------------------- | ---------------------- | -------------------- |
| **Nombre**                  | Obligatorio            | Opcional             |
| **Hoisting**                | Sí                     | No                   |
| **Uso antes de definirla**  | Sí                     | No                   |
| **Se guarda en**            | Memoria de funciones   | Variable             |
| **Función anónima posible** | No                     | Sí                   |

### Cuándo usar cada una

* Usa **declaración de función** cuando:
  * Quieras que esté disponible en cualquier parte del archivo.
  * Sea una función clave del programa.
* Usa **expresión de función** cuando:
  * Necesites pasar funciones como datos (callbacks).
  * Quieras controlar **cuándo** y **dónde** existe.
  * Prefieras usar **arrow functions**.
