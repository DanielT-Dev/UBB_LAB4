import add_operations
import auxiliary_operations

def menu():
    print()
    print("Meniu Principal")
    print("Pentru a adăuga o cheltuială la un apartament apasă tasta 1")
    print("Pentru a modifica o cheltuială la un apartament apasă tasta 2")
    print("Pentru a tipări toate apartamentele care au cheltuieli mai mari decât o sumă dată apasă tasta 3")
    print()

def search_apartments(apartments, search_value):
    """
    Funcție care modifică o anumită cheltuială pentru un apartament
    """

    valid_apartments = []
    for apartment_index in apartments.keys():
        if auxiliary_operations.compute_total_expense(apartments, apartment_index):
            valid_apartments.append(apartment_index)

    return valid_apartments

def run():
    apartments = {}

    while True:
        menu()

        command = int(input())

        match command:
            case 1:
                
                # Se cere input-ul de la utilizator
                apartment_index = int(input("Inserați numărul apartamentului: "))
                expense_value = int(input("Inserați suma asociată cheltuielii: "))
                expense_type = input("Inserați tipul asociat cheltuielii: ")

                # Se realizează operația de adăugare
                add_operations.add(
                    apartments,
                    apartment_index,
                    expense_value,
                    expense_type
                )

                print("Cheltuiala a fost adăugată.")

            case 2: 

                # Se cere input-ul de la utilizator
                apartment_index = int(input("Inserați numărul apartamentului: "))
                expense_value = int(input("Inserați suma asociată cheltuielii: "))
                expense_type = input("Inserați tipul asociat cheltuielii: ")

                # Se realizează operația de adăugare
                add_operations.update(
                    apartments,
                    apartment_index,
                    expense_value,
                    expense_type
                )

                print("Suma cheltuielii a fost modificată.")

            case 3:

                # Se cere input-ul de la utilizator
                search_value = int(input("Inserați suma pentru care doriți să realizați căutarea: "))

                # Se realizează operația de căutare 
                valid_apartments = search_apartments(apartments, search_value)

                print("Apartamentele care au cheltuieli mai mari decât suma dată sunt: ", valid_apartments)

run()