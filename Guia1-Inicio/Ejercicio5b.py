
def Imprimir(clave,cursoNombre,CP):
    print("\n*************************************")
    print("* Calificación final de {} ({}) : {}".format(cursoNombre,clave,str(CP)))
    print("*************************************")


#PASO1
clave=input("Ingrese clave: ")
cursoNombre=input("Nombre del curso: ")
#PASO2
print("*************************")
print("Ingresar los factores de ponderacion: ")
C=float(input("Cuestionarios: "))
T=float(input("Tareas: "))
E=float(input("Examen Final: "))
print("*************************")
#PASO3
cuestionarioPuntaje = 0
cuestionarioCont = 0
print("\nA continuación ingrese los puntajes del cuestionario\n> Para salir presione cualquier letra: ")
while True:
    try:
        cuestionarioPuntaje +=  float(input("Puntaje de cuestionario: "))
        cuestionarioCont = cuestionarioCont + 1
    except:
        break
PC = cuestionarioPuntaje / cuestionarioCont
# print(str(PC))
#PASO3
tareaPuntaje = 0
tareaCont = 0
print("\nA continuación ingrese los puntajes de las tareas\n> Para salir presione cualquier letra: ")
while True:
    try:
        tareaPuntaje +=  float(input("Puntaje de tarea: "))
        tareaCont = tareaCont + 1
    except:
        break
PT = tareaPuntaje / tareaCont
# print(str(PT))

#PASO5
tieneCalificacionFinal = input("\nTiene calificación final? (S/N): ")
if (tieneCalificacionFinal.upper() == "S"):
    #PASO6
    F = float(input("Calificación Final: "))
    #PASO7
    CP = (((C * PC) + ( T * PT) + (E * F)) / ( C + T + E)) * 100.0
else:
    #PASO9
    CP = (((C * PC) + ( T * PT)) / ( C + T)) * 100.0
# print(str(CP))

#PASO10
Imprimir(clave,cursoNombre,CP)

