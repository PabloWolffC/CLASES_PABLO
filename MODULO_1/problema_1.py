'''
PROBLEMA 1:

Una parábola puede definirse con la fórmula y = ax2 + bx + c, donde a, b, c son constantes. Escribe un programa en Python (archivo p1.py)
 que reciba los valores de a, b, c para dos parábolas y luego indique en consola para cada parábola si intersecta (True) o no (False) con el eje X. 
 Además, tu programa debe indicar en consola si las dos parábolas se intersectan (True) o no (False) entre ellas.
 '''

a = input('ingrese un numero para a: ')
b = input('ingrese un numero para b: ')
c = input('ingrese un numero para c: ')

a = float(a)
b = float(b)
c = float(c)

x1 = (-b + ((b**2 - 4*a*c)**0.5)) / 2*a
x2 = (-b - ((b**2 - 4*a*c)**0.5)) / 2*a

print(x1,x2) 

sol1 = a*x1**2 + b*x1 + c 
sol2 = a*x2**2 + b*x2 + c 


print(sol1 == 0)
print(sol2 == 0)
