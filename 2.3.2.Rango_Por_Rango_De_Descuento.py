edad=int(input(" ingrese su edad "))

if edad >0 and edad < 15:
    print(f"edad {edad}, tiene un descuento del 50% ")
elif edad <30 and edad <30:
    print(f"edad {edad}, tiene un descuento del 20% ")
elif edad > 60:
    print(f"edad {edad}, tiene un descuento del 90% ")
else:
    print(f"edad {edad}, no tiene descuento ")