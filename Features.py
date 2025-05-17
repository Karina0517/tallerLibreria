#IMPORTAR datetime, ramdom
import json
import datetime
from Validations import validate_string, validate_number, validate_name, validate_year

#Aquí se harán los requerimientos funcionales
JSON = 'Library.json'
books = []

#1. Registro de libros con lista y diccionario //Por defecto disponible // Validar que sea mayor al año 1500


def book_record():
    print ("\nBook record 📖 ")
    title = validate_string("Enter the book name: ")
    author = validate_name("Enter the author name: ")
    year = validate_year("Enter year of publication (>=1500): ")
    category = validate_name("Enter the category: ")
    
    inventory = {
        'id': generate_id(),
        'Title': title,
        'Author' : author,
        'Year' : year,
        'Category' : category,
        'State' : 'Available'
    }
    books.append(inventory)
    
    return f" ✅ '{title}' has been added successfully "


#Generar ID

def generate_id(counter_id = [1]):
    id_actual = counter_id[0]
    counter_id[0] += 1
    return id_actual
    
#2. Listar todos los libros

def list_boooks():
    state = input("Filter by status? [A] Available / [L] Loaned / [] Enter for all )").upper()
    while state != "A" or state != "L" or state != "":
        print("🔴 Error, you must enter [A], [L] or [Enter]. Try again 🔴")
        state = input("Filter by status? [A] Available / [L] Loaned / [] Enter for all )").upper()
    filter = [sta for sta in books if state == '' or sta['State'] == state]

#3. Buscar libros //Filtrar por estado también // Por título, autor o categoría (búsqueda parcial, sin distinguir mayúsculas).

#4. Prestar libro

#5. Devolver libro // Validar que el libro estaba prestado.

#6. Mostrar libros prestados //Mostrar libros actualmente prestados junto con: Persona que lo tiene y Fecha de préstamo

#7. Eliminar un libro // Solo si no está prestado
