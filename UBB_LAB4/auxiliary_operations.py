def create_expense(apartments, apartment_index, expense_type):
    """
    Funcție auxiliară care crează o nouă cheltuială
    """
    apartments[apartment_index][expense_type] = 0

def get_expense(apartments, apartment_index, expense_type):
    """
    Funcție auxiliară care returnează suma unei cheltuieli
    """
    return apartments[apartment_index][expense_type]

def set_expense(apartments, apartment_index, expense_type, expense_value):
    """
    Funcție auxiliară care setează o nouă cheltuială
    """
    apartments[apartment_index][expense_type] = expense_value

def compute_total_expense(apartments, apartment_index):
    """
    Funcție auxiliară care calculează suma totală asociată unui apartament
    """

    total = 0
    for expense_value in apartments[apartment_index].values():
        total += expense_value
    
    return total