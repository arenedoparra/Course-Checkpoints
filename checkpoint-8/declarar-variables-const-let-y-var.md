---
description: ¿Cuáles son las diferencias entre const, let y var?
---

# 🆚 Declarar variables: Const, Let y Var

### Introducción

Aunque las tres palabras se utilizan para **declarar variables**, su **comportamiento interno** es distinto y puede generar errores si no lo entendemos bien.

Una **variable** es como una caja donde guardamos información. Esa información puede cambiar (como la edad de una persona) o puede ser fija (como el valor de Pi `3.1416`).

### Uso

Usa `const` por defecto, asegurando que tu variable no cambia accidentalmente.

Usa `let` solo cuando sepas que la variable cambiará su valor.

Evita usar `var` ya que es propenso a errores y ya está en desuso.

***

### 1. Var

`var` fue la primera forma de declarar variables en JavaScript por ello es la forma más antigua de declarar variables.

* Se puede **re-declarar** la misma variable sin error.
* Su **ámbito (scope)** es **funcional**, no de bloque.
* Se "mueve" al inicio del código gracias al **hoisting**.
* Se puede **re-asignar** su valor.

**Sintaxis**

```js
var nombre = "Ane";
console.log(nombre); // Ane
```

### 2. Let&#x20;

`let` fue introducido para solucionar los problemas de `var`de por lo que es la forma moderna de declarar variables.

* Su **ámbito es de bloque** (solo existe dentro de `{ }`).
* Se puede **re-asignar** (cambiar el valor).
* No se puede **re-declarar** en el mismo bloque.
* Se eleva con **hoisting**, pero queda en una "zona muerta temporal" (temporal dead zone).

{% hint style="success" %}
Con `let`, la variable solo existe **dentro del bloque `{ }`**, lo que evita errores.
{% endhint %}

**Sintaxis**

```js
let edad = 26;
edad = 27; // se puede cambiar
console.log(edad); // 27
```

### 3. Const&#x20;

`const` se utiliza para declarar variables que **no deben cambiar su valor** es decir para variables constantes.

* Su valor **no se puede re-asignar**.
* Su **ámbito es de bloque** (igual que `let`).
* Se debe **inicializar obligatoriamente** al declararse.

**Sintaxis**

```js
const PI = 3.1416;
console.log(PI); // 3.1416
```

{% hint style="warning" %}
Si `const` guarda un **objeto o array**, **no significa que sea inmutable**. Lo que no se puede cambiar es la **referencia**, pero sí su contenido.
{% endhint %}

<table><thead><tr><th>Característica</th><th>Var</th><th>Let</th><th>Const</th></tr></thead><tbody><tr><td>Uso</td><td>Evitarlo</td><td>Variables que cambian</td><td>Variables fijas</td></tr><tr><td>Re-asignar valor</td><td>✅ </td><td>✅ </td><td>❌ </td></tr><tr><td>Re-declarar</td><td>✅ </td><td>❌ </td><td>❌ </td></tr><tr><td>Ámbito (scope)</td><td>Función</td><td>Bloque</td><td>Bloque</td></tr><tr><td>Hoisting</td><td>Sí, con valor <code>undefined</code></td><td>✅ </td><td>✅ </td></tr><tr><td>Ejemplo</td><td><pre><code>var x = 10;
var x = 20; // se puede re-declarar
console.log(x); // 20
</code></pre></td><td><pre><code>let y = 10;
// let y = 20; // ❌ Error: no se puede re-declarar
y = 20; // se puede re-asignar
console.log(y); // 20
</code></pre></td><td><pre><code>const z = 10;
// z = 20; // ❌ Error: no se puede re-asignar
console.log(z); // 10
</code></pre></td></tr></tbody></table>

***

### Resumen

* **Usa `const` por defecto.** Declara con `let` solo si vas a **re-asignar** el valor.
* **Evita `var`** (es auntiguo): no respeta el bloque `{ }`, se puede re-declarar y puede producir errores sutiles por **hoisting**.
* **Ámbito (scope):**
  * `var` : **función**
  * `let` y `const` : **bloque** (entre llaves `{ }`, por ejemplo en `if`, `for`, `while`…).
* **Re-asignación:**
  * `var` ✅ | `let` ✅ | `const` ❌ (no puedes cambiar la referencia).
* **Re-declaración en el mismo bloque:**
  * `var` ✅ | `let` ❌ | `const` ❌
