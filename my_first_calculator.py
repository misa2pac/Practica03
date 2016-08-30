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
    print("||  * Multiplicacion           ||")
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
                OP2 = float(input("Dame operador 2: "))
                RES = sumar_numeros(OP1,OP2)
    elif(opcion == '-'):
        if(BANDERA):
            OP1 = float(input("Dame operador 1: "))
            BANDERA = False
            if(BANDERA == False):
                OP2 = float(input("Dame operador 2: "))
                RES = resta_numeros(OP1,OP2)
    elif(opcion == '*'):
        if(BANDERA):
            OP1 = float(input("Dame operador 1: "))
            BANDERA = False
            if(BANDERA == False):
                OP2 = float(input("Dame operador 2:"))
                RES = multiplica_numeros(OP1,OP2)
    elif(opcion == '/'):
        if(BANDERA):
            OP1 = float(input("Dame operador 1: "))
            BANDERA = False
            if(BANDERA == False):
                OP2 = float(input("Dame operador 2: "))
                RES = divide_numeros(OP1,OP2)
    elif(opcion == 'r'):
        if (BANDERA):
            OP1 = float(input("Dame operador: "))
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
    elif(opcion == 's'):
        break
    else:
        print("Operacion no valida") 

def sumar_numeros(a,b):
    return a + b

def resta_numeros(a,b):
    return a - b

def divide_numeros(a,b):
    return a / b

def multiplica_numeros(a,b):
    return a * b