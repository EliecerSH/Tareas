palabra=(input(" ingrese un palabra "))
def con_vocales(palabra):
    vocales = "aeiouAEIOU"

    return ([c for c in palabra if c in vocales])

print(len(con_vocales(palabra)))