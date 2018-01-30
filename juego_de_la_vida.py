print("JUEGO DE LA VIDA")
import time
import subprocess
filas=10
columnas=10


tablero=[]
el=0

for i in range(filas):
    tablero.append(([False])*columnas)
    #print(tablero[el])
    #el+=1

tablero[4][5]=True
tablero[5][5]=True
tablero[6][5]=True


for y in range(filas):
    for x in range(columnas):
        if tablero[y][x]:
            print("*"+" ",end="")
        else:
            print("."+" ",end="")
    print()
time.sleep(1)
subprocess.call(["cmd.exe","/C","cls"])

pulsos=10
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
            if y<filas-1 and x>0 and tablero[y+1][x]:
                n+=1
            if y>0 and x<columnas-1 and tablero[y-1][x+1]:
                n+=1
            if x<columnas-1 and tablero[y][x+1]:
                n+=1
            if y<filas-1 and x<columnas-1 and tablero[x+1][y+1]:
                n+=1
                
            if tablero[y][x] and (n==2 or n==3):
                nuevo[y][x]=True
            elif not tablero[y][x] and n==3:
                nuevo[y][x]=True
            else:
                nuevo[y][x]=False

    tablero=nuevo
    t+1
    for y in range(filas):
        for x in range (columnas):
            if tablero[y][x]:
                print("*"+" ",end="")
            else:
                print("."+" ",end="")
        print()
    time.sleep(1)
    subprocess.call(["cmd.exe","/C","cls"])


    







