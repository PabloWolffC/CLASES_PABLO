'''
PROBLEMA 3:

Son tiempos de guerra, por lo que, para que no se puedan desifrar los mensajes se envian las letras en forma de numeros segun tabla ASCII. 
Debes hacer un codigo el cual permita enviar una oracion de 10 caracteres usando solo 1 input escrito en toooooooodo el codigo. 
Este input debe recibir un numero y tu debes desifrar ese numero a letra. Al final entregar la oracion completa.

Hint: investigar la tabla ASCII y como se implementa en python
'''

#Recordar que

a = 0
frase = ''
while a < 10:
    
    numero = int(input('ingrese un numero: '))
    letra = chr(numero)
    frase += letra
    a += 1
    print(frase)

print(frase)
