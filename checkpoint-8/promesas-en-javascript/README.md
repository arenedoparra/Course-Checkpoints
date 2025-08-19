---
description: ¿Qué es una promesa en JS?
---

# 💍 Promesas en JavaScript

### Introducción

En JavaScript, una **promesa** (Promise) es un **objeto especial** que representa **el eventual resultado (o error)** de una operación que se ejecuta de forma **asíncrona**. Una **operación asincrónica** es una tarea que **no bloquea** la ejecución del programa mientras espera su resultado.&#x20;

Antes de que existieran las promesas, el manejo de código asíncrono se hacía con **callbacks** (funciones pasadas como argumento). El problema era que el código se volvía difícil de leer y mantener, algo llamado _Callback Hell._

#### Ejemplo

* Descargar datos de internet.
* Leer un archivo desde el disco.
* Esperar un temporizador.

{% hint style="success" %}
**Consejo**\
Prácticar promesas con ejemplos simples como **esperar unos segundos** o **simular una llamada a un servidor** antes de usarlas en proyectos grandes.
{% endhint %}

***

### Usos

* **Evitar el "Callback Hell"** (código desordenado y difícil de leer).
* Facilitan manejar **errores**.
* Permiten **manejar tareas asincrónicas** de forma más clara. Permiten **encadenar operaciones** asíncronas sin anidar múltiples niveles de funciones.
* Hacen el código **más limpio, facil de mantener y legible**.
* Se integran perfectamente con **`async`/`await`**.

#### Cómo se usa una promesa

Para manejar una promesa usamos:

* `.then()` Se ejecuta cuando la promesa se **cumple**.
* `.catch()` Se ejecuta cuando la promesa es **rechazada**.
* `.finally()` Se ejecuta siempre, haya éxito o error.

***

### Estados de una promesa

Una promesa **puede estar en uno de estos tres estados**

* **Pendiente (pending)** : Esperando a que la operación termine.
* **Cumplida (fulfilled):** Todo salió bien y tienes el resultado.
* **Rechazada (rejected):** Hubo un error y no se pudo completar.

```mermaid
    A[Promesa creada] -->|Pendiente| B{Operación asíncrona}
    B -->|Éxito| C[Cumplida - Fulfilled]
    B -->|Error| D[Rechazada - Rejected]
```

***

### Sintaxis

```javascript
const miPromesa = new Promise((resolve, reject) => {
    // Aquí va la operación asíncrona
    let exito = true;

    if (exito) {
        resolve("Operación  exitosa");
    } else {
        reject("Hubo un error ❌");
    }
});
// Cómo usar la promesa:
miPromesa
    .then(resultado => {
        console.log("Éxito:", resultado);
    })
    .catch(error => {
        console.error("Error:", error);
    });
```

* **`resolve()`** Indica que la promesa se cumplió correctamente.
* **`reject()`** Indica que la promesa falló.

***

### Componentes

1. **`new Promise()`**
   * Crea una nueva promesa.
   * Recibe una **función ejecutora** con dos parámetros: `resolve` y `reject`.
2. **`resolve(valor)`**
   * Indica que la operación terminó con éxito.
   * Devuelve el resultado a `.then()`.
3. **`reject(error)`**
   * Indica que la operación falló.
   * Devuelve el error a `.catch()`.
4. **`.then()`**
   * Define qué hacer cuando la promesa se resuelve con éxito.
5. **`.catch()`**
   * Define qué hacer cuando la promesa es rechazada (error).
6. **`.finally()`**
   * Define un bloque que se ejecuta **siempre**, haya éxito o error.

***

### [Promesas con `async` y `await`](promesas-con-async-y-await.md)&#x20;

**`async`/`await`** es una forma más legible de manejar las promesas.

#### Ventajas de async/await:

* El código es más parecido al síncrono.
* Más fácil de leer y depurar.
* Sigue usando promesas por detrás.

```javascript
async function obtenerDatos() {
    try {
        let respuesta = await fetch("https://........");
        let datos = await respuesta.json();
        console.log("Datos recibidos:", datos);
    } catch (error) {
        console.error("Error:", error);
    } finally {
        console.log("Proceso finalizado");
    }
}

obtenerDatos();
```

### Callbacks vs Promises vs Async/Await

| Técnica         | Ventajas                                          | Desventajas                       |
| --------------- | ------------------------------------------------- | --------------------------------- |
| **Callbacks**   | Compatibilidad antigua, directos                  | Callback Hell, difícil de leer    |
| **Promesas**    | Código más limpio, manejo centralizado de errores | Puede seguir siendo verboso       |
| **Async/Await** | Muy legible, similar a código síncrono            | Necesita `try/catch` para errores |

***

### Resumen

* **Una promesa** es un objeto que representa el resultado futuro de una operación asincrónica.
* Tiene tres estados: `pending`, `fulfilled`, `rejected`.
* Se usa para manejar tareas que toman tiempo sin bloquear el flujo del programa.
* Funciona con `.then()`, `.catch()` y `.finally()`.
* `async`/`await` es una forma más cómoda de usarlas.
