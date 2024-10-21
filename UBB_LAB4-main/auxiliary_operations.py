def create_expense(expense_value, expense_type):
    """
    Funcție auxiliară care crează o nouă cheltuială
    """
    return (expense_value, expense_type)

def compute_total_expense(apartments, apartment_index):
    """
    Funcție auxiliară care calculează suma totală asociată unui apartament
    """

    total = 0
    for expense in apartments[apartment_index]:
        expense_value = expense[0]

        total += expense_value
    
    return total