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
        if auxiliary_operations.compute_total_expense(apartments, apartment_index) > search_value:
            valid_apartments.append(apartment_index)

    return valid_apartments

apartments = {}

def run():
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

                print("\n Cheltuiala a fost adăugată. \n")

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

                print("\n Suma cheltuielii a fost modificată. \n")

            case 3:

                # Se cere input-ul de la utilizator
                search_value = int(input("Inserați suma pentru care doriți să realizați căutarea: "))

                # Se realizează operația de căutare 
                valid_apartments = search_apartments(apartments, search_value)

                print("\n Apartamentele care au cheltuieli mai mari decât suma dată sunt: ", valid_apartments, "\n")

def test():
    print()
    print("Se testează aplicația")

    add_operations.add(
        apartments,
        1,
        10,
        "apă"
    )
    add_operations.add(
        apartments,
        2,
        15,
        "curent"
    )
    add_operations.add(
        apartments,
        3,
        20,
        "apă"
    )

    search_apartments(
        apartments,
        8
    )

    add_operations.update(
        apartments,
        2,
        7,
        "curent"
    )

    assert search_apartments(
        apartments,
        8
    ) == [1, 3]
    assert search_apartments(
        apartments,
        17
    ) == [3]
    assert search_apartments(
        apartments,
        25
    ) == []

    print("Aplicația a fost testată")

test()

run()