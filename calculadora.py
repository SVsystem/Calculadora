def sumar(a,b):
    print("resultado: ",(a+b))
def restar(a,b):
    print("resultado: ",(a-b))
def multiplicar(a,b):
    print("resultado:",(a*b))
def dividir(a,b):
    print("resultado: ",(a/b))
global num1 , num2
while(True):
    print("\n=====================\nCalculadora en python")
    print("=====================")
    opcion=-1
    while(opcion<1)or(opcion>5):
        opcion=int(input("1.SUMA \n2.RESTA \n3.MULTIPLICACION\n4.DIVICION \n5.SALIR\nINGRESE UNA OPCION: "))
    if(opcion==5):
        print("Saliendo...")
        break

    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
    
   
    if(opcion==1):
        sumar(num1,num2)
    elif(opcion==2):
        restar(num1,num2)
    elif(opcion==3):
        multiplicar(num1,num2)
    else:
         dividir(num1,num2)
    

