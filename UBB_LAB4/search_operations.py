import auxiliary_operations
import add_operations

def search_apartments(apartments, search_value):
    """
    Funcție care modifică o anumită cheltuială pentru un apartament
    """

    valid_apartments = []
    for apartment_index in apartments.keys():
        if auxiliary_operations.compute_total_expense(apartments, apartment_index) > search_value:
            valid_apartments.append(apartment_index)

    return valid_apartments

def search_by_type(apartments, search_type):
    """
    Funcție care caută cheltuielile de un anumit tip de la toate apartamentele
    """

    valid_expenses = []
    for apartment_index in apartments.keys():
        apartment = apartments[apartment_index]

        if search_type not in apartment:
            add_operations.add(
                apartments,
                apartment_index,
                0,
                search_type
            )
        
        expense_value = auxiliary_operations.get_expense(
            apartments,
            apartment_index,
            search_type
        )

        valid_expenses.append(
            (apartment_index, expense_value)
        )


    return valid_expenses