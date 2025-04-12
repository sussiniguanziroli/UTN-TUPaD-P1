#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea
for i in range(0,101):
    print(f"{i}")
print("Adios")

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
numero_entero = int(input("Ingrese un numero entero: "))
if numero_entero == 0:
    print("El numero 0 tiene 1 digito.")
else:
    temp = abs(numero_entero)
    contador = 0
    while temp > 0:
        temp = temp // 10
        contador += 1
    print(f"El numero {numero_entero} tiene {contador} digitos.")
print("Fin del programa")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
numero1 = int(input("Ingrese el primer numero entero: "))
numero2 = int(input("Ingrese el segundo numero entero: "))
sumatoria = 0
inicio = min(numero1, numero2)
fin = max(numero1, numero2)
for i in range(inicio, fin):
    sumatoria += i
print(f"La suma de los numeros entre {numero1} y {numero2} es: {sumatoria}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
sumatoria = 0
trigger = 0
while True:
    num = int(input("Ingrese un numero entero: "))
    if num == trigger:
        break
    sumatoria += num
print(f"El total de los numeros sumados es: {sumatoria}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numero_rnd = random.randint(0, 9)
intentos = 0
adivinado = False
print("Adivinar el numero entre 0 y 9: ")
while not adivinado:
    intento = int(input("Tu intento:"))
    intentos += 1
    if intento == numero_rnd:
        print(F"Correcto! El numero era {numero_rnd}")
        adivinado = True
    elif intento < 0 or intento > 9:
        print("Incorrecto, ingresa un numero valido.")
    else:
        print("Incorrecto, intenta nuevamente.")
print(f"Lo lograste en {intentos} intento(s).")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(f"{i}")
print("Chau")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
limite_superior = int(input("Ingrese un numero entero positivo: "))
sumatoria = 0
for i in range(0, limite_superior + 1):
    sumatoria += i
print(f"La suma de los numeros entre 0 y {limite_superior} es: {sumatoria}")
print("Fin")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos.
cantidad_numeros = 100 
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i+1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print("Fin")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
cantidad_numeros = 100 #cambiar para probar con menos numeros
suma_total = 0
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma_total += numero
media = suma_total / cantidad_numeros
print(f"La media de los {cantidad_numeros} números ingresados es: {media}")
print("Fin")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745
numero = int(input("Ingrese un número entero: "))
numero_abs = abs(numero)
invertido = 0
while numero_abs > 0:
    digito = numero_abs % 10
    invertido = invertido * 10 + digito
    numero_abs //= 10
if numero < 0:
    invertido *= -1
print(f"El número invertido es: {invertido}")
print("Fin")