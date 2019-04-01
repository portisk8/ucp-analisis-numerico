c = float(input("Ingrese calificación: "))
if(c < 60):
    print("F")
elif (c >= 60 and c <70):
    print("D")
elif (c >= 70 and c <80):
    print("C")
elif (c >= 80 and c <90):
    print("B")
elif (c >= 90 and c <=100):
    print("A")
else:
    print("La calificacion debe estar entre 0 y 100")