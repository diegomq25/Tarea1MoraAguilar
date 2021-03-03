def check_char(charr):
    if isinstance(charr, str):  # comprueba que el caracter agregado se string
        if len(charr) == 1:  # comprueba que la longitud del string sea uno
            if(charr.isalpha() == 1):  # Comprueba solo letras
                return 0
            else:
                return("ERROR: NO ES UN CARACTER EN RANGO A-Z")  # Error único
        else:
            return ("ERROR:CADENA MUY EXTENSA")  # Error único
    else:
        return ("ERROR: CARACTER NO ES STRING")  # Error único


def caps_switch(charr):
    if check_char(charr) == 0:  # comprueba que se cumpla "check_char"
        return charr.swapcase()  # Mayúscula a minúscula y viceversa
    else:
        return check_char(charr)  # si no retorna error único
