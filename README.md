# Quiz-1-Lenguajes 

Este repositorio contiene la resolución de **tres problemas prácticos** relacionados con programación en Python, estructuras de datos y diseño de software. Cada problema incluye descripción, diseño, métodos principales y la implementación funcional en Python.

---
Autor: Eduardo Hincapie Uribe 
---
## Problema 1: Sistema de navegación de páginas web

**Descripción:**  
Se diseñó un sistema que permite a los usuarios navegar por páginas web, con funcionalidad de **retroceder** (`goBack()`), **avanzar** (`goForward()`) y **cargar nuevas páginas** (`loadPage(url)`), simulando la navegación de un navegador moderno.

**Características implementadas:**
- Navegación hacia atrás y hacia adelante.
- Manejo de casos extremos:
  - Intentar retroceder sin páginas anteriores.
  - Intentar avanzar sin páginas siguientes.
- Registro del historial de páginas visitadas.

**Diagramas:**
- Diagrama de flujo que ilustra el comportamiento de la navegación y actualización del historial.

**Métodos principales:**
- `loadPage(url)`: Carga una nueva página en el historial.
- `goBack()`: Retrocede a la página anterior si existe.
- `goForward()`: Avanza a la página siguiente si existe.

**Lenguaje utilizado:** Python

---

## Problema 2: Función de autocompletar

**Descripción:**  
Se implementó un sistema de autocompletado que, dado un **prefijo**, devuelve todas las palabras posibles que comienzan con dicho prefijo. Está optimizado para la **búsqueda eficiente de palabras**.

**Características implementadas:**
- Inserción de palabras (`insert(word)`).
- Búsqueda rápida por prefijo (`autocomplete(prefix)`).
- Manejo de múltiples prefijos.
- Estructura de datos eficiente: **Trie (árbol de prefijos)**.

**Diagramas:**
- Diagrama UML de clases que muestra la relación entre `Trie` y `TrieNode`.

**Métodos principales:**
- `insert(word)`: Agrega una palabra al Trie.
- `autocomplete(prefix)`: Devuelve una lista de palabras que comienzan con el prefijo dado.

**Lenguaje utilizado:** Python

---

## Problema 3: Sistema de recomendación de productos

**Descripción:**  
Se desarrolló un sistema de recomendación que sugiere productos basándose en las relaciones entre usuarios y productos, siguiendo la lógica:  

> “Los usuarios que compraron X también compraron Y”.

**Características implementadas:**
- Registro de compras por usuario (`addPurchase(usuario, producto)`).
- Generación de recomendaciones (`getRecommendations(usuario)`).
- Manejo de múltiples usuarios y productos.
- Evita recomendar productos que el usuario ya posee.

**Diagramas:**
- Diagrama de relaciones Usuario–Producto mostrando cómo los usuarios y productos están conectados para generar recomendaciones.

**Métodos principales:**
- `addPurchase(usuario, producto)`: Registra una compra de un usuario.
- `getRecommendations(usuario)`: Devuelve productos recomendados según compras compartidas.

**Lenguaje utilizado:** Python

---

## Instrucciones de uso:

1. Clonar el repositorio:
```bash
git clone <URL_DEL_REPOSITORIO>

python Problema1_Navegacion.py
python Problema2_Autocompletar.py
python Problema3_Recomendacion.py

