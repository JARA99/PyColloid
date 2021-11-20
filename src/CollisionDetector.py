#-----------------------------------------------------------------------------------------#
#--------------------------------   Collision Detector   ----------------------------------#
#-----------------------------------------------------------------------------------------#
#   Date: 11/2021                                                                         #
#   File: CollisionDetector.py                                                                         #
#-----------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------#
#                                        Packages                                         #
#-----------------------------------------------------------------------------------------#

import csv
from types import DynamicClassAttribute
import CollisionDynamics

#-----------------------------------------------------------------------------------------#
#                                    Global Variables                                     #
#-----------------------------------------------------------------------------------------#

id_column = 0
mass_column = 1
q_column = 2
radius_column = 3
x_column = 4
y_column = 5
vx_column = 6
vy_column = 7
ax_column = 8
ay_column = 9

max_cicles = 15

#-----------------------------------------------------------------------------------------#
#                                          Code                                           #
#-----------------------------------------------------------------------------------------#

def detect(Lista,Lista_out,N,delta):
    for ide1 in range(N):
        for ide2 in range(ide1):            # Se compara hasta ide1 para evitar que se repita el análisis de choque
            if abs(Lista[ide1].rx-Lista[ide2].rx)<delta and abs(Lista[ide1].ry-Lista[ide2].ry)<delta :
                Lista_out.append([Lista[ide1].ID,Lista[ide2].ID])
                # en vez de hacer un append se puede sustituir por la función que corrige las direcciones después del choque
                # y se detiene una vez detecte al primer par de particulas colisionando


def collisions(data_block):
    n_particles = len(data_block)
    # last_data_block = data_block.copy()

    velocity_unchanged = [True]*n_particles
    position_unfixed = [True]*n_particles

    def pol(p1,p2):

        x1 = float(data_block[p1][x_column])
        y1 = float(data_block[p1][y_column])
        x2 = float(data_block[p2][x_column])
        y2 = float(data_block[p2][y_column])
        dx = x2-x1
        dy = y2-y1
        d = (dx**2+dy**2)**(1/2)

        unit_x = dx/d
        unit_y = dy/d

        return [d,unit_x,unit_y]


    ################################### Change velocities #####################################
    ###########################################################################################

    for particle in range(n_particles):
        if velocity_unchanged[particle]:
            radius = float(data_block[particle][radius_column])

            for i in range(n_particles):
                if velocity_unchanged[i]:
                    polar = pol(particle,i)
                    d = polar[0]
                    dmin = radius + float(data_block[i][radius_column])

                    if d < dmin:
                        particle_vx = data_block[particle][vx_column]
                        particle_vy = data_block[particle][vy_column]

                        data_block[particle][vx_column] = data_block[i][vx_column]
                        data_block[particle][vy_column] = data_block[i][vy_column]
                        data_block[i][vx_column] = particle_vx
                        data_block[i][vy_column] = particle_vy

                        velocity_unchanged[particle] = False
                        velocity_unchanged[i] = False


    #################################### Change positions #####################################
    ###########################################################################################

    for particle in range(n_particles):
        radius = float(data_block[particle][radius_column])

        check = True
        checks = 0

        while check:
            check = False
            checks += 1 
            for i in range(n_particles):
                polar = pol(particle,i)
                d = polar[0]
                dmin = radius + float(data_block[i][radius_column])

                if d < dmin:
                    check = True

            
            if checks > max_cicles:
                print('This particle has too many collisions')
                break
