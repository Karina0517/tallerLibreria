from datetime import date
from utils import get_new_id, input_date, save_books, books
from validations import *
from validations import prompt_until_valid, validate_alpha

# Registers a new book in the library
def register_book():
    print("\n📝 Registrar nuevo libro")

    while True:
        title = input("📖 Título: ").strip().title()
        if title:
            break
        print("⚠️ El título no puede estar vacío.")

    author = prompt_until_valid("👤 Autor: ", validate_alpha, "❌ Autor inválido (solo letras y espacios).").title()

    while True:
        year_input = input("📅 Año de publicación: ").strip()
        if validate_year(year_input):
            year = int(year_input)
            break
        else:
            print(f"❌ Solo se permite entre 1500 y {date.today().year}.")

    categories = ['Ficción', 'No Ficción', 'Infantil', 'Educativo']
    while True:
        print("📂 Seleccione una categoría:")
        for idx, cat in enumerate(categories, 1):
            print(f"{idx}. {cat}")
        cat_option = input("👉 Opción: ").strip()
        if cat_option.isdigit() and 1 <= int(cat_option) <= len(categories):
            category = categories[int(cat_option) - 1]
            break
        else:
            print("❌ Opción de categoría inválida.")

    book = {
        "id": get_new_id(books),
        "title": title,
        "author": author,
        "year": year,
        "category": category,
        "status": "Disponible"
    }

    books.append(book)
    save_books()
    print("✅ Libro registrado exitosamente.")

# Lists all books with optional filtering by availability status
def list_books():
    print("\n📋 Filtrar por estado:")
    print("1️⃣ Todos")
    print("2️⃣ Disponible")
    print("3️⃣ Prestado")
    while True:
        option = input("👉 Seleccione una opción: ").strip()
        if option in ["1", "2", "3"]:
            break
        print("❌ Opción inválida.")

    if option == "2":
        filtered = [b for b in books if b["status"] == "Disponible"]
    elif option == "3":
        filtered = [b for b in books if b["status"] == "Prestado"]
    else:
        filtered = books

    if not filtered:
        print("📭 No hay libros para mostrar.")
        return

    for b in filtered:
        print("\n📕--------------------------")
        print(f"🆔 ID: {b['id']}")
        print(f"📖 Título: {b['title']}")
        print(f"👤 Autor: {b['author']}")
        print(f"📅 Año: {b['year']}")
        print(f"📚 Categoría: {b['category']}")
        print(f"🔖 Estado: {b['status']}")
        if b['status'] == "Prestado":
            p = b.get("prestamo", {})
            print(f"🙋 Prestado a: {p.get('nombre', 'Desconocido')} el {p.get('fecha', 'Desconocida')}")
        print("📕--------------------------")

# Searches books by title, author, or category
def search_books():
    print("\n🔍 Buscar libros")
    while True:
        query = input("🔎 Buscar por título, autor o categoría: ").strip().lower()
        if query:
            break
        print("⚠️ Debe ingresar algún criterio de búsqueda.")

    results = [
        b for b in books
        if query in b["title"].lower()
        or query in b["author"].lower()
        or query in b["category"].lower()
    ]

    if not results:
        print("🚫 No se encontraron libros.")
        return

    for b in results:
        print("\n📘--------------------------")
        print(f"🆔 ID: {b['id']}")
        print(f"📖 Título: {b['title']}")
        print(f"👤 Autor: {b['author']}")
        print(f"📅 Año: {b['year']}")
        print(f"📚 Categoría: {b['category']}")
        print(f"🔖 Estado: {b['status']}")
        if b['status'] == "Prestado":
            p = b.get("prestamo", {})
            print(f"🙋 Prestado a: {p.get('nombre', 'Desconocido')} el {p.get('fecha', 'Desconocida')}")
        print("📘--------------------------")

# Lends a book to a borrower
def lend_book():
    id_input = input("📌 Ingrese el ID del libro a prestar: ").strip()
    if not id_input.isdigit():
        print("❌ ID inválido.")
        return
    book_id = int(id_input)

    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        print("📭 Libro no encontrado.")
        return
    if book["status"] == "Prestado":
        print("⚠️ Este libro ya está prestado.")
        return

    borrower = prompt_until_valid("🙋 Nombre del prestatario: ", validate_alpha, "❌ Nombre inválido.")
    book["status"] = "Prestado"
    book["prestamo"] = {
        "nombre": borrower,
        "fecha": input_date()
    }
    save_books()
    print("📤 Libro prestado exitosamente.")

# Returns a book (marks it as available again)
def return_book():
    id_input = input("📌 Ingrese el ID del libro a devolver: ").strip()
    if not id_input.isdigit():
        print("❌ ID inválido.")
        return
    book_id = int(id_input)

    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        print("📭 Libro no encontrado.")
        return
    if book["status"] == "Disponible":
        print("✅ Este libro ya está disponible.")
        return

    book["status"] = "Disponible"
    book.pop("prestamo", None)
    save_books()
    print("📥 Libro devuelto exitosamente.")

# Displays a list of all books currently on loan
def show_lent_books():
    lent_books = [b for b in books if b["status"] == "Prestado"]
    if not lent_books:
        print("📭 No hay libros prestados.")
        return

    for b in lent_books:
        print("\n📘--------------------------")
        print(f"🆔 ID: {b['id']}")
        print(f"📖 Título: {b['title']}")
        print(f"🙋 Prestado a: {b['prestamo']['nombre']}")
        print(f"📅 Fecha de préstamo: {b['prestamo']['fecha']}")
        print("📘--------------------------")

# Deletes a book by ID from the collection
def delete_book():
    id_input = input("🗑️ Ingrese el ID del libro a eliminar: ").strip()
    if not id_input.isdigit():
        print("❌ ID inválido.")
        return
    book_id = int(id_input)

    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        print("📭 Libro no encontrado.")
        return

    if book["status"] == "Prestado":
        print("⚠️ No se puede eliminar un libro que está prestado.")
        return

    books.remove(book)
    save_books()
    print("✅ Libro eliminado exitosamente.")
