---
description: ¿Qué es una función de flecha?
---

# 🏹 Arrow function (función de flecha)

### Introducción

En JavaScript, una **función de flecha** (_arrow function_) es una forma **más corta y moderna** de escribir funciones. Son una **alternativa** a las funciones tradicionales para hacer el código más limpio y fácil de leer, especialmente cuando la función es **pequeña.**

{% hint style="success" %}
Si ves una función muy corta que solo devuelve un valor, es mejor escribirla como **función de flecha** para que el código sea más limpio.
{% endhint %}

Reciben ese nombre porque usan el símbolo **`=>`** (flecha) en su sintaxis.

Resumiendo, es una **nueva sintaxis** para definir funciones que:

* ✅ Son **más compactas**.
* ✅ No tienen su propio valor de `this` (heredan el de su contexto).
* ✅ Son muy útiles en programación funcional y en código que debe ser conciso.

{% hint style="danger" %}
### Cuidados al Usarlas

* No usar si necesitas un `this` propio (por ejemplo, en objetos con métodos que usan `this`).
* No sirven como constructores (`new`).
* Si necesitas acceder a `arguments`, usa una función normal.
{% endhint %}

***

### Usos

1. **Simplificar código**\
   Cuando el cuerpo de la función es corto, se puede reducir mucho la escritura.
2. **Callbacks**\
   Son muy útiles como funciones que se pasan como argumentos a otras funciones.
3. **Programación funcional**\
   Especialmente en métodos como `.map()`, `.filter()`, `.reduce()`.

#### Ejemplo

Ejemplo con `.map()`:

```javascript
const numeros = [1, 2, 3, 4];
const cuadrados = numeros.map(n => n * n);
console.log(cuadrados); // [1, 4, 9, 16]
```

***

### Sintaxis

Las funciones de flecha tienen esta estructura:

```javascript
const nombreFuncion = (parametros) => {
    // Cuerpo de la función
    return resultado;
};
```

#### Partes

* `const nombreFuncion` → asigna la función a una variable constante.
* `(parametros)` → lista de parámetros de entrada.
* `=>` → símbolo de flecha que sustituye la palabra clave `function`.
* `{ ... }` → bloque de código de la función.
* `return` → indica lo que la función devuelve.

***

### Diferencias con las Funciones Tradicionales

| Característica  | Función Tradicional                | Función de Flecha                    |
| --------------- | ---------------------------------- | ------------------------------------ |
| **Sintaxis**    | Más larga (`function nombre() {}`) | Más corta (`() => {}`)               |
| **`this`**      | Crea su propio `this`              | No crea su propio `this` (lo hereda) |
| **Constructor** | Puede usarse con `new`             | ❌ No puede usarse con `new`          |
| **`arguments`** | Tiene su propio objeto `arguments` | ❌ No tiene `arguments` propio        |
| **Lectura**     | Más explícita                      | Más concisa                          |

#### Ejemplo

{% columns %}
{% column %}
{% code overflow="wrap" %}
```javascript
// Función tradicional
function hola() {
  return "Hola mundo";
}
```
{% endcode %}
{% endcolumn %}

{% column %}
{% code overflow="wrap" %}
```javascript
// Con función de flecha
const saludar = () => "Hola Mundo";

```
{% endcode %}
{% endcolumn %}
{% endcolumns %}



***

### Resumen

* **Qué es:** Una forma más corta de escribir funciones (`()=>{}`).
* **Ventajas:** Sintaxis más limpia, `this` heredado.
* **Cuándo usar:** Callbacks, programación funcional, código conciso.
* **Cuándo evitar:** Si necesitas `this` propio, `arguments` o constructor.

