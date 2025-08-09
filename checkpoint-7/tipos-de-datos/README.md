---
description: ¿Cuáles son algunos tipos de datos JS?
cover: >-
  https://images.unsplash.com/photo-1516259762381-22954d7d3ad2?crop=entropy&cs=srgb&fm=jpg&ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHw2fHxQcm9ncmFtYWNpb24lMjBqYXZhc2NyaXB0fGVufDB8fHx8MTc1NDczOTIxNHww&ixlib=rb-4.1.0&q=85
coverY: 0
---

# 💻 Tipos de Datos en JavaScript

### 🔎 Qué es un tipo de Dato

Todo lo que escribimos en un lenguaje de programación es para **crear, almacenar, modificar o manipular datos**. Un tipo de dato, define que tipo de información es la que vamos a utilizar en nuestro código: si es un número, un texto, un valor falso o verdadero etc.

Un tipo de dato es **la clasificación de la información** que le dice a JavaScript **qué puede hacer con ese valor**. Cómo JavaScript **categoriza** todos nuestros puntos de datos.

* Si tenemos una variable, es cómo JS **ve** esa variable. Si por ejemplo tienes una frase, esa frase puede tener diversos códigos en ella.
* Si el dato que tenemos es un **número**, podremos hacer funciones matemáticas como sumarlo, restarlo, multiplicarlo...

***

### 💬 Comentarios&#x20;

No es un típo de datos, pero en JavaScript también existen los **comentarios**, estos nos permiten **poder añadir texto en el código sin ejecutarlo**. Normalmente en los comentarios debe haber una **intención clara**, no hay que rellenarlo todo de comentarios. Son exactamente lo que su nombre indica, comentarios sobre el codigo para facilitar su comprensión por ejemplo si trabajamos **en quipo**.

{% hint style="success" %}
Las clases, los módulos las funciones deben de ser autodescriptivas para no rellenar todo de comentarios.
{% endhint %}

{% hint style="warning" %}
Si el programa se sigue desarrollando y esos comentarios no se actualizan, pierden su funcionalidad.
{% endhint %}

### 📁 Tipos de Datos en JavaScript

| Tipo de dato                             | Descripción                         | Ejemplo               | Uso                     |
| ---------------------------------------- | ----------------------------------- | --------------------- | ----------------------- |
| [**Boolean**](boolean.md)                | Valores lógicos                     | `true`, `false`       | Decisiones              |
| [**Null**](null.md)                      | Representa ausencia de un valor     | `let data = null;`    | Resetear valores        |
| [**Undefined**](undefined.md)            | No tiene ningun valor asignado      | `let x; // undefined` | Variables sin iniciar   |
| [**Number**](number.md)                  | Números                             | `42`, `3.14`          | Operaciones matemáticas |
| [**String**](string-cadenas-de-texto.md) | Texto                               | `"Hola"`, `'Adios'`   | Frases, nombres...      |
| [**Symbol**](symbol.md)                  | Identificadores únicos e inmutables | `Symbol("id")`        | Keys únicas en objetos  |

### 🏷️ Cómo ver qué tipo de Dato estamos usando
