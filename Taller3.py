# Ejercicio 2

# Pedir al usuario la cantidad de palabras
num_palabras = int(input("¿Cuántas palabras quieres agregar a la lista? "))

# Se crea una lista vacía
lista_palabras = []

# Se solicitan las palabras una por una y se agregan a la lista
for i in range(num_palabras):
    palabra = input(f"Escribe la palabra {i+1}: ")
    lista_palabras.append(palabra)

# Se muestra la lista de palabras
# Salida
print("La lista de palabras es:", lista_palabras)


# Ejercicio 3

# Se crea una lista vacía
lista_palabras = []

# Definir Cantidad de palabras
n_p = int(input("¿Cuántas palabras deseas ingresar? "))

# Ingresar palabras en la lista
for i in range(n_p):
    palabra = input(f"Ingresa la palabra {i+1}: ")
    lista_palabras.append(palabra)

# Pedir la palabra para buscar cuántas veces aparece
p_buscar = input("Ingresa la palabra que deseas buscar: ")

# Contar las veces que aparece la palabra
cantidad = lista_palabras.count(p_buscar)

# Salida
print(f"La palabra '{p_buscar}' aparece {cantidad} veces en la lista.")


# Ejercicio 4

# Se pidiò al usuario la cantidad de palabras
can_palabras = int(input("Ingresa la cantidad de palabras: "))
# Se crea una lista vacìa
lista_palabras = [0]
# Se hace un ciclo ya que se sabe la cantidad de palabras y se agrega la palabra en la lista
for _ in range(can_palabras):
    palabra = input("Ingresa una palabra: ")
    lista_palabras.append(palabra)
# Se crea la lista invertida o inversa
lista_invertida = lista_palabras[::-1]
# Salida
print("Lista original:", lista_palabras)
print("Lista invertida:", lista_invertida)


# Ejercicio 5

# Definir el diccionario con los precios de las frutas
precios_frutas = { 'platano': 1.35, 'manzana': 0.80, 'pera': 0.85, 'naranja': 0.70}

# Solicitar al usuario el nombre de la fruta y la cantidad de kilos
fruta = input("Introduce el nombre de la fruta: ").strip().lower()
kilos = float(input("Introduce el número de kilos: "))

# Verificar si la fruta está en el diccionario
if fruta in precios_frutas:
    precio_por_kilo = precios_frutas[fruta]
    precio_total = precio_por_kilo * kilos
    print(f"El precio de {kilos} kilos de {fruta} es {precio_total:.2f} euros.")
else:
    print("La fruta que has introducido no está en el diccionario.")



# Ejercicio 6

compra = {}

while True:
    articulo = input("Ingresa el nombre del artículo (o escribe 'terminar' para finalizar): ").capitalize()

    if articulo.lower() == 'terminar':
        break

    precio = float(input(f"Ingrese el precio de {articulo}: "))

    compra[articulo] = precio

print("\nLista de compra")
for articulo, precio in compra.items():
    print(f"{articulo:20} {precio:.2f} euros")

coste_total = sum(compra.values())
print(f"\nTotal: {coste_total:.2f} euros")


# Ejercicio 7

# multiplicador.py

def imprimir_tabla_multiplicar(x):
    """
    Imprime la tabla de multiplicar del número x hasta el 10.

    x: Número del cual se quiere imprimir la tabla de multiplicar
    """
    for i in range(1, 11):
         print(f"{x} x {i} = {x * i}")

# Número que se quiere imprimir de la tabla de multiplicar
numero = 5  # Puedes cambiar este número a cualquier otro valor, en mi caso es 5

# Llamada a la función
imprimir_tabla_multiplicar(numero)






