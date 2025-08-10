---
description: ¿Qué es un condicional?
---

# ⚙️ Condicionales en JS

### Introducción

Un **condicional** es una instrucción que permite que tu programa **tome decisiones**.&#x20;

En programación usamos condicionales para decir algo como:

> _"Si ocurre X, haz Y; si no ocurre X, haz Z."_
>
> ![](<../.gitbook/assets/image (2).png>)

***

### Importancia de los condicionales

Sin condicionales, un programa sólo podría ejecuta instrucciones en secuencia. Los condicionales permiten:

* Reaccionar a la entrada del usuario (ej.: si la contraseña es correcta).
* Validar datos (ej.: si el correo tiene formato válido).
* Controlar la lógica de negocio (ej.: aplicar descuento sólo si la compra supera X).
* Hacer que el software sea **dinámico** y **útil**.

***

### Conceptos básicos

* **Condición**: expresión que se evalúa como `true` o `false`.
* **Bloque**: conjunto de instrucciones que se ejecutan si la condición es verdadera o falsa.
* **Operadores de comparación**: `==`, `===`, `!=`, `>`, `<`, `>=`, `<=`.
* **Operadores lógicos**: `&&` (AND), `||` (OR), `!` (NOT).
* **Truthy / Falsy**: en algunos lenguajes (ej. JavaScript), no sólo `true/false` cuentan — ciertos valores se consideran `falsy` (equivalentes a `false`) como `0`, `""`, `null`, `undefined`, `NaN`.

***

### Sintaxis, ejemplos

#### JavaScript — `if`, `else if`, `else`

```javascript
const edad = 20;

if (edad >= 18) {
  console.log("Eres mayor de edad");
} else {
  console.log("Eres menor de edad");
}

// Con varias condiciones:
const nota = 85;

if (nota >= 90) {
  console.log("Excelente");
} else if (nota >= 70) {
  console.log("Aprobado");
} else {
  console.log("Reprobado");
}
```

**Ternary operator**

```javascript
const edad = 16;
const msg = (edad >= 18) ? "Mayor" : "Menor";
console.log(msg); // "Menor"
```

### Operadores

#### 1. Operadores de comparación

| Operador  | Significado                                   |
| --------- | --------------------------------------------- |
| `==`      | Igual (con conversión de tipos en JS)         |
| `===`     | Igual estricto (sin conversión de tipos — JS) |
| `!=`      | Distinto                                      |
| `!==`     | Distinto estricto (JS)                        |
| `>` `<`   | Mayor / Menor                                 |
| `>=` `<=` | Mayor o igual / Menor o igual                 |

#### 2. Operadores lógicos

* `&&` (AND) — true si ambas condiciones son true.
* `||` (OR) — true si al menos una es true.
* `!` (NOT) — invierte la condición.

```javascript
const a = true;
const b = false;
console.log(a && b); // false
console.log(a || b); // true
console.log(!a);     // false
```

***

### Buenas prácticas

#### 1. Mantener las condiciones simples

Evita expresiones grandes y difíciles de leer. Si es necesario, divide la condición en variables con nombres descriptivos.

```javascript
// Mal
if (user && user.profile && user.profile.age >= 18 && user.isActive) { ... }

// Mejor
const hasProfile = Boolean(user && user.profile);
const isAdult = hasProfile && user.profile.age >= 18;
if (isAdult && user.isActive) { ... }
```

#### 2. Evita anidar demasiados `if`s

Mucho anidamiento dificulta la lectura. Usa **guard clauses** (devoluciones tempranas).

```javascript
// En vez de:
if (a) {
  if (b) {
    // trabajo
  } else {
    // otra cosa
  }
}

// Mejor:
if (!a) return;
if (!b) return;
// trabajo

```

#### 3. Usa ternarios con moderación

Son útiles para casos simples. Evita encadenar demasiados ternarios, porque reducen legibilidad.

#### 4. Prefiere `===` en JavaScript

Evita bugs por conversión de tipos.

#### 5. Escribe tests para condiciones complejas

Cuando la lógica condicional es crítica, cubre los casos con tests unitarios.

***

### Errores comunes

* **Confundir `=` con `==` o `===`** (asignación vs comparación).
* **Olvidar que `0`, `""`, `null` son falsy en JS**.
* **Comparar floats directamente** (p. ej. `0.1 + 0.2 === 0.3` puede fallar por imprecisión).
* **Usar condiciones complejas sin comentarios** — documenta la intención, pero sin pasarte y actualizala si cambias el codigo.

