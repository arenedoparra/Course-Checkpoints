---
description: ¿Cuáles son las tres funciones de String en JS?
---

# ⛓️ Funciones de String

### Introducción

Un **String** es un tipo de dato que representa una **secuencia de caracteres**: letras, números, símbolos, espacios, etc. Es decir, un **texto** o un **mensaje**. El texto siempre se escribe entre **comillas**:

Por ejemplo: `"Buenos días"`, `"JavaScript"`, `"1234"`, `"Gracias!"`.

Una **función** (o _método_) es una **herramienta** que podemos usar para **hacer algo con o en un texto**. En JavaScript hay muchas más de 20 funciones para trabajar con strings. Estas funciones nos permiten **manipular, buscar, transformar y comparar Strings**. Normalmente las 3 básicas o más comunes suelen ser:&#x20;

* `.length` (Saber cuántos caracteres tiene un String)
* `.toUpperCase()` (Convertir un String a mayúsculas)
* `.toLowerCase()` (Convertir un String a minúsculas)

### Sintaxis&#x20;

La forma de usar una función de String es:

```javascript
nombreDelString.funcionDeString(argumentosOpcionales)

let texto = "JavaScript";
let resultado = texto.includes("Script");
console.log(resultado); // true
```

#### 1. Obtener información

| Función          | Descripción                                                                | Ejemplo                   |
| ---------------- | -------------------------------------------------------------------------- | ------------------------- |
| `.length`        | Devuelve la cantidad de caracteres.                                        | `"Hola".length // 4`      |
| `.charAt(index)` | Devuelve el carácter en la posición indicada.                              | `"Hola".charAt(1) // 'o'` |
| `.at(index)`     | Versión moderna para obtener el carácter en un índice (soporta negativos). | `"Hola".at(-1) // 'a'`    |

#### 2. Modificar el formato

| Función          | Descripción             | Ejemplo                          |
| ---------------- | ----------------------- | -------------------------------- |
| `.toUpperCase()` | Convierte a mayúsculas. | `"hola".toUpperCase() // 'HOLA'` |
| `.toLowerCase()` | Convierte a minúsculas. | `"HOLA".toLowerCase() // 'hola'` |

#### 3. Buscar

| Función                   | Descripción                                                          | Ejemplo                                  |
| ------------------------- | -------------------------------------------------------------------- | ---------------------------------------- |
| `.indexOf(substring)`     | Devuelve la posición donde aparece la subcadena (o -1 si no existe). | `"JavaScript".indexOf("Script") // 4`    |
| `.lastIndexOf(substring)` | Igual que `.indexOf` pero desde el final.                            | `"Hola Hola".lastIndexOf("Hola") // 5`   |
| `.includes(substring)`    | Devuelve `true` si encuentra la subcadena.                           | `"Hola mundo".includes("mundo") // true` |
| `.startsWith(substring)`  | Verifica si empieza con esa subcadena.                               | `"Hola".startsWith("Ho") // true`        |
| `.endsWith(substring)`    | Verifica si termina con esa subcadena.                               | `"Hola".endsWith("la") // true`          |

#### 4. Extraer partes

| Función                               | Descripción                                                             | Ejemplo                             |
| ------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------- |
| `.slice(start, end)`                  | Extrae una parte desde un índice inicial hasta uno final (no incluido). | `"JavaScript".slice(0,4) // 'Java'` |
| `.substring(start, end)`              | Similar a `.slice`, pero no acepta índices negativos.                   | `"Hola".substring(1,3) // 'ol'`     |
| `.substr(start, length)` _(obsoleto)_ | Extrae desde un índice cierta cantidad de caracteres.                   | `"Hola".substr(1,2) // 'ol'`        |

#### 5. Reemplazar

| Función                         | Descripción                        | Ejemplo                                                       |
| ------------------------------- | ---------------------------------- | ------------------------------------------------------------- |
| `.replace(search, newValue)`    | Reemplaza la primera coincidencia. | `"Hola mundo".replace("mundo","JS") // 'Hola JS'`             |
| `.replaceAll(search, newValue)` | Reemplaza todas las coincidencias. | `"Hola mundo mundo".replaceAll("mundo","JS") // 'Hola JS JS'` |

#### 6. Dividir y unir

| Función             | Descripción                                       | Ejemplo                                   |
| ------------------- | ------------------------------------------------- | ----------------------------------------- |
| `.split(separator)` | Convierte el string en array usando un separador. | `"a,b,c".split(",") // ['a','b','c']`     |
| `.concat(string2)`  | Une dos o más cadenas.                            | `"Hola".concat(" mundo") // 'Hola mundo'` |
| Operador `+`        | También concatena.                                | `"Hola" + " mundo" // 'Hola mundo'`       |

#### 7. Repetir

| Función          | Descripción                     | Ejemplo                      |
| ---------------- | ------------------------------- | ---------------------------- |
| `.repeat(count)` | Repite la cadena `count` veces. | `"ha".repeat(3) // 'hahaha'` |
