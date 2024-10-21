import auxiliary_operations

def delete_by_apartment(apartments, apartment_index):
    """
    Funcție care șterge toate cheltuielile de la un apartament
    """

    apartments[apartment_index] = {}

def delete_by_range(apartments, left_apartment, right_apartment):
    """
    Funcție care șterge toate cheltuielile de la un interval de apartamente
    """

    for i in range(left_apartment, right_apartment + 1):
        delete_by_apartment(apartments, i)
    
def delete_by_type(apartments, search_type):
    """
    Funcție care șterge un anumit tip de cheltuială de la toate apartamentele
    """

    for apartment_index in apartments.keys():
        if search_type in apartments[apartment_index]:
            auxiliary_operations.set_expense(
                apartments,
                apartment_index,
                search_type,
                0
            )