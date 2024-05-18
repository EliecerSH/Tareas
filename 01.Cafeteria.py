election=0
pn=0
pie=0
ca=0
te=0
al=0
letras=("qwertyuiopasdfghjklQWERTYUIOPASDFGHJKL")
while election !=3:
  print("""----Elija una opcion----
          
          1.Registrar compra
          2.Ver informe de ventas
          3.Salir
          """)
  try:
     election=int(input())
  except ValueError:
       print(" SOLO SE PERMITEN NUMEROS ENTEROS DEL 1 AL 3 ")

  if election==1:
      while election !=6:
       print("""----Que decea comprar----
              
              1.Pan ciabatta = $2.000
              2.Pie de limón = $3.500
              3.Cafe = $2.200
              4.te = $1.600
              5.Alfajor = $1.000
              6.volver
              """)
       try:
        election=int(input())
       except ValueError:
        print (" SOLO SE PERMITEN NUMEROS ENTEROS DEL 1 AL 6")
       if election==1:
         pn=pn+1
       elif election==2:
         pie=pie+1
       elif election==3:
        ca=ca+1
       elif election==4:
         te=te+1
       elif election==5:
         al=al+1
  elif election==2:
        while election !=1:
          print(f"""---informe de venta---
              1.pan
              Cantidad vendida = {pn} monto ingresado = ${pn*2000}
              2.Pie de limón
              Cantidad vendida = {pie} monto ingresado = ${pie*3500}
              3.cafe
              Cantidad vendida = {ca} monto ingresado = ${ca*2200}
              4.te
              cantidad vendida = {te} monto ingresado = ${te*1600}
              5.Alfajor
              cantidad vendida = {al} monto ingresado = ${al*1000}
              
              -TOTAL A PAGAR= ${pn*2000+pie*3500+ca*2200+te*1600+al*1000}
              
              1.Volver
              2.Guardar archivo
            """)
          try:
            election=int(input())
          except ValueError:
               print(" SOLO SE PERMITEN NUMEROS ENTEROS DEL 1 AL 2 ")
          if election==2:
              archivo=open('data.txt','a')
              archivo.write(f"""---informe de venta---
              1.pan
              Cantidad vendida = {pn} monto ingresado = ${pn*2000}
              2.Pie de limón
              Cantidad vendida = {pie} monto ingresado = ${pie*3500}
              3.cafe
              Cantidad vendida = {ca} monto ingresado = ${ca*2200}
              4.te
              cantidad vendida = {te} monto ingresado = ${te*1600}
              5.Alfajor
              cantidad vendida = {al} monto ingresado = ${al*1000}
              
              -TOTAL A PAGAR= ${pn*2000+pie*3500+ca*2200+te*1600+al*1000}
             """)
  elif election==3:
       print("----fin del proceso----")