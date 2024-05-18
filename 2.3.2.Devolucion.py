user=input(" ingrese su usuario ")
pwd=input(" ingrese contraseña ")


if user=="duoc" and pwd=="uc123":
    devolucion=int(input(" bienvenido, ingresa el monto a devolver "))
    if devolucion>100000:
        print(" se dara maxima urgencia a su devolucion de dinero")
    else:
        print(" el caso a quedado registrado, se le informara lo antes posible")
else:
    print(" error en la contraseña ")