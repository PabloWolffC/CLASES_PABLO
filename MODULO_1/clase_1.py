print('hello word')

texto = 'hola mundo'

print(texto)

a = 1 #int
print(a)

b = 2 #int

print(a+b)

a = 5
print(a)

c = 5.3 #float
print(a+c)

a = float(a) #transformo a a un float
print(a)

c = int(c)
print(c) #es decir, lo corta

#type me dice que formato tiene
print(type(c))

print(texto+texto)
print(texto+ ' '+texto)

nombre = 'pablo'
print('hola', nombre) #asi junto una variable con texto

#como poder consultar algo en la consola
#uso el input

#variable = input('ingrese un numero: ')
#print(type(variable)) #si ingreso un numero me dice que es un string, pero yo quiero que sea un int

#variable = int(input('ingrese un numer: '))
#print(type(variable))

#para hacer operaciones iterativas uso el while

a = 0

while a < 3:
    print('se corre una iteracion de ciclo')
    print(a)

    #es inmportante agregaqr la condicion de fin
    a += 1 #cada vez que el codigo pasa por aqui se suma 1

print(2==2)
print(2!=2)

#if y else, si pasa, de otra forma

a = 3

if a < 3:
    print('a es menor que 3')

elif a == 3:
    print('a es 3')

else:
    print('a es mayor que 3')

b = 2

if b > 2:
    print('b es mayor que 2')
    






