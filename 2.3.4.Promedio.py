nt1=float(input(" ingresa tu primera nota "))
nt2=float(input(" ingrese tu segunda nota "))
nt3=float(input(" ingresa tu tercera nota "))

promedio=(nt1+nt2+nt3)/4

if promedio>4:
    print(f" aprobado {promedio}")
else:
    print(f" desaprobado {promedio}")