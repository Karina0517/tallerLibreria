from features import *
from validations import validate_option
from utils import load_books, save_books

# Displays the main menu and handles user interaction
def main_menu():
    while True:
        print("\n📚 Menú Principal 📚")
        print("1️⃣  Registrar libro")
        print("2️⃣  Listar libros")
        print("3️⃣  Buscar libros")
        print("4️⃣  Prestar libro")
        print("5️⃣  Devolver libro")
        print("6️⃣  Mostrar libros prestados")
        print("7️⃣  Eliminar libro")
        print("8️⃣  Salir")

        # Get user input and validate option
        option = input("👉 Seleccione una opción: ")
        if not validate_option(option, 1, 8):
            print("❌ Opción inválida.")
            continue

        # Execute the corresponding function based on user choice
        option = int(option)
        if option == 1:
            register_book()
        elif option == 2:
            list_books()
        elif option == 3:
            search_books()
        elif option == 4:
            lend_book()
        elif option == 5:
            return_book()
        elif option == 6:
            show_lent_books()
        elif option == 7:
            delete_book()
        elif option == 8:
            print("👋 Hasta luego.")
            save_books()  # Save any changes before exiting
            break

# Entry point of the application
if __name__ == "__main__":
    load_books()  # Load data before starting menu
    main_menu()