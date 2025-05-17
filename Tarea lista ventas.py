ventas = [{'fecha':'2025-01-01',  #se crea una lista de diccionarios con las ventas
                'producto':'Bdja uva 8,2 kg 608x406x123', 
                'cantidad': 50000,
                'precio': 1.08 },

                {'fecha':'2025-02-02', 
                'producto':'Bdja uva 5 kg 600x400X100', 
                'cantidad': 100000,
                'precio': 0.95 },

                {'fecha':'2025-03-02', 
                'producto':'Bdja uva 8,2 kg 508x406X123', 
                'cantidad': 30000,
                'precio': 1.01 },

                {'fecha':'2025-04-03', 
                'producto':'Parrilla interconectora citricos', 
                'cantidad': 8000,
                'precio': 1.45 },

                {'fecha':'2025-04-03', 
                'producto':'Parrilla interconectora citricos', 
                'cantidad': 3000,
                'precio': 1.70},

                {'fecha':'2025-04-13', 
                'producto':'Bdja uva 5 kg 600x400X100', 
                'cantidad': 40000,
                'precio': 0.97},

                {'fecha':'2025-05-21', 
                'producto':'Bdja uva 5 kg 600x400X100', 
                'cantidad': 10000,
                'precio': 0.97},

                {'fecha':'2025-05-17', 
                'producto':'Bdja citricos 15kg 608x406X162', 
                'cantidad': 50000,
                'precio': 1.6},

                {'fecha':'2025-05-17', 
                'producto':'Bdja citricos 15kg 608x406X162', 
                'cantidad': 40000,
                'precio': 1.6},

                {'fecha':'2025-05-17', 
                'producto':'Bdja citricos 15kg 608x406X162', 
                'cantidad': 100000,
                'precio': 1.49} ]



#Calculo de ingresos totales
def ingresos_totales(lista): #Defino una funcion para una lista de diccionarios
    total = 0 #Estoy buscando el total de los ingresos de los diccionarios
    for diccionario in lista: #Para cada diccionario de la lista
        total += diccionario['cantidad'] * diccionario['precio'] #Quiero que se agregue a la variable total la multiplicacion de la cantidad por el precio
    return f"Ingresos totales : ${int(total)}" #Quiero que me entregue una string con el valor sin decimales añadiendo el signo $

print(ingresos_totales(ventas))



#Análisis del Producto Más Vendido
ventas_por_producto = {} #Se crea un diccionario que se llama ventas por producto
for diccionario in ventas: #para cada diccionario que esta en la lista ventas
    producto = diccionario['producto'] #se designa una variable producto que corresponde al valor de la clave producto
    cantidad = diccionario['cantidad'] #se designa una variable cantidad que corresponde al valor de la clave cantidad
    if producto in ventas_por_producto: #se crea una condicion en la iteracion para crear el diccionario donde la variable producto se encuentra dentro del diccionario ventas_por_producto 
        ventas_por_producto[producto] += cantidad #si ya se creo una clave valor del producto en el diccionario ventas_por_producto, se debe sumar la cantidad
    else: #en caso opuesto
        ventas_por_producto[producto] = cantidad #solo se crea una clave valor donde el producto tiene su cantidad inicial

print(ventas_por_producto) #Se comprueba creacion del diccionario

mejor_producto = max(ventas_por_producto, key=ventas_por_producto.get) #Se busca el producto con la mayor cantidad vendida usando la funcion maximo, con el parametro key con el diccionario.get para poder comparar los valores de las claves
cantidad_mejor_producto = ventas_por_producto[mejor_producto] #Para visualizar el producto con su cantidad respectiva, se crea una variable que llama al valor de la clave del mejor producto
print(f"El producto mas vendido es {mejor_producto} con {cantidad_mejor_producto} unidades") #Se imprime una string que contiene el mejor producto seguido de su cantidad



#Calculando promedio de precio por producto
precios_por_producto = {}  # Diccionario para almacenar suma de ingresos y cantidad total

for diccionario in ventas:# se itera sobre cada diccionario en la lista de ventas
    producto = diccionario['producto'] # nombre del producto
    cantidad = diccionario['cantidad'] # cantidad vendida
    precio = diccionario['precio'] # precio por unidad
    ingreso = precio * cantidad  # es la suma de todos los precios por la cantidad vendida

    if producto in precios_por_producto:# si el producto ya está en el diccionario
        suma_ingresos, suma_cantidades = precios_por_producto[producto] # obtener la suma de ingresos y cantidades
        precios_por_producto[producto] = (suma_ingresos + ingreso, suma_cantidades + cantidad) # actualizar la suma de ingresos y cantidades
    else:# si el producto no está en el diccionario
        precios_por_producto[producto] = (ingreso, cantidad) # agregar el producto con su ingreso y cantidad inicial

print(precios_por_producto) # se imprime el diccionario con los ingresos y cantidades por producto


# Calcular y mostrar el precio promedio de venta por producto
for producto, (suma_ingresos, suma_cantidades) in precios_por_producto.items():# iterar sobre cada producto y sus ingresos y cantidades
    promedio = suma_ingresos / suma_cantidades # calcular el precio promedio
    print(f"El precio promedio de {producto} es ${round(promedio, 2)}") # imprimir el precio promedio redondeado a 2 decimales

#Ingresos por dia
ingresos_por_dia = {} #Se crea un diccionario que se llama ingresos por dia
for diccionario in ventas: #para cada diccionario que esta en la lista ventas
    fecha = diccionario['fecha'] #se designa una variable fecha que corresponde al valor de la clave fecha
    cantidad = diccionario['cantidad'] #se designa una variable cantidad que corresponde al valor de la clave cantidad
    precio = diccionario['precio'] #se designa una variable precio que corresponde al valor de la clave precio
    ingreso = cantidad * precio #se crea una variable ingreso que corresponde a la multiplicacion de cantidad por precio
    if fecha in ingresos_por_dia: #se crea una condicion en la iteracion para crear el diccionario donde la variable fecha se encuentra dentro del diccionario ingresos_por_dia 
        ingresos_por_dia[fecha] += ingreso #si ya se creo una clave valor del producto en el diccionario ingresos_por_dia, se debe sumar el ingreso
    else: #en caso opuesto
        ingresos_por_dia[fecha] = ingreso #solo se crea una clave valor donde la fecha tiene su ingreso inicial

print(ingresos_por_dia) #Se comprueba creacion del diccionario

#Resumen de ventas

resumen_ventas = {} #Se crea un diccionario que se llama resumen ventas
for diccionario in ventas:
    producto = diccionario['producto'] #se designa una variable producto que corresponde al valor de la clave producto
    cantidad = diccionario['cantidad'] #se designa una variable cantidad que corresponde al valor de la clave cantidad
    precio = diccionario['precio'] #se designa una variable precio que corresponde al valor de la clave precio
    ingreso = cantidad * precio #se crea una variable ingreso que corresponde a la multiplicacion de cantidad por precio
    if producto in resumen_ventas:
        suma_cant, suma_ingresos, promedio_precio = resumen_ventas[producto] #se crea una variable que llama al valor de la clave del producto
        resumen_ventas[producto] = (suma_cant + cantidad, suma_ingresos + ingreso, round((suma_ingresos + ingreso) / (suma_cant + cantidad),2))# #se actualiza la suma de ingresos y cantidades  
    else:# si ya se creo una clave valor del producto en el diccionario resumen_ventas, se debe sumar la cantidad y el ingreso
        resumen_ventas[producto] = (cantidad, ingreso, precio)# #solo se crea una clave valor donde el producto tiene su cantidad inicial, ingreso y precio

print(resumen_ventas) #Se comprueba creacion del diccionario

