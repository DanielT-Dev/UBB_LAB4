import auxiliary_operations

def add(
    apartments, 
    apartment_index, 
    expense_value, 
    expense_type
):
    """
    Funcție care adaugă o nouă cheltuială pentru un apartament
    """

    if apartment_index not in apartments:
        apartments[apartment_index] = []

    expense = auxiliary_operations.create_expense(expense_value, expense_type)

    apartments[apartment_index].append(expense)

def update(
    apartments, 
    apartment_index, 
    expense_value, 
    expense_type
):
    """
    Funcție care modifică o anumită cheltuială pentru un apartament
    """

    if apartment_index not in apartments:
        print("Apartamentul nu este înregistrat")

    apartments[apartment_index][expense_type] = expense_value