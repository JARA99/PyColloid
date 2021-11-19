#-----------------------------------------------------------------------------------------#
#----------------------------------   Initial Values   -----------------------------------#
#-----------------------------------------------------------------------------------------#
#   Date: 11/2021                                                                         #
#   File: InitialValues.py                                                                #
#-----------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------#
#                                        Packages                                         #
#-----------------------------------------------------------------------------------------#

import csv
import random as rd     # Librería para generar números aleatorios

#-----------------------------------------------------------------------------------------#
#                                    Global Variables                                     #
#-----------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------#
#                                          Code                                           #
#-----------------------------------------------------------------------------------------#



#-----------------------------------------------------------------------------------------#
#                                         Classes                                         #
#-----------------------------------------------------------------------------------------#

class coloide:  # Clase para las partículas
    def __init__(self, ID, masa, carga, rx, ry, vx, vy, ax, ay):
        self.ID = ID
        self.masa = masa
        self.carga = carga
        self.rx = rx
        self.ry = ry
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay

#-----------------------------------------------------------------------------------------#
#                                        Functions                                        #
#-----------------------------------------------------------------------------------------#

def ini_values(i,m,q,x,y,vx,vy,ax,ay,Lista):   # Función para asignar valores random en un rango dado
    mas= rd.uniform(m[0],m[1])
    car= rd.uniform(q[0],q[1])
    rx = rd.uniform(x[0],x[1])
    ry = rd.uniform(y[0],y[1])
    vx = rd.uniform(vx[0],vx[1])
    vy = rd.uniform(vy[0],vy[1])
    ax = rd.uniform(ax[0],ax[1])
    ay = rd.uniform(ay[0],ay[1])
    Lista.append(coloide(i, mas, car, rx, ry, vx, vy, ax, ay))

def export(Lista,nombre,i,N):   # Función para crear un archivo .csv con toda la información de las particulas dadas
    a = str(nombre) +'_'+ str(i) +'.csv'
    f = open(a, 'w')
    w = csv.writer(f)
    w.writerow(["Id", "m", "q","rx","ry","vx","vy","ax","ay"])  # Encabezado
    w.writerow([])
    for ide in range(N):
        col=[Lista[ide].ID,Lista[ide].masa,Lista[ide].carga,Lista[ide].rx,
             Lista[ide].ry,Lista[ide].vx,Lista[ide].vy,Lista[ide].ax,Lista[ide].ay]
        w.writerow(col)
    f.close()
