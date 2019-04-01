import math


print('Hallar raices de una ecuación cuadratica (ax²+bx+c=0)')
print('Ingrese los valores de A,B y C')

a=float(input("Ingresa coeficiente cuadratico\n"))
b=float(input("Ingresa coeficiente lineal\n"))
c=float(input("Ingresa constante\n"))
disc=b*b-4*a*c
if(a!=0):
 if(disc<0):
  print("Tiene raices imaginarias")
 else:
  x1=(-b+(math.sqrt(disc)))/(2*a)
  x2=(-b-(math.sqrt(disc)))/(2*a)

  print(str(a) + "x² + "+str(b)+"x + "+str(c)+" c = 0")
  print("|_ X1 = "+str(x1))
  print("|_ X2 = "+str(x2))
else:
  x = -c/b
  print("X = " + str(x))