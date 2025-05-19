from features import *
from validations import validate_option
from utils import load_books, save_books

# Displays the main menu and handles user interaction
def main_menu():
    while True:
        print("\nMenú Principal")
        print("1. Registrar libro")
        print("2. Listar libros")
        print("3. Buscar libros")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Mostrar libros prestados")
        print("7. Eliminar libro")
        print("8. Salir")

        # Get user input and validate option
        option = input("Seleccione una opción: ")
        if not validate_option(option, 1, 8):
            print("Opción inválida.")
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
            print("Hasta luego.")
            save_books()  # Save any changes before exiting
            break

# Entry point of the application
if __name__ == "__main__":
    load_books()  # Load data before starting menu
    main_menu()

