eleccion=0

print(""" ¿que tan amenudo estudias? 
      
      1) nunca
      2) a veces
      3) normalmente
      4) siempre
      """)

eleccion=int(input())

if eleccion==1:
    puntuacion=0+3
elif eleccion==2:
    puntuacion=0+6
elif eleccion==3:
    puntuacion=0+8
elif eleccion==4:
    puntuacion=0+10

print(""" ¿Vienes a clases? 
      
      1) nunca
      2) a veces
      3) normalmente
      4) siempre
      """)

eleccion=int(input())

if eleccion==1:
    pt=puntuacion+3
elif eleccion==2:
    pt=puntuacion+6
elif eleccion==3:
    pt=puntuacion+8
elif eleccion==4:
    pt=puntuacion+10

print(""" ¿llegas temprano a clases? 
      
      1) nunca
      2) a veces
      3) normalmente
      4) siempre
      """)

eleccion=int(input())

if eleccion==1:
    pt1=pt+3
elif eleccion==2:
    pt1=pt+6
elif eleccion==3:
    pt1=pt+8
elif eleccion==4:
    pt1=pt+10

print(""" ¿pones atencion en clases? 
      
      1) nunca
      2) a veces
      3) normalmente
      4) siempre
      """)

eleccion=int(input())

if eleccion==1:
    pt2=pt1+3
elif eleccion==2:
    pt2=pt1+6
elif eleccion==3:
    pt2=pt1+8
elif eleccion==4:
    pt2=pt1+10

print(""" ¿participa en clases? 
      
      1) nunca
      2) a veces
      3) normalmente
      4) siempre
      """)

eleccion=int(input())

if eleccion==1:
    pt3=pt2+3
elif eleccion==2:
    pt3=pt2+6
elif eleccion==3:
    pt3=pt2+8
elif eleccion==4:
    pt3=pt2+10

print(""" ¿tomas apuntes? 
      
      1) nunca
      2) a veces
      3) normalmente
      4) siempre
      """)

eleccion=int(input())

if eleccion==1:
    pt4=pt3+3
elif eleccion==2:
    pt4=pt3+6
elif eleccion==3:
    pt4=pt3+8
elif eleccion==4:
    pt4=pt3+10

print(""" ¿estudia de forma autodidacta? 
      
      1) nunca
      2) a veces
      3) normalmente
      4) siempre
      """)

eleccion=int(input())

if eleccion==1:
    pt5=pt4+3
elif eleccion==2:
    pt5=pt4+6
elif eleccion==3:
    pt5=pt4+8
elif eleccion==4:
    pt5=pt4+10

print(""" ¿lees en tu tiempos libres? 
      
      1) nunca
      2) a veces
      3) normalmente
      4) siempre
      """)

eleccion=int(input())

if eleccion==1:
    pt6=pt5+3
elif eleccion==2:
    pt6=pt5+6
elif eleccion==3:
    pt6=pt5+8
elif eleccion==4:
    pt6=pt5+10

print(""" ¿le preguntas tu dudas al profesor? 
      
      1) nunca
      2) a veces
      3) normalmente
      4) siempre
      """)

eleccion=int(input())

if eleccion==1:
    pt7=pt6+3
elif eleccion==2:
    pt7=pt6+6
elif eleccion==3:
    pt7=pt6+8
elif eleccion==4:
    pt7=pt6+10

print(""" ¿ayudas a tu compañeros? 
      
      1) nunca
      2) a veces
      3) normalmente
      4) siempre
      """)

eleccion=int(input())

if eleccion==1:
    pt8=pt7+3
elif eleccion==2:
    pt8=pt7+6
elif eleccion==3:
    pt8=pt7+8
elif eleccion==4:
    pt8=pt7+10

print(""" ¿lo que no resuelves en clase lo resuelves en casa? 
      
      1) nunca
      2) a veces
      3) normalmente
      4) siempre
      """)

eleccion=int(input())

if eleccion==1:
    pt9=pt8+3
elif eleccion==2:
    pt9=pt8+6
elif eleccion==3:
    pt9=pt8+8
elif eleccion==4:
    pt9=pt8+10

print(""" ¿te retro alimentas con tu compalleros? 
      
      1) nunca
      2) a veces
      3) normalmente
      4) siempre
      """)

eleccion=int(input())

if eleccion==1:
    pt10=pt9+3
elif eleccion==2:
    pt10=pt9+6
elif eleccion==3:
    pt10=pt9+8
elif eleccion==4:
    pt10=pt9+10

if pt10==120:
    print(f" eres el alumno perfecto {pt10}pts")
elif pt10>90 and pt10 < 120:
    print(f"en un estudiante ecepcional {pt10}pts")
elif pt10>60 and pt10<90:
    print(f" eres un buen estudiante {pt10}pts")
else:
    print(f" tienes que mejora {pt10}pts")