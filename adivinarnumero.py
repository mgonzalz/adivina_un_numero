#Elegir número
numero = int(input("Adivine el numero entre el 0 y el 99: "))
#Elección numero al azar
import random
numeroal = random.randint(0, 100)
numeroal = int(numeroal)
#Intento
while True:
    if numero == numeroal:
        print("¡Has acertado!")
        break
    elif numero < numeroal:
        print("Demasiado pequeño")
        numero = int(input("Adivine el numero entre el 0 y el 99: "))
    elif numero > numeroal:
        print("Demasiado grande")
        numero = int(input("Adivine el numero entre el 0 y el 99: "))
