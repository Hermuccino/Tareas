matriz = [ [10, 15, 20], [3, 7, 14] ]
matriz[1][0] = 6

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]['nombre'] = 'Enrique Martin Morales'

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades['México'][2] = 'Monterrey'

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]['longitud'] = 9.9355431

def iterarDiccionario(lista):
    for diccionario in lista:
        datos = [f"{clave} - {valor}" for clave, valor in diccionario.items()]
        print(', '.join(datos))

iterarDiccionario(cantantes)
print()

def iterarDiccionario2(llave,lista):
    for diccionario in lista:
        print(diccionario[llave])

iterarDiccionario2('nombre',cantantes)
iterarDiccionario2('pais', cantantes)
print()

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for item in lista:
            print(item)
        print()

imprimirInformacion(ciudades)





