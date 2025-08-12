---
description: ¿Qué hacen async y await por nosotros?
---

# Promesas con async y await

### Introducción

Al programar en Javascript, hay tareas que **tardan un tiempo en completarse**. Por ejmplo,

* Leer datos desde una base de datos&#x20;
* Descargar información de un servidor&#x20;
* Esperar la respuesta de una API&#x20;
* Procesar un archivo pesado

Este tipo de tareas **no ocurren al momento o instantaneamente**. Si JavaScript esperara a que terminaran para seguir ejecutando el resto del código, **la página o aplicación quedaría congelada**. Para solucionar esto, JavaScript usa **programación asíncrona**. Ahí es donde entran en juego **`async`** y **`await`** que nos permiten **trabajar con código asíncrono de manera más sencilla y legible**.Trabaja como si fuera código síncrono, pero sin bloquear la aplicación.

Antes de `async` y `await`, el manejo de tareas asíncronas se hacía con **promesas** y `.then()`.Esto funciona, pero cuando hay muchas operaciones encadenadas, el código se vuelve difícil de leer (lo que llamamos **callback hell**).

#### Síncrono vs asíncrono

**Código síncrono**: Se ejecuta línea por línea, esperando que cada tarea termine antes de pasar a la siguiente.

**Código asíncrono:** Permite que ciertas tareas se ejecuten **en segundo plano** mientras el resto del programa sigue funcionando.

***

### Usos

* Para escribir un código más **limpio y fácil de leer**
* Para evitar el **callback hell**
* Para manejar más **intuitivo** las promesas
* Es más **parecido al código síncrono**, lo que facilita aprender

***

### Funcionamiento

* `async` transforma la función en una que devuelve una promesa.
* Cuando ejecutas `await promesa`, la función `async` **suspende su ejecución** en ese punto pero **no bloquea** el hilo principal (evento loop sigue ejecutando otras cosas).
* Al resolverse la promesa, la ejecución de la función se reanuda en la siguiente línea.
* Si la promesa se rechaza, la ejecución salta fuera de `await` lanzando la excepción (como si hicieras `throw`), permitiendo usar `try/catch`.

### Async and Await

| Promesa   | Funcion                                                                  | Uso                                   |
| --------- | ------------------------------------------------------------------------ | ------------------------------------- |
| **async** | Marca una función como asíncrona y devuelve una promesa automáticamente. | Antes de la definición de la función. |
| **await** | Pausa la ejecución de la función hasta que la promesa se resuelva.       | Solo dentro de funciones `async`.     |

### Async

* Se coloca antes de la definición de una función, es una **palabra clave** que ponemos **antes de una función**.
* Indica que **esa función siempre devolverá una promesa**.
* Nos permite usar `await` dentro de ella.

**Sintaxis**

{% columns %}
{% column %}
{% code overflow="wrap" %}
```javascript
async function miFuncion() {
    return "Hola mundo";
}
```
{% endcode %}
{% endcolumn %}

{% column %}
{% code overflow="wrap" %}
```javascript
function miFuncion() {
    return Promise.resolve("Hola mundo");
}
```
{% endcode %}
{% endcolumn %}
{% endcolumns %}

{% hint style="warning" %}
Una función marcada `async` **siempre** devuelve una **promesa**. Si devuelves un valor normal, JS lo envuelve en `Promise.resolve(valor)` automáticamente.

```javascript
async function saludar() {
  return "Hola";
}

const p = saludar(); // p es una Promise
p.then(v => console.log(v)); // imprime "Hola"
```
{% endhint %}

### Await

* Es una **palabra clave** que solo se puede usarse **dentro de funciones `async`**.
* Hace que JavaScript **espere** a que una promesa se resuelva antes de continuar con la siguiente línea. Es decir, pausa la ejecución de la **función async** hasta que la promesa se resuelva (o rechace).

**Sintaxis**

{% columns %}
{% column width="50%" %}
{% code overflow="wrap" %}
```javascript
let resultado = await promesa;
```
{% endcode %}
{% endcolumn %}

{% column width="50%" %}
{% code overflow="wrap" %}
```javascript
async function demo() {
  const valor = await Promise.resolve(42);
  console.log(valor); // 42
}
```
{% endcode %}
{% endcolumn %}
{% endcolumns %}

Si `promesa` se resuelve, `resultado` obtiene el valor. Si la promesa es rechazada, se lanza una excepción (que podemos capturar con `try/catch`).

### `async/await` vs `.then/.catch` vs Callbacks

| Característica           | **async/await**                                                                                                                                  | **.then() / .catch()**                                                                      | **Callbacks**                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Estilo de código**     | Más limpio y legible, se parece al código síncrono.                                                                                              | Encadenado con promesas, más ordenado que callbacks pero menos natural que `async/await`.   | Puede generar **callback hell** (pirámide de la perdición) si se anidan mucho.                          |
| **Facilidad de lectura** | Muy alta: se lee como un flujo normal de instrucciones.                                                                                          | Media: cada `.then()` representa un paso; legible, pero se fragmenta.                       | Baja: difícil de seguir cuando hay muchas funciones anidadas.                                           |
| **Manejo de errores**    | Con `try...catch`, muy similar al código tradicional.                                                                                            | Con `.catch()`, separado de la lógica principal.                                            | Hay que manejar errores manualmente (ej. `if (err) { ... }`).                                           |
| **Soporte de async**     | Ideal para trabajar con Promesas y operaciones asíncronas.                                                                                       | Soporta promesas nativamente.                                                               | Necesita que las funciones acepten callbacks; no usa promesas.                                          |
| **Depuración**           | Fácil de depurar, las excepciones se lanzan como en código síncrono.                                                                             | Algo más difícil; las trazas de error pueden ser más complejas.                             | Más difícil aún, especialmente con callbacks anidados.                                                  |
| **Compatibilidad**       | Requiere ES2017 o posterior (o transpilar con Babel).                                                                                            | Compatible desde ES6.                                                                       | Compatible con versiones antiguas de JavaScript.                                                        |
| **Manejo secuencial**    | Muy simple: basta con usar `await` en cada paso.                                                                                                 | Hay que encadenar varios `.then()`.                                                         | Hay que anidar llamadas y pasar funciones como argumentos.                                              |
| **Manejo paralelo**      | Necesita `Promise.all()` o `Promise.allSettled()` para correr en paralelo.                                                                       | Igual que `async/await`.                                                                    | Mucho más difícil de implementar sin librerías extra.                                                   |
| **Ejemplo básico**       | `js\nasync function ejemplo() {\n try {\n const data = await fetchData();\n console.log(data);\n } catch (err) {\n console.error(err);\n }\n}\n` | `js\nfetchData()\n .then(data => console.log(data))\n .catch(err => console.error(err));\n` | `js\nfetchData(function(err, data) {\n if (err) return console.error(err);\n console.log(data);\n});\n` |
| **Cuándo usarlo**        | Cuando quieras escribir código asíncrono limpio y fácil de mantener.                                                                             | Cuando trabajes con APIs basadas en Promesas pero quieras encadenar transformaciones.       | Cuando trabajes con librerías antiguas o APIs que solo aceptan callbacks.                               |

### Buenas prácticas

* **Usar `try/catch`** dentro de las funciones `async` para manejar errores localmente.
* **No usar `await` si no se necesita el resultado de inmediato**; mejor usar `Promise.all` o dejar que las promesas se ejecuten sin await si quieres concurrencia.
* **No abusar de `await` en series** pensar en si las tareas pueden ser paralelizadas.
* **En funciones públicas, manejar o documentar** cómo se propagan errores.
* **Evitar `return await`** innecesario.
