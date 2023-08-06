fin = False
print("""*******
calculadora
*********
                  
 Menu 
1 Suma
2 Resta 
3 Multiplicacion
4 Division 
5 Salir""")

while not(fin):
    opc = int (input("Opcion:"))
    if  (opc==1):
        sum1 = int(input("Sumando uno:"))
        sum2= int (input("Sumando dos:"))
        print("la Suma es:",sum1+sum2)
    elif  (opc==2):
        resta1= int(input("Resta uno:"))
        resta2= int (input("Resta dos:"))
        print("La Resta es:",resta1-resta2)
    elif  (opc==3):
        multiplicando1= int(input("Multiplicando uno:"))
        multiplicando2= int (input("Multiplicando dos:"))
        print("La Multiplicacion es:",multiplicando1*multiplicando2)
    elif  (opc==4):
        dividendo= int(input("Dividendo uno:"))
        divisor = int (input("Divisor:"))
        print("La División es.",dividendo/divisor)
    elif ( opc ==5):
        fin =True