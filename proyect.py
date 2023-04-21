import random

numero = random.randint(100, 999)
print(numero)

unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

def numero_a_palabras(numero):
    centena = numero // 100
    decena = (numero % 100) // 10
    unidad = numero % 10

    if centena == 1 and decena == 0 and unidad == 0:
        return "cien"
    elif decena == 1:
        if unidad == 0:
            return "diez"
        elif unidad == 1:
            return "once"
        elif unidad == 2:
            return "doce"
        elif unidad == 3:
            return "trece"
        elif unidad == 4:
            return "catorce"
        elif unidad == 5:
            return "quince"
        else:
            return decenas[decena] + " y " + unidades[unidad]
    elif decena == 0 and unidad == 0:
        return centenas[centena]
    elif decena == 0:
        return centenas[centena] + " " + unidades[unidad]
    elif unidad == 0:
        return centenas[centena] + " " + decenas[decena]
    else:
        return centenas[centena] + " " + decenas[decena] + " y " + unidades[unidad]
respuesta = input("Ingresa el número en palabras: ")

if respuesta.lower() == numero_a_palabras(numero).lower():
    print("¡Correcto!")
else:
    print("Incorrecto. El número era:", numero, "(", numero_a_palabras(numero), ")")
