import add_operations
import delete_operations
import search_operations
import auxiliary_operations

def menu():
    print()
    print("Meniu Principal")
    print("Pentru a adăuga o cheltuială la un apartament apasă tasta 1")
    print("Pentru a modifica o cheltuială la un apartament apasă tasta 2")
    print("Pentru a tipări toate apartamentele care au cheltuieli mai mari decât o sumă dată apasă tasta 3")
    print("Pentru a tipări cheltuielile de un anumit tip de la toate apartamentele apasă tasta 4")
    print("Pentru a șterge toate cheltuielile de la un apartament apasă tasta 5")
    print("Pentru a șterge toate cheltuielile de la apartamente consecutive apasă tasta 6")
    print("Pentru a șterge cheltuielile de un anumit tip de la toate apartamentele apasă tasta 7")
    print()

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

                print("\nSuma cheltuielii a fost modificată. \n")

            case 3:

                # Se cere input-ul de la utilizator
                search_value = int(input("Inserați suma pentru care doriți să realizați căutarea: "))

                # Se realizează operația de căutare 
                valid_apartments = search_operations.search_apartments(apartments, search_value)

                print("\nApartamentele care au cheltuieli mai mari decât suma dată sunt: ", valid_apartments, "\n")

            case 4:

                # Se cere input-ul de la utilizator
                search_type = input("Inserați tipul de cheltuială pentru care doriți să realizați căutarea: ")

                # Se realizează operația de căutare 
                valid_expenses = search_operations.search_by_type(apartments, search_type)

                print()

                for expense in valid_expenses:
                    apartment_index = expense[0]
                    expense_value = expense[1]

                    print("Apartamentul cu numărul", apartment_index, "are o cheltuială de", expense_value, "la", search_type)
                
                print()
            
            case 5:

                # Se cere input-ul de la utilizator
                apartment_index = int(input("Inserați numărul apartamentului: "))

                delete_operations.delete_by_apartment(apartments, apartment_index)

                print("\nCheltuielile de la apartamentul cu numărul", apartment_index, "au fost șterse\n")

            case 6:

                # Se cere input-ul de la utilizator
                apartment_index1 = int(input("Inserați numărul primului apartament "))
                apartment_index2 = int(input("Inserați numărul celui de al doilea apartament "))

                delete_operations.delete_by_range(apartments, apartment_index1, apartment_index2)

                print("\nCheltuielile de la apartamentele din intervalul", apartment_index1, " -> ", apartment_index2, "au fost șterse\n")

            case 7:

                # Se cere input-ul de la utilizator
                search_type = int(input("Inserați tipul de cheltuială pentru care doriți să realizați ștergerea: "))

                delete_operations.delete_by_type(apartments, search_type)

                print("\nCheltuielile de tip", search_type, "au fost șterse\n")

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

    add_operations.update(
        apartments,
        2,
        7,
        "curent"
    )

    assert search_operations.search_apartments(
        apartments,
        8
    ) == [1, 3]
    assert search_operations.search_apartments(
        apartments,
        17
    ) == [3]
    assert search_operations.search_apartments(
        apartments,
        25
    ) == []

    assert search_operations.search_by_type(
        apartments,
        "apă"
    ) == [(1, 10), (2, 0), (3, 20)]
    assert search_operations.search_by_type(
        apartments,
        "curent"
    ) == [(1, 0), (2, 7), (3, 0)]
    assert search_operations.search_by_type(
        apartments,
        "gaz"
    ) == [(1, 0), (2, 0), (3, 0)]


    print("Aplicația a fost testată")

test()

run()