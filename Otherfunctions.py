import random
import string

#Para generar el id del nuevo usuario
def get_dni(username):
    dni = ''.join((random.choice(str(username) + string.digits) for i in range(34)))
    return dni
