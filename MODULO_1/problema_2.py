'''
EL usuario ingresa un numero, el programa debe decir si es par o impar
'''

a = input('por favor ingrese un numero: ')
a= int(a)

sol = a%2

if sol == 0:
    print(a, 'es par.')
elif sol != 0:
    print(a, 'es impar.')
