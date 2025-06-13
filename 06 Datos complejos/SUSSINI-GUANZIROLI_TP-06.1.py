#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
precios_frutas["Naranja"] = 1200 
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800
precios_frutas['Banana'] = 1330 #aumento de 130 pesos
precios_frutas['Manzana'] = 1700
precios_frutas['Pera'] = 2800
print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios
frutas = precios_frutas.keys()
print(frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
#Ejemplo:
mis_contactos = {} #iniciamos y esta vacio
def agregar_contacto(nombre, numero):
    mis_contactos[nombre] = numero
    return mis_contactos
def buscar_contacto(nombre):
    contacto_buscado = mis_contactos[nombre]
    return print(f"El numero del contacto buscado es: {contacto_buscado}")
for i in range (0,5):
    agregar_contacto(input('\nIngrese el nombre del contacto: '), int(input("ingrese el numero del contacto: ")))
buscar_contacto(input("\nIngrese el nombre del contacto a buscar: "))

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.
frase_larga = input("Usuario, introduzca una frase que le guste!: ")
palabras = frase_larga.split(' ')
palabras_set = set(palabras)
contar_palabras = {} #armo el dicc vacio
for palabra in palabras:
    if palabra in contar_palabras:
        contar_palabras[palabra] += 1
    else:
        contar_palabras[palabra] = 1
print("Palabras unicas: ", palabras_set)
print("Repeticion de palabras: ", contar_palabras)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.
alumnos = {}
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i + 1}: ")    
    while True:
        notas = input(f"Ingresá 3 notas separadas por espacios para {nombre}: ")
        notas_tupla = tuple(map(int, notas.split()))        
        if len(notas_tupla) == 3:
            break
    alumnos[nombre] = notas_tupla
print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: {promedio:.2f}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
aprobados_p1 = {'Juan', 'María', 'Carlos', 'Lucía', 'Pedro'}
aprobados_p2 = {'María', 'Pedro', 'Ana', 'Luis', 'Carlos'}
print("Aprobaron ambos:", aprobados_p1 & aprobados_p2)
print("Solo uno:", aprobados_p1 ^ aprobados_p2)
print("Total aprobados:", aprobados_p1 | aprobados_p2)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.
stock = {'yerba': 50, 'azúcar': 30, 'fideos': 40, 'arroz': 25}
while True:
    print("\n1-Consultar | 2-Agregar stock | 3-Agregar producto | 4-Salir")
    op = input("Opción: ")
    if op == '1':
        prod = input("Producto a consultar: ").lower()
        print(f"Stock: {stock.get(prod, 'No existe')}")
    elif op == '2':
        prod = input("Producto: ").lower()
        if prod in stock:
            cant = int(input("Unidades a agregar: "))
            stock[prod] += cant
            print(f"Nuevo stock de {prod}: {stock[prod]}")
        else:
            print("Producto no existe. Usá opción 3 para agregarlo")
    elif op == '3':
        prod = input("Nuevo producto: ").lower()
        if prod not in stock:
            cant = int(input("Stock inicial: "))
            stock[prod] = cant
            print(f"Producto '{prod}' agregado con {cant} unidades")
        else:
            print("¡El producto ya existe!")
    elif op == '4':
        print("¡Chau! Stock final:", stock)
        break   
    else:
        print("Opción inválida. Elegí 1, 2, 3 o 4")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.
agenda = {
    ('lunes', '10:00'): 'Reunión con el equipo',
    ('miércoles', '15:30'): 'Entrevista de trabajo',
    ('viernes', '09:00'): 'Desayuno con clientes'
}
while True:
    print("\n1-Consultar evento | 2-Agregar evento | 3-Salir")
    op = input("Opción: ").strip()   
    if op == '1':
        dia = input("Día (ej: lunes): ").lower()
        hora = input("Hora (ej: 14:30): ")
        evento = agenda.get((dia, hora), 'No hay nada agendado')
        print(f"Evento: {evento}")
    elif op == '2':
        dia = input("Día (ej: martes): ").lower()
        hora = input("Hora (ej: 16:00): ")
        evento = input("Evento: ")
        agenda[(dia, hora)] = evento
        print(f"Evento agregado: {dia} {hora} - {evento}")
    elif op == '3':
        print("Agenda guardada. Chau!")
        break
    else:
        print("Opción inválida. Elegí 1, 2 o 3")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.
paises = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
    'Paraguay': 'Asunción'
}
#se invierte
capitales = {capital: pais for pais, capital in paises.items()}
print("Diccionario original:")
print(paises)
print("\nDiccionario invertido:")
print(capitales)