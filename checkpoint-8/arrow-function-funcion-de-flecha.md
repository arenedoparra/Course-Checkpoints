---
description: ¿Qué es una función de flecha?
---

# 🏹 Arrow function (función de flecha)

### Introducción

En JavaScript, una **función de flecha** (_arrow function_) es una forma **más corta y moderna** de escribir funciones. Son una **alternativa** a las funciones tradicionales para hacer el código más limpio y fácil de leer, especialmente cuando la función es **pequeña.**

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

### Usos
