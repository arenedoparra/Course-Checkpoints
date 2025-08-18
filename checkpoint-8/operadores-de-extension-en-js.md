---
description: ¿Qué hace el operador de extensión en JS?
---

# Operadores de extensión en JS

### Introducción

El **operador de extensión** en JavaScript, o en inglés **spread operator**, es un elemento versatil, poderoso y útil. Rapidamente se convirtió en una herramienta esencial para trabajar con **arrays**, **objetos** y **funciones** en JavaScript. El **spread operator** se representa con **tres puntos (`...`)**.

Este operador no es complicado de entender si lo vemos como una **herramienta que "desempaqueta" elementos de una estructura de datos** (como arrays u objetos) para poder usarlos individualmente. El operador de extensión es como una mano que **abre la caja y reparte todo su contenido**.

Resumiendo,

El operador de extensión `...` **permite expandir** (extender) los elementos de un iterable (como arrays o strings) o propiedades de un objeto donde se esperan múltiples elementos o argumentos.

### Por qué se usan?

* **Comodidad:** Evita código como `arr.concat()` o `Object.assign({}, a, b)`.
* **Inmutabilidad:** Permite crear **copias** y **versiones nuevas** sin cambiar el original.
* **Legibilidad:** El código se vuelve más claro y cercano al lenguaje natural.
* **Versatilidad:** Sirve con arrays, objetos, strings y llamadas a funciones.

### Sintaxis&#x20;

#### 1. L**lamadas a funciones**

```javascript
function maximo(a, b, c) { return Math.max(a, b, c); }

const numeros = [10, 7, 20];
maximo(...numeros); // equivale a maximo(10, 7, 20)
```

#### 2. L**iterales de array**

```javascript
const a = [1, 2];
const b = [3, 4];
const combinado = [...a, ...b]; // [1, 2, 3, 4]
```

#### 3. L**iterales de objeto**

```javascript
const base = { id: 1, nombre: "Ane" };
const extra = { rol: "admin" };
const perfil = { ...base, ...extra }; // { id: 1, nombre: "Ane", rol: "admin" }
```

{% hint style="danger" %}
**El Orden importa** cuando mezclas objetos
{% endhint %}

### Spread vs rest

*   **Spread (`...`)**: expande (**lado derecho**)

    ```js
    const partes = [1, 2, 3];
    suma(...partes); // spread: pasa 1, 2, 3 como argumentos sueltos
    ```
*   **Rest (`...`)**: recoge (**lado izquierdo)**

    ```js
    function suma(...nums) { // rest: junta N argumentos en un array
      return nums.reduce((a, b) => a + b, 0);
    }
    ```

{% hint style="success" %}
Spread = expandir / Rest = reunir. Misma sintaxis (`...`), **intención opuesta**.
{% endhint %}

### Usos

En los **arrays**: Sirve para copiar, combinar o descomponer listas.

En los **objetos**: Sirve para clonar objetos o fusionarlos.

En las **funciones**: Se utiliza para pasar argumentos de forma más sencilla.

<table data-full-width="true"><thead><tr><th width="106.78155517578125">Uso</th><th width="129.357177734375">Descripción</th><th width="358.2830810546875">Sintaxis</th><th>Ejemplo</th></tr></thead><tbody><tr><td><strong>Arrays</strong></td><td><strong>Copiar</strong>, <strong>fusionar</strong> o <strong>expandir</strong> elementos</td><td><code>const nuevoArray = [...arrayExistente];</code></td><td><pre><code>const original = [1, 2, 3];
const copia = [...original];

console.log(copia); // [1, 2, 3]
console.log(original === copia); // false (son distintos en memoria)
</code></pre></td></tr><tr><td></td><td><strong>Unir arrays</strong> sin necesidad de <code>concat</code></td><td><code>const combinado = [...arr1, ...arr2];</code></td><td><pre><code>const a = [1, 2];
const b = [3, 4];
const combinado = [...a, ...b];

console.log(combinado); // [1, 2, 3, 4]
</code></pre></td></tr><tr><td><strong>Objetos</strong></td><td><strong>Copiar propiedades</strong> de un objeto a otro o <strong>combinar objetos</strong></td><td><code>const nuevoObj = {...obj};</code></td><td><pre><code>const persona = { nombre: "Ane", edad: 27 };
const copia = { ...persona };

console.log(copia); // { nombre: "Ane", edad: 27 }
console.log(persona === copia); // false
</code></pre></td></tr><tr><td><strong>Funciones</strong></td><td>Cuando se usa como <strong>parámetro (rest)</strong> permite que la función reciba un número indefinido de argumentos</td><td><code>function sumar(...args) {}</code></td><td><pre><code>function sumar(a, b, c) {
  return a + b + c;
}

const numeros = [1, 2, 3];
console.log(sumar(...numeros)); // 6
</code></pre></td></tr><tr><td></td><td>Cuando se usa al <strong>invocar una función</strong>, expande un array en múltiples argumentos</td><td><code>funcion(...array);</code></td><td><pre><code>const numeros = [5, 10, 20];
console.log(Math.max(...numeros)); // 20
</code></pre></td></tr></tbody></table>
