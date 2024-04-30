con=(input(" cree una contraseña "))

if 7 < len(con) < 9:
    if any([c.isdigit() for c in con]):
        if any([c.islower() for c in con]):
            if any([c.isupper() for c in con]):
                print(" la contrasena es valida ")
else:
    print(" la contrasena no es validad ")