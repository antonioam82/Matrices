print("JUEGO DE LA VIDA")
import time
from VALID import OKI
import subprocess
filas=OKI(input("Introduce el número de filas: "))
columnas=OKI(input("Introduce el número de columnas: "))
pul=OKI(input("Introduce el número de pulsos: "))
print("¿Que desea ver?: ")
print("A) OSCILADOR")
print("B) PLANEADOR")
ver=input("Escriba aquí su opción: ")
while ver!=("A") and ver!=("B"):
    ver=input("Escriba \'A\' o \'B\' según su opción: ")
subprocess.call(["cmd.exe","/C","cls"])

tablero=[]
el=0

for i in range(filas):
    tablero.append(([False])*columnas)
    #print(tablero[el])
    #el+=1

if ver==("A"):
    tablero[4][5]=True
    tablero[5][5]=True
    tablero[6][5]=True
else:
    tablero[7][7]=True
    tablero[8][8]=True
    tablero[8][9]=True
    tablero[7][9]=True
    tablero[6][9]=True
print("JUEGO DE LA VIDA")
print("TIME:  0")
for y in range(filas):
    for x in range(columnas):
        if tablero[y][x]:
            print("*"+" ",end="")
        else:
            print("."+" ",end="")
    print()
time.sleep(2)
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
                print("."+" ",end="")
        print()
    time.sleep(2)
    subprocess.call(["cmd.exe","/C","cls"])


    









    







