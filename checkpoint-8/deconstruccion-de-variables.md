---
description: ¿Qué es la deconstrucción de variables?
---

# Deconstrucción de variables

### Introducción

La **deconstrucción** te permite **sacar valores** de **arrays** y **objetos** **y guardarlos en variables** de una forma **concisa**.



La **deconstrucción de variables,** en ingl **destructuring**) ,´es una **característica introducida en ECMAScript 6 (ES6)** que permite **extraer valores** de **arrays** o **propiedades de objetos** y asignarlos a variables de una manera **más sencilla, clara y elegante**.

En lugar de acceder a cada valor usando su índice o propiedad de manera manual, la deconstrucción nos da una **forma más rápida y legible de hacerlo**.

* **Destructuring** te da **claridad** y **menos código** al **extraer** datos de objetos/arrays.
* Úsalo especialmente en **parámetros de funciones**, **respuestas de APIs**, **iteraciones** y **código de configuración**.
* Acompáñalo con **defaults**, **alias** y el operador **rest** para cubrir el 99% de escenarios cotidianos.

{% hint style="success" %}
Si observas que accedes a `obj.algo.algo` muchas veces o a `arr[0]`, `arr[1]` repetidamente, piensa en añadir destructuring.
{% endhint %}

<table data-header-hidden data-full-width="true"><thead><tr><th width="271.88800048828125">Titulo</th><th>Ejemplo</th></tr></thead><tbody><tr><td><strong>Antes (sin destructuring)</strong></td><td><pre class="language-javascript"><code class="lang-javascript">const usuario = { nombre: "Ane", edad: 26 };
const nombre = usuario.nombre;
const edad   = usuario.edad;
</code></pre></td></tr><tr><td><strong>Despues (con destructuring)</strong></td><td><pre class="language-javascript"><code class="lang-javascript">const { nombre, edad } = { nombre: "Ane", edad: 26 };
</code></pre></td></tr></tbody></table>

***

### Errores comunes

#### Destructurar `null`/`undefined`&#x20;

```js
// const { x } = undefined; // ❌ TypeError
const obj = undefined;
const { x } = obj || {};
```

#### Asignar a variables YA declaradas: usa paréntesis

```js
let a;
({ a } = { a: 42 });
console.log(a); // 42
```

{% hint style="warning" %}
Sin paréntesis, el intérprete trata `{ a }` como un **bloque** y no como un **patrón de asignación**.
{% endhint %}

#### Re-declarar en el mismo bloque con `let/const`

```js
const { a } = { a: 1 };
// const { a } = { a: 2 }; // ❌ Cannot redeclare variable 'a'
```

***

### Destructuring con **arrays**

#### Sintaxis

```js
const numeros = [10, 20, 30];
const [a, b, c] = numeros;
console.log(a, b, c); // 10 20 30
```

#### Ignorar elementos

```js
const colores = ["rojo", "verde", "azul"];
const [primero, , tercero] = colores;
console.log(primero, tercero); // "rojo" "azul"
```

#### Valores por defecto

Se usan si la posición no existe o es `undefined`.

```js
const datos = [42];
const [x = 0, y = 0] = datos;
console.log(x, y); // 42 0
```

#### Intercambiar variables en una línea

```js
let alto = 800, ancho = 600;
[alto, ancho] = [ancho, alto];
console.log(alto, ancho); // 600 800
```

### Destructuring con **objetos**

#### Sintaxis

```js
const persona = { nombre: "Ane", edad: 26 };
const { nombre, edad } = persona;
console.log(nombre, edad); // "Ane" 26
```

#### Cambiar el nombre de la variable (alias)

```js
const user = { id: 101, nombre: "Ane" };
const { nombre: nombreCompleto, id: usuarioId } = user;
console.log(nombreCompleto, usuarioId); // "Ane" 101
```

#### Rest operator

```js
const producto = { sku: "ABC", precio: 9.99, stock: 10, activo: true };
const { sku, ...atributos } = producto;
console.log(sku);        // "ABC"
console.log(atributos);  // { precio: 9.99, stock: 10, activo: true }
```

#### Nested destructuring&#x20;

```js
const pedido = {
  id: 555,
  cliente: { nombre: "Ane", direccion: { ciudad: "Bilbao", zip: "48001" } }
};

const {
  cliente: {
    nombre: clienteNombre,
    direccion: { ciudad }
  }
} = pedido;

console.log(clienteNombre, ciudad); // "Ane" "Bilbao"
```

{% hint style="success" %}
Si algun apartado es `undefined`, considera `?.` u ofrecer **defaults (prederminado)**
{% endhint %}

### Destructuring en **parámetros de funciones**

#### Objetos como opciones

* No importa el **orden** de los argumentos.
* Puedes dar **valores por defecto**.
* Facilita la lectura.

```js
function crearUsuario({ nombre, email, rol = "usuario" }) {
  return { nombre, email, rol };
}

const u = crearUsuario({ nombre: "Ane", email: "ane@ejemplo.com" });
console.log(u); // { nombre: "Ane", email: "...", rol: "usuario" }
```

#### Arrays como parámetros

```js
function suma([a, b]) {
  return a + b;
}
console.log(suma([2, 3])); // 5
```

#### Defaults + destructuring en la firma

```js
function conectar({ host = "localhost", puerto = 5432 } = {}) {
  console.log(`Conectando a ${host}:${puerto}`);
}

conectar();                         // "Conectando a localhost:5432"
conectar({ host: "db", puerto: 1 }); // "Conectando a db:1"
```

### Destructuring en **iteraciones**

#### `for...of` con arrays

```js
const pares = [[1,"uno"], [2,"dos"], [3,"tres"]];
for (const [numero, texto] of pares) {
  console.log(numero, texto);
}
```

#### Iterar **entradas** de un objeto

```js
const opciones = { modo: "dev", debug: true };
for (const [clave, valor] of Object.entries(opciones)) {
  console.log(clave, "→", valor);
}
```

***

### Cheat sheet

* **Array**\
  `[a, b] = arr` | `[primero,,tercero] = arr` | `[x=0] = arr` | `[a, ...rest] = arr`
* **Objeto**\
  `{a} = obj` | `{a: alias} = obj` | `{a=1} = obj` | `{a, ...rest} = obj` | nested: `{c:{d}} = obj`
* **Funciones**:\
  `function f({a=1, b}) {}` | `function g([x, y=0]) {}`
* **Asignar a variables ya declaradas**\
  `({a} = obj)` (usa paréntesis)
* **Seguridad**\
  `const { a } = obj || {};` (si `obj` podría ser `null`/`undefined`)
