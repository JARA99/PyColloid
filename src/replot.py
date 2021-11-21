#-----------------------------------------------------------------------------------------#
#----------------------------------------  Main  -----------------------------------------#
#-----------------------------------------------------------------------------------------#
#   Date: 11/2021                                                                         #
#   File: main.py                                                                         #
#-----------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------#
#                                        Packages                                         #
#-----------------------------------------------------------------------------------------#

# from math import pi
# import InitialValues as iv
# import TemporalEvolution as tevo
# import CollisionDetector as cdet
# import CollisionDynamics
# import DataHandle as dh
import GetParameters as gpar

#-----------------------------------------------------------------------------------------#
#                                    Global Variables                                     #
#-----------------------------------------------------------------------------------------#
Nombre='output'         # Nombre del archivo donde se exportan los datos

cicles = 100

# Rango entre el cual se asignará valores aleatorios a cada característica de la partícula
# i.e. r_m=[0,5] -> todas las partículas tendran una masa aleatoria entre 0 y 5 U

r_m =[0,1]              # rango masa
r_q =[-1,1]             # rango carga
r_r =[0.04,0.06]        # rango del radio
r_x =[0,0.7]            # rango posición x
r_y =[0,0.6]            # rango posición y
r_vx=[-10,10]             # rango velocidad x
r_vy=[-10,10]             # rango velocidad y
r_ax=[0,0]              # rango aceleración x
r_ay=[0,0]              # rango aceleración y

Coloides = []           # Lista para almacenar todas las partículas
radio = 0.05               # Radio de cada partícula
N=10                    # Cantidad de partículas a considerar

Chocando=[]

#-----------------------------------------------------------------------------------------#
#                                   Reading Parameters                                    #
#-----------------------------------------------------------------------------------------#


with open('../Parameters.txt','r') as file:
    Case = file.readline().replace('Case: ','').replace('\n','')
    Apf = float(file.readline().replace('APF: ',''))
    Particles = int(file.readline().replace('Particles: ',''))
    Mass = float(file.readline().replace('Mass: ',''))
    MaxCharge = float(file.readline().replace('MaxCharge: ',''))
    MinCharge = float(file.readline().replace('MinCharge: ',''))
    MaxRadius = float(file.readline().replace('MaxRadius: ',''))
    MinRadius = float(file.readline().replace('MinRadius: ',''))
    MaxX = float(file.readline().replace('MaxX: ',''))
    MinX = 0
    MaxY = float(file.readline().replace('MaxY: ',''))
    MinY = 0
    MaxV = float(file.readline().replace('MaxVo: ',''))
    # MinV = float(file.readline().replace('MinV: ',''))
    ForceConstant = float(file.readline().replace('ForceConstant: ',''))
    DeltaTime = float(file.readline().replace('DeltaTime: ',''))
    Iterations = int(file.readline().replace('Iterations: ',''))
    CollisionLoops = float(file.readline().replace('CollisionLoops: ',''))
    Palette = file.readline().replace('Palette: ','').replace('\n','')
    InvertPalette = file.readline().replace('Invert: ','')
    file.close()

if InvertPalette == 'True':
    InvertPalette = True
else:
    InvertPalette = False

N = Particles
r_m =[Mass,Mass]              # rango masa
r_q =[MinCharge,MaxCharge]    # rango carga
r_r =[MinRadius,MaxRadius]    # rango del radio
r_x =[MinX,MaxX]              # rango posición x
r_y =[MinY,MaxY]              # rango posición y

cicles = Iterations

#-----------------------------------------------------------------------------------------#
#                                          Code                                           #
#-----------------------------------------------------------------------------------------#

# print(InvertPalette)

gpar.AutoGnuplot(MaxX,MaxY,Palette,InvertPalette,DeltaTime)

