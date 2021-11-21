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
import math

#-----------------------------------------------------------------------------------------#
#                                    Global Variables                                     #
#-----------------------------------------------------------------------------------------#

margin = 0
dec = 40

#-----------------------------------------------------------------------------------------#
#                                          Code                                           #
#-----------------------------------------------------------------------------------------#



#-----------------------------------------------------------------------------------------#
#                                         Classes                                         #
#-----------------------------------------------------------------------------------------#

class coloide:  # Clase para las partículas
    def __init__(self, ID, masa, carga, radio, rx, ry, vx, vy, ax, ay):
        self.ID = ID
        self.masa = masa
        self.carga = carga
        self.radio = radio
        self.rx = rx
        self.ry = ry
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay

#-----------------------------------------------------------------------------------------#
#                                        Functions                                        #
#-----------------------------------------------------------------------------------------#

def LowAPF(i,m,q,r,x,y,vx,vy,ax,ay,Lista):   # Función para asignar valores random en un rango dado
    mas= round(rd.uniform(m[0],m[1]),dec)
    car= round(rd.uniform(q[0],q[1]),dec)
    r  = round(rd.uniform(r[0],r[1]),dec)
    rx = round(rd.uniform(x[0],x[1]),dec)
    ry = round(rd.uniform(y[0],y[1]),dec)
    vx = round(rd.uniform(vx[0],vx[1]),dec)
    vy = round(rd.uniform(vy[0],vy[1]),dec)
    ax = round(rd.uniform(ax[0],ax[1]),dec)
    ay = round(rd.uniform(ay[0],ay[1]),dec)
    Lista.append(coloide(i, mas, car, r, rx, ry, vx, vy, ax, ay))

def export(Lista,nombre,N):   # Función para crear un archivo .csv con toda la información de las particulas dadas
    a = str(nombre)+'.csv'
    f = open(a, 'w', newline='')
    w = csv.writer(f)
    w.writerow(["Id", "m", "q","radius","rx","ry","vx","vy","ax","ay"])  # Encabezado
    w.writerow([])
    for ide in range(N):
        col=[Lista[ide].ID,Lista[ide].masa,Lista[ide].carga,Lista[ide].radio,
             Lista[ide].rx,Lista[ide].ry,Lista[ide].vx,Lista[ide].vy,Lista[ide].ax,Lista[ide].ay]
        w.writerow(col)
    f.close()


def HighAPF(n_particles,r_m,r_q,r_r,r_x,r_y,r_vx,r_vy,r_ax,r_ay):
    '''Creates output.csv file with initial values for high atomic packing number.'''
    
    radius = r_r[1] + margin
    x_max = r_x[1]
    y_max = r_y[1]


    lines = math.floor(x_max/(2*radius))
    cols = math.floor(y_max/(2*radius))

    if n_particles > lines*cols:
        print('Too many particles')
        return

    points = []

    for line in range(lines):
        for col in range(cols):
            x_coord = (line*2*radius) + radius
            y_coord = (col*2*radius) + radius
            points.append([x_coord,y_coord])

    while len(points) > n_particles:
        remove_point = rd.randint(0,len(points)-1)
        # print(remove_point)
        points.pop(remove_point)
    
    # print(points)

    particles = []

    for particle in range(n_particles):
        mass= round(rd.uniform(r_m[0],r_m[1]),dec)
        charge = round(rd.uniform(r_q[0],r_q[1]),dec)
        rad  = round(rd.uniform(r_r[0],r_r[1]),dec)
        rx = points[particle][0]
        ry = points[particle][1]
        vx = round(rd.uniform(r_vx[0],r_vx[1]),dec)
        vy = round(rd.uniform(r_vy[0],r_vy[1]),dec)
        ax = round(rd.uniform(r_ax[0],r_ax[1]),dec)
        ay = round(rd.uniform(r_ay[0],r_ay[1]),dec)
        particles.append([particle, mass, charge, rad, rx, ry, vx, vy, ax, ay])

    with open('output.csv','w',newline='') as file:
        data = csv.writer(file)
        data.writerow(["Id", "m", "q","radius","rx","ry","vx","vy","ax","ay"])
        data.writerow([])
        data.writerows(particles)
        data.writerow([])
        data.writerows(particles)
        file.close()

    # print(particles)
    
