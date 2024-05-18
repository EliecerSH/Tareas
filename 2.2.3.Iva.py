producto=input(" ingresa el nombre del producto ")
ValorDelProducto=int(input(" ingresa el valor del producto "))
valorNeto=float(0.81)
valorSinIva=float(ValorDelProducto*valorNeto)

print("----Detalle del producto----")
print(f" Nombre del producto = {producto}")
print(f" Valor del producto = ${ValorDelProducto}")
print(f" valor del producto sin iva = ${valorSinIva}")