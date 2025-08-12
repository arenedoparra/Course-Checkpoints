---
description: ¿Qué es una función de flecha?
---

# 🏹 Arrow function (función de flecha)

### Introducción

En JavaScript, una **función de flecha** (_arrow function_) es una forma **más corta y moderna** de escribir funciones. En vez de escribir el mismo código una y otra vez, lo metes dentro de una función y lo ejecutas cuando quieras. Son una **alternativa** a las funciones tradicionales para hacer el código más limpio y fácil de leer, especialmente cuando la función es **pequeña.**

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

1. **Menos código, Simplificar código (**&#x53;on más cortas de escribir).\
   Cuando el cuerpo de la función es corto, se puede reducir mucho la escritura.
2. **Más claras** Especialmente cuando son funciones pequeñas
3. **Callbacks**\
   Son muy útiles como funciones que se pasan como argumentos a otras funciones.
4. **No cambian el valor de `this`** .Esto es importante cuando trabajamos dentro de objetos o clases.
5. **Programación funcional**\
   Especialmente en métodos como `.map()`, `.filter()`, `.reduce()`.
6.  &#x20;**Se usan mucho en funciones anónimas** cuando no necesitas ponerle nombre.



#### Ejemplo con `.map()`:

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

#### **Función tradicional** vs **función de flecha**

| Forma Tradicional     | Función de Flecha        |
| --------------------- | ------------------------ |
| \`\`\`javascript      | \`\`\`javascript         |
| function suma(a, b) { | const suma = (a, b) => { |
| return a + b;         | return a + b;            |
| }                     | };                       |
| \`\`\`                | \`\`\`                   |

***

### Diferencias con las Funciones Tradicionales

1. **No tienen su propio `this`**
   * En funciones normales, `this` cambia dependiendo de cómo se llama la función.
   * En funciones de flecha, `this` hereda el valor del contexto donde se creó.
2. **No se pueden usar como constructoras** (`new`)
   * No puedes hacer `new miFuncionFlecha()`.
3. **Siempre son expresiones**
   * Una función de flecha siempre se guarda en una variable o constante.

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
const hola = () => {
  return "Hola mundo";
};
```
{% endcode %}
{% endcolumn %}
{% endcolumns %}

{% hint style="success" %}
### Return implícito

Si la función tiene **solo una línea** y **devuelve** algo, no es necesario escribir `return` ni llaves `{}`:

```javascript
const hola = () => "Hola mundo";
console.log(hola()); // "Hola mundo"
```
{% endhint %}

### Función con parámetros

Si solo hay **un parámetro**, podemos omitir los paréntesis:

```javascript
const saludarPersona = nombre => `Hola, ${nombre}`;
console.log(saludarPersona("Ane")); // Salida: Hola, Ane
```

Cuando hay más de un parámetro, los paréntesis son obligatorios:

```javascript
// Suma de dos números con función de flecha
const sumar = (a, b) => a + b;

console.log(sumar(5, 3)); // 8
```

* `(a, b)` → parámetros.
* `a + b` → valor que devuelve.
* Sin llaves y sin `return` → retorno implícito.

### Función con varias líneas de código

Si la función tiene varias instrucciones, **se usan llaves** y es necesario escribir `return` si queremos devolver un valor:

```javascript
const calcularArea = (base, altura) => {
    const area = base * altura;
    return area;
};
console.log(calcularArea(5, 10)); // Salida: 50
```

***

### Resumen

* **Qué es:** Una forma más corta de escribir funciones (`()=>{}`).
* **Ventajas:** Sintaxis más limpia, `this` heredado.
* **Cuándo usar:** Callbacks, programación funcional, código conciso.
* **Cuándo evitar:** Si necesitas `this` propio, `arguments` o constructor.

