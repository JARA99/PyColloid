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
    def __init__(self, ID, masa, rx, ry, vx, vy, ax, ay, carga):
        self.ID = ID
        self.masa = masa
        self.rx = rx
        self.ry = ry
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.carga = carga

#-----------------------------------------------------------------------------------------#
#                                        Functions                                        #
#-----------------------------------------------------------------------------------------#

def ini_values(i,m,x,y,vx,vy,ax,ay,q,Lista):   # Función para asignar valores random en un rango dado
    mas= rd.uniform(m[0],m[1])
    rx = rd.uniform(x[0],x[1])
    ry = rd.uniform(y[0],y[1])
    vx = rd.uniform(vx[0],vx[1])
    vy = rd.uniform(vy[0],vy[1])
    ax = rd.uniform(ax[0],ax[1])
    ay = rd.uniform(ay[0],ay[1])
    q  = rd.uniform(q[0],q[1])
    Lista.append(coloide(i, mas, rx, ry, vx, vy, ax, ay, q))

def export(Lista,nombre,N,i):     # Función para exportar los datos en formato csv
    a = str(nombre) +'_'+ str(i) +'.csv'
    f = open(a, 'w')
    w = csv.writer(f)
    for ide in range(N):
        col=[Lista[ide].ID,Lista[ide].masa,Lista[ide].rx,Lista[ide].ry,Lista[ide].vx,Lista[ide].vy,Lista[ide].ax,Lista[ide].ay,Lista[ide].carga]
        w.writerow(col)
    f.close()