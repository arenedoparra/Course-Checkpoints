---
description: ¿Qué tipo de bucles hay en JS?
---

# 🌀 Bucles en JavaScipt

### Introducción

Un **bucle** o en inglés un **loop** es una estructura de control que **repite** un bloque de código **mientras** se cumpla una **condición**. Sirve para tareas repetitivas: recorrer listas, acumular totales, buscar elementos, esperar eventos, procesar datos de una API, etc.

En JavaScript disponemos de varios bucles, cada uno con **ventajas** y **casos de uso** diferentes.

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

```svg
<svg width="720" height="230" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="20" width="200" height="50" rx="8" ry="8" fill="#EFF6FF" stroke="#1D4ED8"/>
  <text x="120" y="50" font-family="monospace" font-size="14" text-anchor="middle">Inicio</text>

  <polygon points="300,45 360,20 420,45 360,70" fill="#ECFDF5" stroke="#059669"/>
  <text x="360" y="50" font-family="monospace" font-size="12" text-anchor="middle">¿Condición?</text>

  <rect x="520" y="20" width="180" height="50" rx="8" ry="8" fill="#FEF2F2" stroke="#DC2626"/>
  <text x="610" y="50" font-family="monospace" font-size="14" text-anchor="middle">Fin del bucle</text>

  <rect x="300" y="130" width="220" height="50" rx="8" ry="8" fill="#F5F3FF" stroke="#7C3AED"/>
  <text x="410" y="160" font-family="monospace" font-size="12" text-anchor="middle">Bloque del bucle</text>

  <line x1="220" y1="45" x2="300" y2="45" stroke="#1F2937" marker-end="url(#arrow)"/>
  <line x1="420" y1="45" x2="520" y2="45" stroke="#1F2937" marker-end="url(#arrow)"/>
  <line x1="410" y1="130" x2="410" y2="70" stroke="#1F2937" marker-end="url(#arrow)"/>
  <line x1="360" y1="70" x2="360" y2="130" stroke="#1F2937" marker-end="url(#arrow)"/>
  <line x1="360" y1="180" x2="360" y2="200" stroke="#1F2937"/>
  <line x1="360" y1="200" x2="120" y2="200" stroke="#1F2937"/>
  <line x1="120" y1="200" x2="120" y2="70" stroke="#1F2937" marker-end="url(#arrow)"/>

  <text x="470" y="35" font-family="monospace" font-size="12">NO</text>
  <text x="330" y="120" font-family="monospace" font-size="12">SÍ</text>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#1F2937"/>
    </marker>
  </defs>
</svg>

```
