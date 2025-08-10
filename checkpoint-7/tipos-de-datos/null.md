# 🗑️ Null

**Null** es la ausencia de cualquier tipo de valor.

Es un valor especial que indica **vacío intencional.**

{% hint style="danger" %}
No es lo mismo que `undefined`

* `undefined` → el valor no fue asignado.
* `null` → el valor fue asignado intencionalmente como vacío.
{% endhint %}

### Ejemplo

Si creamos una app y en ella colocamos un formulario con espacios vacios para que el usuario llene, pero queremos que en algunos de esos espacios no se rellene.

```javascript
var answer = null;
console.log(answer);
```
