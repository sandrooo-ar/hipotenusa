import math     #Libreria que permite la raíz cuadrada

status = input("\n1.- Falta la hipotenusa \n2.- Falta el cateto grande \n3.- Falta el cateto pequeño \n")

#a == Hipotenusa
#b == Cateto grande
#c == Cateto pequeño 

def hipotenusa():
    b = int(input("Introduce el tamaño del cateto más grande: "))      #Se introduce el cateto mas grande primero para que la fórmula no de negativo
    c = int(input("Introduce el tamaño del cateto más pequeño: "))

    a = math.sqrt(b**2+c**2)        #Fórmula de la hipotenusa

    print("\nLa medida de la hipotenusa de tu triángulo es de " + str(a) + "\n")

def cateto_grande():
    a = int(input("Introduce el tamaño de la hipotenusa: "))            #Se introduce la hipotenusa primero porque es más grande que el cateto pequeño y así la fórmula no da negativo
    c = int(input("Introduce el tamaño del cateto más pequeño: "))      

    b = math.sqrt(a**2 - c**2)      #Fórmula del cateto grande

    print("\nLa medida del cateto más grande de tu triángulo es de " + str(b) + "\n")

def cateto_pequeño():
    a = int(input("Introduce el tamaño de la hipotenusa: "))            #Se introduce la hipotenusa primero porque es más grande que el cateto grande y asi la fórmula no da negativo
    b = int(input("Introduce el tamaño del cateto más grande: "))

    c = math.sqrt(a**2-b**2)        #Fórmula del cateto pequeño

    print("\nLa medida del cateto más pequeño de tu triángulo es de " + str(c) + "\n")

if status == 1:
    print(hipotenusa())         #Si el input es de 1, el output es la medida de la hipotenusa

elif status == 2:              
    print(cateto_grande())      #Si el input es de 2, el output es la medida del cateto grande

elif status == 3: 
    print(cateto_pequeño())     #Si el input es de 3, el output es la medida del cateto pequeño

xyz = 0

while xyz == 0:
    x = input("Pulsa enter para salir:  ")
    xyz = 1