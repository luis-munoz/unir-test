# pylint: disable=no-else-return
def convert_to_number(operand):
    try:
        if "." in operand:
            return float(operand)
        else:
            return int(operand)

    except ValueError:
        raise TypeError("Operator cannot be converted to number")

#Actualmente no utilizada
def InvalidConvertToNumber(operand):
    try:
        if "." in operand:
            return (float(operand))

        return int(operand)

    except ValueError:
        raise TypeError("Operator cannot be converted to number")

#Se eliminó su uso ya que actualmente no se tiene usuarios ni métodos de autenticación
def validate_permissions(operation, user):
    print(f"checking permissions of {user} for operation {operation}")
    return user == "user1"
