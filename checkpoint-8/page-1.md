---
description: ¿Qué tipo de bucles hay en JS?
---

# 🌀 Bucles en JavaScipt

### Introducción

Un **bucle,** también llamado _loop_ en inglés, es una  una estructura de control que **repite una o varias instrucciones varias veces** de un bloque de código **mientras** se cumpla una **condición**. Sirve para tareas repetitivas: recorrer listas, acumular totales, buscar elementos, esperar eventos, procesar datos de una API, etc.

En JavaScript disponemos de varios bucles, cada uno con **ventajas** y **casos de uso** diferentes.

{% hint style="success" %}
En otras palabras, los bucles son una forma de decirle al ordenador:

“Haz esto una y otra vez hasta que yo te diga que pares"
{% endhint %}

#### Tipos

* **`for` :** clásico para el control  por **índice.**
* **`while`** : Lo repite **mientras** una condición sea **verdadera**.
* **`do...while`** : Lo ejecuta **al menos una vez** y luego verifica la condición.
* **`for...in`** : Itera sobre **claves enumerables** de un **objeto.**
* **`for await...of`** : Recorre **iterables asíncronos** (ej.: resultados que llegan con retraso).
* **Métodos de Arrays** (no son “bucles” del lenguaje, pero iteran):
  * `forEach` (recorrer)
  * `map` (transformar)
  * `filter` (filtrar)

***

### 1. For

* El cásico.&#x20;
* Cuando necesitas un **contador** (`i`) y control absoluto del **índice**, el **paso** y el **sentido** (ascendente/descendente).
* Para **recorrer arrays** por posición o **modificarlos por índice**.

{% hint style="success" %}
Se utiliza cuando sabemos **exactamente cuántas veces queremos repetir** algo.
{% endhint %}

<table><thead><tr><th>Sintaxis</th><th>Ejemplo</th></tr></thead><tbody><tr><td><pre class="language-javascript" data-overflow="wrap"><code class="lang-javascript">for (inicialización; condición; actualización) {
// bloque que se repite
}
</code></pre></td><td><pre class="language-javascript" data-overflow="wrap"><code class="lang-javascript">for (let i = 0; i &#x3C; 5; i++) {
  console.log(i);
}
// 0 1 2 3 4
</code></pre></td></tr><tr><td></td><td><pre class="language-javascript" data-overflow="wrap"><code class="lang-javascript">const frutas = ["manzana", "pera", "kiwi"];
for (let i = 0; i &#x3C; frutas.length; i++) {
  console.log(i, frutas[i]);
}
</code></pre></td></tr></tbody></table>

#### Errores comunes

* **Off-by-one**: usar `<` vs `<=` puede cambiar cuántas veces iteras.
* **No actualizar el índice** puede crear un bucle infinito.
* **Usar `var`** dentro del `for` puede causar **capturas extrañas** en callbacks. Mejor usar `let`.

{% hint style="info" %}
Usar `let` en el índice para que su valor sea de bloque.
{% endhint %}

### 2. While

* Se refiere a mientras.
* Cuando la cantidad de iteraciones **no se conoce.**
* Cuando lees de una **cola**, **stream**, o esperas que **cambie** la condición.

{% hint style="success" %}
El bucle `while` se usa cuando **no sabemos cuántas veces repetiremos** el código, pero queremos que siga ejecutándose **mientras la condición sea verdadera**.
{% endhint %}

<table><thead><tr><th>Sintaxis</th><th>Ejemplo</th></tr></thead><tbody><tr><td><pre class="language-javascript" data-overflow="wrap"><code class="lang-javascript">while (condición) {
  // se repite mientras condición sea true
}
</code></pre></td><td><pre class="language-javascript" data-overflow="wrap"><code class="lang-javascript">const cola = ["a", "b", "c"];
while (cola.length > 0) {
  const item = cola.shift();
  console.log("Procesado:", item);
}
</code></pre></td></tr></tbody></table>

{% hint style="danger" %}


Si te olvidars de **actualizar** la condición se vuelve en un **bucle infinito**.

```js
let n = 3;
while (n > 0) {
  console.log(n);
  n--; // ¡Importante! Sin esto, infinito
}
```
{% endhint %}

### 3. Do...while

* Para recorrer **claves enumerables** de un **objeto** plano.

<table><thead><tr><th>Sintaxis</th><th>Ejemplo</th></tr></thead><tbody><tr><td><pre class="language-javascript" data-overflow="wrap"><code class="lang-javascript">do {
  // se ejecuta al menos una vez
} while (condición);
</code></pre></td><td><pre class="language-javascript" data-overflow="wrap"><code class="lang-javascript">let intentos = 0;
do {
  intentos++;
  console.log("Intento n.º", intentos);
} while (intentos &#x3C; 3);
</code></pre></td></tr></tbody></table>

### 4. For...in

* Se refiere a haz... mientras
* Cuando **debes ejecutar al menos una vez** el bloque, y **luego** comprobar la condición.
* Por ejemplo, leer entrada del usuario y volver a pedir si no es válida.

<table><thead><tr><th>Sintaxis</th><th>Ejemplo</th></tr></thead><tbody><tr><td><pre class="language-javascript" data-overflow="wrap"><code class="lang-javascript">for (const clave in objeto) {
  // clave es un string con el nombre de la propiedad
}}
</code></pre></td><td><pre class="language-javascript" data-overflow="wrap"><code class="lang-javascript">const persona = { nombre: "Ane", edad: 27 };
for (const k in persona) {
  console.log(k, persona[k]);
}
</code></pre></td></tr></tbody></table>

<table data-full-width="true"><thead><tr><th width="155.977294921875">Tipo de bucle</th><th>Uso</th><th>Ejemplo</th></tr></thead><tbody><tr><td><strong>for</strong></td><td>Repetir un número conocido de veces</td><td><code>for (let i=0; i&#x3C;10; i++) { ... }</code></td></tr><tr><td><strong>while</strong></td><td>Repetir mientras una condición sea verdadera</td><td><code>while (x > 0) { ... }</code></td></tr><tr><td><strong>do...while</strong></td><td>Igual que <code>while</code>, pero se ejecuta <strong>al menos una vez</strong></td><td><code>do { ... } while(x > 0)</code></td></tr><tr><td><strong>for...of</strong></td><td>Recorrer <strong>valores</strong> de arrays, strings, iterables</td><td><code>for (let item of lista) { ... }</code></td></tr><tr><td><strong>for...in</strong></td><td>Recorrer <strong>prepiedades</strong> de objetos</td><td><code>for (let clave in objeto) { ... }</code></td></tr></tbody></table>

### Métodos de Arrays&#x20;

* **Iteran** pero no son bucles.

<table><thead><tr><th width="213.9981689453125">Método</th><th>Uso</th><th>Return</th></tr></thead><tbody><tr><td><code>forEach</code></td><td>Ejecutar efecto por cada elemento</td><td><code>undefined</code></td></tr><tr><td><code>map</code></td><td>Transformar cada elemento en otro</td><td>Nuevo array</td></tr><tr><td><code>filter</code></td><td>Quedarse con los que cumplan una condición. 'filtrar'</td><td>Nuevo array</td></tr><tr><td><code>reduce</code></td><td>Acumular en un único valor</td><td>Valor acumulado</td></tr><tr><td><code>some</code></td><td>Si alguno lo cumple</td><td><code>true</code> / <code>false</code></td></tr><tr><td><code>every</code></td><td>Si todos lo cumplen</td><td><code>true</code> / <code>false</code></td></tr><tr><td><code>find</code></td><td>Buscar</td><td>Elemento / <code>undefined</code></td></tr><tr><td><code>findIndex</code></td><td>Buscar en indice</td><td>Índice / <code>-1</code></td></tr></tbody></table>

### Errores comunes

1. **Bucle infinito**\
   Olvidar actualizar la condición en `while` / `for`.
2. **`for...in` sobre arrays**\
   Puede iterar propiedades extra o desordenadas.
3. **`forEach` con `await`**\
   `forEach` **no** espera.
4. **Re-declarar variables índice**\
   “Cannot redeclare block-scoped variable…”. Usar `let` y **evita** re-declarar en el mismo ámbito.

```php
¿Necesitas repetir algo un número fijo de veces?
   └── Sí → usa for
   └── No → ¿Depende de una condición?
              └── Sí → usa while
              └── ¿Quieres que se ejecute al menos una vez? → usa do...while

¿Quieres recorrer una lista (array o string)?
   └── Usa for...of

¿Quieres recorrer un objeto por propiedades?
   └── Usa for...in
```
