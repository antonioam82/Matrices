print("JUEGO DE LA VIDA")
import time
from VALID import OKI, OK
import subprocess

def nval(n):
    while n<=0:
        n=OKI(input("Introduce un número mayor de 0: "))
    return n

def nvalcf(n,t):
    if t==("f"):
        while n<7:
            n=OKI(input("Introduce un número mayor de 6: "))
    else:
        while n<6:
            n=OKI(input("Introduce un número mayor de 5: "))
    return n

print("¿Que desea ver?: ")
print("A) OSCILADOR")
print("B) PLANEADOR")
print("C) COLISION PLANEADORES")
print("D) RANA")
ver=input("Escriba aquí su opción: ")
while ver!=("A") and ver!=("B") and ver!=("C") and ver!=("D"):
    ver=input("Escriba \'A\', \'B\',\'C\'o\'D\' según su opción: ")
panel=input("Escriba caracter para el tablero: ")

if ver==("A") or ver==("B"):
    filas=nvalcf(OKI(input("Introduce el número de filas: ")),"f")
    columnas=nvalcf(OKI(input("Introduce el número de columnas: ")),"c")
else:
    filas=22
    columnas=22
    
pul=nval(OKI(input("Introduce el número de pulsos: ")))
vel=OK(input("Escribe periodicidad de pulso: "))
tablero=[]
el=0
subprocess.call(["cmd.exe","/C","cls"])

for i in range(filas):
    tablero.append(([False])*columnas)
    
if ver==("A"):
    tablero[4][5]=True
    tablero[5][5]=True
    tablero[6][5]=True
if ver==("D"):
    filas=22
    columnas=22
    tablero[20][20]=True
    tablero[20][19]=True
    tablero[20][18]=True
    tablero[19][19]=True
    tablero[19][18]=True
    tablero[19][17]=True


else:
    tablero[2][2]=True
    tablero[3][3]=True
    tablero[3][4]=True
    tablero[2][4]=True
    tablero[1][4]=True
    if ver==("C"):
        filas=22
        columnas=22
        tablero[20][20]=True 
        tablero[19][19]=True
        tablero[19][18]=True
        tablero[20][18]=True
        tablero[21][18]=True

    
    
print("JUEGO DE LA VIDA")
print("TIME:  0")
for y in range(filas):
    for x in range(columnas):
        if tablero[y][x]:
            print("*"+" ",end="")
        else:
            print(panel+" ",end="")
    print()
time.sleep(vel)
subprocess.call(["cmd.exe","/C","cls"])

pulsos=pul
for t in range(pulsos):
    print("JUEGO DE LA VIDA")
    nuevo=[]
    for i in range(filas):
        nuevo.append([0]*columnas)
        
    for y in range(filas):
        for x in range(columnas):
            n=0
            if y>0 and x>0 and tablero[y-1][x-1]:
                n+=1
            if x>0 and tablero[y][x-1]:
                n+=1
            if y<filas-1 and x>0 and tablero[y+1][x-1]:
                n+=1
            if y>0 and tablero[y-1][x]:
                n+=1
            if y<filas-1 and tablero[y+1][x]:
                n+=1
            if y>0 and x<columnas-1 and tablero[y-1][x+1]:
                n+=1
            if x<columnas-1 and tablero[y][x+1]:
                n+=1
            if y<filas-1 and x<columnas-1 and tablero[y+1][x+1]:
                n+=1
                
            if tablero[y][x] and (n==2 or n==3):
                nuevo[y][x]=True
            elif not tablero[y][x] and n==3:
                nuevo[y][x]=True
            else:
                nuevo[y][x]=False

    tablero=nuevo
    t+1
    print("TIME: ",t+1)
    for y in range(filas):
        for x in range (columnas):
            if tablero[y][x]:
                print("*"+" ",end="")
            else:
                print(panel+" ",end="")
        print()
    time.sleep(vel)
    if t<pulsos:
        subprocess.call(["cmd.exe","/C","cls"])


    



    







    









    







