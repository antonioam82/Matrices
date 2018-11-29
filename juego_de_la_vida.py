import time
import subprocess
from VALID import ns, OK, OKI, opt
def nval(n):
    while n<=0:
        n=OKI(input("Introduce un número mayor de 0: "))
    return n

while True:
    print("¿Que desea ver?: ")
    print("A) OSCILADOR")
    print("B) PLANEADOR")
    print("C) COLISION PLANEADORES")
    print("D) DISPARADOR DE PLANEADORES")
    ver=opt(input("Escriba aquí su opción: "),["A","B","C","D"])
    vel=OK(input("Introduce segundos entre cada pulso: "))
    panel=(".")
    filas=38
    colum=75
    
    pul=nval(OKI(input("Introduce número de pulsos: ")))

    tablero=[]
    el=0
    subprocess.call(["cmd.exe","/C","cls"])

    for i in range(filas):
        tablero.append(([False])*colum)

    #for x in tablero:
        #print(x)

    if ver==("A"):
        tablero[4][5]=True
        tablero[5][5]=True
        tablero[6][5]=True
    if ver==("B"):
        tablero[2][2]=True
        tablero[3][3]=True
        tablero[3][4]=True
        tablero[2][4]=True
        tablero[1][4]=True
    if ver==("C"):
        tablero[2][2]=True
        tablero[3][3]=True
        tablero[3][4]=True
        tablero[2][4]=True
        tablero[1][4]=True
        tablero[20][20]=True
        tablero[19][19]=True
        tablero[19][18]=True
        tablero[20][18]=True
        tablero[21][18]=True
    if ver=="D":
        tablero[4][1]=True
        tablero[5][1]=True
        tablero[4][2]=True
        tablero[5][2]=True
        tablero[4][11]=True
        tablero[5][11]=True
        tablero[6][11]=True
        tablero[3][12]=True
        tablero[7][12]=True
        tablero[2][13]=True
        tablero[8][13]=True
        tablero[2][14]=True
        tablero[8][14]=True
        tablero[5][15]=True
        tablero[3][16]=True
        tablero[7][16]=True
        tablero[4][17]=True
        tablero[5][17]=True
        tablero[6][17]=True
        tablero[5][18]=True
        tablero[2][21]=True
        tablero[3][21]=True
        tablero[4][21]=True
        tablero[2][22]=True
        tablero[3][22]=True
        tablero[4][22]=True
        tablero[1][23]=True
        tablero[5][23]=True
        tablero[0][25]=True
        tablero[1][25]=True
        tablero[5][25]=True
        tablero[6][25]=True
        tablero[2][35]=True
        tablero[3][35]=True
        tablero[2][36]=True
        tablero[3][36]=True
        

    print("JUEGO DE LA VIDA")
    print("PULSO: 0")
    for y in range(filas):
        for x in range (colum):
            if tablero[y][x]:
                print("*"+" ",end="")
            else:
                print(panel+" ",end="")
        print()
    time.sleep(1)
    subprocess.call(["cmd.exe","/C","cls"])

    pulsos=pul
    subprocess.call(["cmd.exe","/C","cls"])
    for t in range(pulsos):
        print("JUEGO DE LA VIDA")
        nuevo=[]
        for i in range(filas):
            nuevo.append([0]*colum)

        for y in range(filas):
            for x in range(colum):
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
                if y>0 and x<colum-1 and tablero[y-1][x+1]:
                    n+=1
                if x<colum-1 and tablero[y][x+1]:
                    n+=1
                if y<filas-1 and x<colum-1 and tablero[y+1][x+1]:
                    n+=1
                if tablero[y][x] and (n==2 or n==3):
                    nuevo[y][x]=True
                elif not tablero[y][x] and n==3:
                    nuevo[y][x]=True
                else:
                    nuevo[y][x]=False
        tablero=nuevo
        
        #t+1
        print("PULSO: ",t+1)
        for y in range(filas):
            for x in range (colum):
                if tablero[y][x]:
                    print("*"+" ",end="")
                else:
                    print(panel+" ",end="")
            print()
        time.sleep(vel)
        if t<pulsos:
            subprocess.call(["cmd.exe","/C","cls"])
    conti=ns(input("¿Desea continuar?: "))
    if conti==("n"):
        break
    try:
        subprocess.call(["cmd.exe","/C","cls"])
    except:
        continue
