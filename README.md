
# 📚 Sistema de Gestión de Librería en Python

Este proyecto es una aplicación de consola desarrollada en Python que permite registrar, buscar, prestar y devolver libros, manteniendo un control sobre los libros disponibles y prestados.

---

## ✨ Características Principales

🔹 Registrar libros con título, autor, año y categoría.  
🔹 Listar libros filtrando por estado (disponible, prestado o todos).  
🔹 Buscar libros por título, autor o categoría.  
🔹 Prestar libros a usuarios y guardar quién lo tiene.  
🔹 Devolver libros prestados.  
🔹 Mostrar todos los libros prestados.  
🔹 Evitar eliminar libros que estén prestados.  
🔹 Eliminar libros disponibles por su ID.  
🔹 Guardado automático de cambios en un archivo `books.json`.

---

## 📂 Estructura del Proyecto

```
tallerLibreria/
├── main.py              # Punto de entrada principal
├── features.py          # Funciones del sistema (registro, préstamo, búsqueda...)
├── validations.py       # Validaciones reutilizables
├── utils.py             # Funciones auxiliares (guardar, cargar, generar ID)
├── books.json           # Base de datos local de los libros
```

---

## 🚀 Cómo Ejecutarlo

1. Asegúrate de tener Python instalado (`>= 3.6`).
2. Descarga o clona este repositorio.
3. Abre la terminal en la carpeta del proyecto.
4. Ejecuta el programa:

```bash
python main.py
```

---

## 🧠 Funcionamiento General

### 📥 Registro de libros
- Se piden los datos del libro: título, autor, año y categoría.
- Se valida cada campo y se guarda automáticamente en `books.json`.

### 🔍 Búsqueda y listado
- Puedes buscar libros por título, autor o categoría.
- También puedes listar todos o filtrar solo los disponibles o prestados.

### 🤝 Préstamo y devolución
- Para prestar un libro, debes indicar su ID y el nombre del lector.
- El estado cambia a `Prestado`.
- Solo se pueden prestar libros que estén disponibles.
- Para devolver, solo ingresa el ID del libro prestado.

### ❌ Eliminación segura
- No es posible eliminar libros que estén prestados.
- Si el libro está disponible, puedes eliminarlo por su ID.

---

## 🛠 Validaciones Inteligentes

Las entradas del usuario se validan para asegurar que:
- No estén vacías.
- El año sea numérico y válido.
- El texto contenga solo letras donde corresponda.
- Las opciones estén dentro del menú válido.

---

## 💾 Persistencia de datos

Todos los cambios (registro, préstamo, devolución, eliminación) se guardan en tiempo real en el archivo `books.json`.

Ejemplo del formato JSON:

```json
[
  {
    "id": 1,
    "title": "Cien años de soledad",
    "author": "Gabriel García Márquez",
    "year": 1967,
    "category": "Realismo Mágico",
    "status": "Disponible",
    "borrowed_by": ""
  }
]
```

---

## 🧪 Ejemplo en Consola

```plaintext
📚 Bienvenido al sistema de gestión de librería

1. Registrar libro
2. Listar libros
3. Buscar libros
4. Prestar libro
5. Devolver libro
6. Mostrar libros prestados
7. Eliminar libro
8. Salir
Seleccione una opción: 1

Ingrese el título: El Principito
Ingrese el autor: Antoine de Saint-Exupéry
Ingrese el año: 1943
Ingrese la categoría: Fantasía
📘 Libro registrado exitosamente.
```

---

## 📌 Recomendaciones

- No edites manualmente `books.json` a menos que sepas lo que haces.
- Usa el ID de cada libro para prestar, devolver o eliminar.
- Siempre devuelve los libros antes de intentar eliminarlos.

---

## 👨‍💻 Autores

Desarrollado por Jerónimo, Mariana y Karina, como parte de un taller de programación en Python orientado a objetos y manipulación de archivos.

---

## 📝 Licencia

Este proyecto es de libre uso con fines educativos.
