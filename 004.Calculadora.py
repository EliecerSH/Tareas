election=0

while election != 5:
    print("""
    seleccione la operacion
          
    1) Sumar
    2) Restar
    3) Dividir
    4) Multiplicar
    5) Salir
    """)

    election=int(input() )

    if election == 1:
        valor1=input(" ingrase primer valor ")
        numero1=float(valor1)
        valor2=input(" ingrase segundo valor ")
        numero2=float(valor2)
        resulato = (numero1+numero2)
        print("El resultado es ",resulato)

    elif election == 2:
        valor1=input(" ingrase primer valor ")
        numero1=float(valor1)
        valor2=input(" ingrase segundo valor ")
        numero2=float(valor2)
        resulato = (numero1-numero2)
        print(" el resitado es ",resulato)

    elif election == 3:
        valor1=input(" ingrase primer valor ")
        numero1=float(valor1)
        valor2=input(" ingrase segundo valor ")
        numero2=float(valor2)
        resulato = (numero1/numero2)
        print(" el resitado es ",resulato)

    elif election == 4:
        valor1=input(" ingrase primer valor ")
        numero1=float(valor1)    
        valor2=input(" ingrase segundo valor ")
        numero2=float(valor2)
        resulato = (numero1*numero2)
        print(" el resitado es ",resulato)

    elif election ==5:
        print(" termino del proceso ")

