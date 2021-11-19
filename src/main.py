#-----------------------------------------------------------------------------------------#
#----------------------------------------  Main  -----------------------------------------#
#-----------------------------------------------------------------------------------------#
#   Date: 11/2021                                                                         #
#   File: main.py                                                                         #
#-----------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------#
#                                        Packages                                         #
#-----------------------------------------------------------------------------------------#

import InitialValues as IV
import TemporalEvolution
import CollisionDetector
import CollisionDynamics

#-----------------------------------------------------------------------------------------#
#                                    Global Variables                                     #
#-----------------------------------------------------------------------------------------#
Nombre='particulas'     # Nombre del archivo donde se exportan los datos

# Rango entre el cual se asignará valores aleatorios a cada característica de la partícula
# i.e. r_m=[0,5] -> todas las partículas tendran un radio aleatorio entre 0 y 5 U

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

#-----------------------------------------------------------------------------------------#
#                                          Code                                           #
#-----------------------------------------------------------------------------------------#

for i in range(N):      # Crear N partículas
    IV.ini_values(i,r_m,r_x,r_y,r_vx,r_vy,r_ax,r_ay,r_q, Coloides)

IV.export(Coloides,Nombre,N,1)    # Exportar archivo con todos los datos