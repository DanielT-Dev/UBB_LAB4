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
        apartments[apartment_index] = {}

    if expense_type not in apartments[apartment_index]:
        auxiliary_operations.create_expense(
            apartments,
            apartment_index,
            expense_type
        )

    previous_expense_value = auxiliary_operations.get_expense(
        apartments,
        apartment_index,
        expense_type
    )

    new_expense_value = previous_expense_value + expense_value

    auxiliary_operations.set_expense(
        apartments,
        apartment_index,
        expense_type,
        new_expense_value,
    )

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

    auxiliary_operations.set_expense(
        apartments,
        apartment_index,
        expense_type,
        expense_value,
    )