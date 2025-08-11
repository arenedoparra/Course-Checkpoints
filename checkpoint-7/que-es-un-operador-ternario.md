---
description: ¿Qué es un operador ternario?
---

# ↗️ Ternary Operator

### Introducción

En programación, muchas veces necesitamos **tomar decisiones,** normalmente para tomar decisiones usamos estructuras como `if...else`. Sin embargo, existe una forma **más corta y compacta** de escribir una condición: el **operador ternario**.&#x20;

El **operador ternario** en JavaScript es un operador condicional que evalúa una condición y devuelve un valor si la condición es `true` (verdadera) o devuelve otro valor si la condición es `false` (falsa).

Su nombre "ternario" viene de que trabaja con **tres partes**:

1. **Condición** → Lo que queremos comprobar.
2. **Valor si es verdadero** → Lo que se devuelve si la condición se cumple.
3. **Valor si es falso** → Lo que se devuelve si la condición no se cumple.

El operador ternario es como un **atajo** para escribir una condición que devuelve un valor u otro dependiendo de si la condición es verdadera o falsa.

### Usos

1. **Tomar decisiones rápidas** en una sola línea.
2. **Asignar valores** según una condición.
3. **Simplificar código**.
4. **Devolver un valor dentro de una función** sin necesidad de un `if...else` completo.

### Sintaxis

```javascript
condición ? valorSiVerdadero : valorSiFalso;
```

* `condición` → Una expresión que se evalúa como `true` o `false`.
* `?` → Indica el **inicio** de las dos posibles salidas.
* `valorSiVerdadero` → Lo que retorna si la condición es cierta.
* `:` → Separa las dos posibles salidas.
* `valorSiFalso` → Lo que retorna si la condición es falsa.

### Ejemplo con `if...else`Vs Ternary Operator

{% columns %}
{% column width="50%" %}
```javascript
let edad = 18;
let mensaje;

if (edad >= 18) {
  mensaje = "Eres mayor de edad";
} else {
  mensaje = "Eres menor de edad";
}

console.log(mensaje); // Eres mayor de edad
```
{% endcolumn %}

{% column width="50%" %}
```javascript
let edad = 18;
let mensaje = (edad >= 18) ? "Eres mayor de edad" : "Eres menor de edad";

console.log(mensaje); // Eres mayor de edad
```
{% endcolumn %}
{% endcolumns %}
