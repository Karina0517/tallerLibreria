# 📚 Proyecto: Sistema de Inventario de Librería


¡Bienvenidos al sistema de gestión de libros de nuestra librería! Este programa en Python permite registrar, listar, buscar, prestar y devolver libros utilizando estructuras de datos como listas y diccionarios. 💪🐍

---

## 👥 Equipo de Desarrollo

Este proyecto fue desarrollado por:

- 👤 Mariana Restrepo Acevedo
- 👤 Jerónimo Gutiérrez Arias
- 👤 Karina Andrea Henao Zuleta

---

## 🎯 Objetivo

Crear una aplicación de consola modular y validada que administre un inventario de libros, con operaciones CRUD básicas y gestión de préstamos 📖🔁.

---

## ✅ Funcionalidades Principales

1. 📌 **Registrar libros**
   - ID autogenerado 🆔
   - Título, autor y año de publicación obligatorios ✍️📅
   - Categorías disponibles: `Ficción`, `No Ficción`, `Infantil`, `Educativo` 📗📘📙📕

2. 📋 **Listar todos los libros**
   - Mostrar todos los libros en formato tabla 📊
   - Permitir filtrar por estado (Disponible o Prestado) ✅🚫

3. 🔍 **Buscar libros**
   - Por título, autor o categoría 🔠

4. 📤 **Prestar libros**
   - Validación de disponibilidad
   - Registro de nombre de la persona y fecha de préstamo 🧑📆
   - Límite de 3 libros por persona ❗

5. 📥 **Devolver libros**
   - Cambiar estado a "Disponible" y eliminar registro de préstamo 🔁

6. 📚 **Mostrar libros prestados**
   - Con nombre del lector y fecha del préstamo 🧾

7. 🗑️ **Eliminar libros**
   - Solo si están disponibles ❌

---

## 🛡️ Validaciones y Restricciones

- Entradas obligatorias validadas ✏️
- Uso de listas y diccionarios correctamente 📦
- Código modular dividido en funciones 🧩
- Sin errores por entradas vacías o incorrectas 🧼

---

## 💡 Bonus (Opcional)

- Exportar lista de libros a `.json` o `.csv` 🗃️
- Persistencia de datos entre ejecuciones 💾
- Estadísticas por categoría, libros prestados y disponibles 📈

---
## 🧠 Sugerencias Técnicas

- Emplear `input()` y `print()` de forma efectiva.
- Usar `datetime.date.today()` para registrar fechas.
- Crear un menú principal con `while` para manejar las opciones del sistema 🔁.
