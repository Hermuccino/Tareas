#Bucle Basico#
for i in range(101):
    print(i) 
#Bucle multiplos de 2#
for i in range(4,500,2):
    print(i)
#Bucle Contando Vanilla Ice#
for i in range(1,100):
    if i % 5 == 0 and i % 10 == 0:
        print('baby')
    elif i % 5 == 0:
        print('ice ice')
    else:
        print(i)
#Bucle Wow Numero Gigante#
numero_gigante = 0
for i in range(0,500001):
    if i % 2 == 0:
        numero_gigante += i
print(numero_gigante)
#Bucle Regresame al 3#
numero = 2024
while numero > 0:
    print(numero)
    numero -= 3
#Bucle Contador Dinamico#
numInicial = 2
numFinal = 40
multiplo = 5
for i in range(numInicial,numFinal+1):
    if i % multiplo == 0:
        print(i)

