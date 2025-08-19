---
description: ¿Qué es la deconstrucción de variables?
---

# Deconstrucción de variables

### Introducción

La **deconstrucción de variables,** en ingles **destructuring** ,es una **característica** que permite **extraer valores** de **arrays** o **propiedades de objetos** y guardarlos en variables de una manera **más sencilla, concisa, clara y elegante**.

En lugar de acceder a cada valor usando su índice o propiedad de manera manual, la deconstrucción nos da una **forma más rápida y legible de hacerlo**.

#### Ventajas

* **Código más limpio y legible:** Te da **claridad** y **menos código** al **extraer** datos de objetos/arrays.
* **Menos repetición** (no necesitas `obj.prop` una y otra vez).
* **Ideal en funciones:** para extraer parámetros directamente.
* **Permite valores por defecto:** Acompáñalo con **defaults**, **alias** y el operador **rest** para cubrir el 99% de escenarios cotidianos y para mayor seguridad.
* **Más moderno y expresivo:** muy usado en frameworks como **React o Angular.**

{% hint style="success" %}
Si observas que accedes a `obj.algo.algo` muchas veces o a `arr[0]`, `arr[1]` repetidamente, piensa en añadir destructuring.
{% endhint %}

<table data-header-hidden data-full-width="true"><thead><tr><th width="240.55096435546875">Titulo</th><th width="236.5665283203125">Descipción</th><th>Ejemplo</th></tr></thead><tbody><tr><td><strong>Antes (sin destructuring)</strong></td><td>Esto funciona, pero cuando la lista es larga o el objeto tiene muchas propiedades, puede volverse repetitivo y difícil de leer.</td><td><pre class="language-javascript"><code class="lang-javascript">const usuario = { nombre: "Ane", edad: 26 };
const nombre = usuario.nombre;
const edad   = usuario.edad;
</code></pre></td></tr><tr><td><strong>Despues (con destructuring)</strong></td><td>En una sola linea se accede a los valores</td><td><pre class="language-javascript"><code class="lang-javascript">const { nombre, edad } = { nombre: "Ane", edad: 26 };
</code></pre></td></tr></tbody></table>

***

### Tipos

Existen **dos tipos de deconstrucción**:

1. **Deconstrucción de Arrays**
2. **Deconstrucción de Objetos**

{% hint style="info" %}
También podemos aplicar la deconstrucción en **parámetros de funciones**, usar **valores por defecto**, **renombrar variables** y más.
{% endhint %}

### Destructuring de **arrays**

#### Sintaxis

```js
const numeros = [10, 20, 30];
const [a, b, c] = numeros;
console.log(a, b, c); // 10 20 30
```

#### Ignorar elementos

Se pueden **ignorar valores** usando comas

```js
const colores = ["rojo", "verde", "azul"];
const [primero, , tercero] = colores;
console.log(primero, tercero); // "rojo" "azul"
```

#### Valores por defecto

Se usan si la posición no existe o es `undefined`. Es decir, si el array no tiene suficientes valores, podemos asignar valores por defecto.

```js
const numeros = [10];

// El segundo valor no existe, entonces usamos el valor por defecto
const [a, b = 99] = numeros;

console.log(a, b); // 10 99
```

#### Intercambiar variables en una línea

```js
let alto = 800, ancho = 600;
[alto, ancho] = [ancho, alto];
console.log(alto, ancho); // 600 800
```

### Destructuring de **objetos**

La deconstrucción de objetos nos permite **extraer propiedades** y asignarlas a variables fácilmente.

#### Sintaxis

```js
const persona = {
  nombre: "Ane",
  edad: 27,
  pais: "Bilbao"
};

// Deconstrucción de objeto
const { nombre, edad, pais } = persona;

console.log(nombre); // Ane
console.log(edad);   // 27
console.log(pais);   // Bilbao

```

#### Renovar propiedades

Podemos asignar una propiedad a una variable con un **nombre diferente,** esto se conoce como crear un **alias**.

```js
const user = { id: 101, nombre: "Ane" };
const { nombre: nombreCompleto, id: usuarioId } = user;
console.log(nombreCompleto, usuarioId); // "Ane" 101
```

#### Valores por defecto

Si una propiedad no existe en el objeto, podemos darle un valor por defecto.

```javascript
const persona = {
  nombre: "Iratxe"
};

// "edad" no existe, usamos 18 como valor por defecto
const { nombre, edad = 18 } = persona;

console.log(nombre); // Iratxe
console.log(edad);   // 18
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

La deconstrucción es muy útil en funciones, especialmente cuando trabajamos con objetos.

#### Objetos como opciones

* No importa el **orden** de los argumentos.
* Puedes dar **valores por defecto**.
* Facilita la lectura.

```js
function mostrarUsuario({ nombre, edad }) {
  console.log(`Usuario: ${nombre}, Edad: ${edad}`);
}

const usuario = { nombre: "Ane", edad: 27 };

mostrarUsuario(usuario);
// Usuario: Ane, Edad: 27
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

| Tipo                      | Sintaxis                  | Ejemplo                           |
| ------------------------- | ------------------------- | --------------------------------- |
| Deconstrucción de Arrays  | `[a, b] = array`          | `const [x, y] = [1, 2]`           |
| Deconstrucción de Objetos | `{prop1, prop2} = objeto` | `const {nombre, edad} = persona`  |
| Valores por defecto       | `prop = valor`            | `const {ciudad = "Madrid"} = obj` |
| Renombrar propiedades     | `prop: nuevoNombre`       | `const {edad: años} = persona`    |
| En funciones (parámetros) | `function fn({prop}) {}`  | `function saluda({nombre}) {}`    |

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
