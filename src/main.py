#-----------------------------------------------------------------------------------------#
#----------------------------------------  Main  -----------------------------------------#
#-----------------------------------------------------------------------------------------#
#   Date: 11/2021                                                                         #
#   File: main.py                                                                         #
#-----------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------#
#                                        Packages                                         #
#-----------------------------------------------------------------------------------------#

import InitialValues as iv
import TemporalEvolution as tevo
import CollisionDetector as cdet
import CollisionDynamics
import DataHandle as dh

#-----------------------------------------------------------------------------------------#
#                                    Global Variables                                     #
#-----------------------------------------------------------------------------------------#
Nombre='output'         # Nombre del archivo donde se exportan los datos

# Rango entre el cual se asignará valores aleatorios a cada característica de la partícula
# i.e. r_m=[0,5] -> todas las partículas tendran una masa aleatoria entre 0 y 5 U

r_m =[0,1]              # rango masa
r_x =[0,1]              # rango posición x
r_y =[0,1]              # rango posición y
r_vx=[0,1]              # rango velocidad x
r_vy=[0,1]              # rango velocidad y
r_ax=[0,1]              # rango aceleración x
r_ay=[0,1]              # rango aceleración y
r_q =[0,1]              # rango carga

Coloides=[]             # Lista para almacenar todas las partículas

N=10                    # Cantidad de partículas a considerar
delta_c=0.2             # diferencia dentro de la cual se considera como choque

Chocando=[]

#-----------------------------------------------------------------------------------------#
#                                          Code                                           #
#-----------------------------------------------------------------------------------------#

for i in range(N):      # Crear N partículas
    iv.ini_values(i,r_m,r_x,r_y,r_vx,r_vy,r_ax,r_ay,r_q, Coloides)

iv.export(Coloides,Nombre,N)    # Exportar archivo con todos los datos

cdet.detect(Coloides,Chocando,N,delta_c)      # Se recorre todas las partículas para saber cuales están superpuestas
print("delta=",delta_c)
print(Chocando)

for a in Coloides:             # Se recorre la lista creada para observar determinadas características
  print("ID=",a.ID,"rx=",a.rx,"ry=",a.ry)


##  Probando funcionalidad de evolucion temporal

block = dh.getLastBlock(N)        # Guarda el ultimo bloque en una lista

print(block)                   # Imprime
print('\n\n')

newblock = tevo.motion(block)     # Aplica la evolucion temporal y guarda este bloque en otra lista

print(block)                   # Imprime
print('\n\n')
print(newblock)