import math
# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too
# Editada por Misael Saenz Flores

BANDERA = True
RES = 0.0

while (True):
    print("=================================")
    print("===========Calculadora===========")
    print("=================================")
    print("||  + Suma                     ||")
    print("||  - Resta                    ||")
    print("||  / Division                 ||")
    print("||  r Raiz                     ||")
    print("||  = Resutado                 ||")
    print("||  s Salir                    ||")
    print("=================================")
    opcion = input("Escribe una opcion: ")
    if(opcion == '+'):
        if(BANDERA):
            OP1 = int(input("Dame operador 1: "))
            BANDERA = False
            if(BANDERA == False):
                OP2 = int(input("Dame operador 2: "))
                RES = OP1 + OP2
    elif(opcion == '-'):
        if(BANDERA):
            OP1 = int(input("Dame operador 1: "))
            BANDERA = False
            if(BANDERA == False):
                OP2 = int(input("Dame operador 2: "))
                RES = OP1 - OP2
    elif(opcion == '/'):
        if(BANDERA):
            OP1 = int(input("Dame operador 1: "))
            BANDERA = False
            if(BANDERA == False):
                OP2 = int(input("Dame operador 2: "))
                RES = OP1/OP2
    elif(opcion == 'r'):
        if (BANDERA):
            OP1 = int(input("Dame operador: "))
            BANDERA = False
            if(BANDERA == False):
                RES = math.sqrt(OP1)
    elif(opcion == '='):
        if(BANDERA):
            print("Nada que mostrar!")
        else:
            print("El resultado es: " + str(RES))
            BANDERA = True
            RES = 0.0
        pass        