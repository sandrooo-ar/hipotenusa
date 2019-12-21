import math     #Libreria que permite la raíz cuadrada

status = input("\n1.- Missing hypotenuse \n2.- Missing large leg \n3.- Missing small leg \n")

#a == Hipotenusa
#b == Cateto grande
#c == Cateto pequeño 

def hipotenusa():
    b = int(input("Enter the size of the largest leg: "))      #Se introduce el cateto mas grande primero para que la fórmula no de negativo
    c = int(input("Enter the size of the smallest leg: "))

    a = math.sqrt(b**2+c**2)        #Fórmula de la hipotenusa

    print("\nLa medida de la hipotenusa de tu triángulo es de " + str(a) + "\n")

def cateto_grande():
    a = int(input("Introduce el tamaño de la hipotenusa: "))            #Se introduce la hipotenusa primero porque es más grande que el cateto pequeño y así la fórmula no da negativo
    c = int(input("Enter the size of the smallest leg: "))      

    b = math.sqrt(a**2 - c**2)      #Fórmula del cateto grande

    print("\nThe measure of the hypotenuse of your triangle is " + str(b) + "\n")

def cateto_pequeño():
    a = int(input("Enter the size of the hypotenuse: "))            #Se introduce la hipotenusa primero porque es más grande que el cateto grande y asi la fórmula no da negativo
    b = int(input("Enter the size of the largest leg: "))

    c = math.sqrt(a**2-b**2)        #Fórmula del cateto pequeño

    print("\nThe measure of the smallest leg of your triangle is " + str(c) + "\n")

if status == 1:
    print(hipotenusa())         #Si el input es de 1, el output es la medida de la hipotenusa

elif status == 2:              
    print(cateto_grande())      #Si el input es de 2, el output es la medida del cateto grande

elif status == 3: 
    print(cateto_pequeño())     #Si el input es de 3, el output es la medida del cateto pequeño

xyz = 0

while xyz == 0:
    x = input("Press enter to exit:  ")
    xyz = 1