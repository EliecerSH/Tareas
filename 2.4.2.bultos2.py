cand=int(input(" ingresa la cantidad de bultos "))
md=0
lv=0
nrBulto=1
while nrBulto <= cand:
    kg=float(input(f" ingrese el peso del bulto {nrBulto} (kg) "))
    if kg <10 and kg >5:
        md=md+1
        nrBulto=nrBulto+1
    elif kg<6 and kg >0:
        lv=lv+1
        nrBulto=nrBulto+1

total= md*5000+lv*1000

print(f" su total a pagar es ${total}")