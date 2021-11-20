#-----------------------------------------------------------------------------------------#
#--------------------------------   Equations of motion   --------------------------------#
#-----------------------------------------------------------------------------------------#
#   Date: 11/2021                                                                         #
#   File: TemporalEvolution.py                                                            #
#-----------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------#
#                                        Packages                                         #
#-----------------------------------------------------------------------------------------#

# import csv

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

# k = 1e+2
# dt = 0.01

dec = 2 ##Decimals on aproximations

#-----------------------------------------------------------------------------------------#
#                                          Code                                           #
#-----------------------------------------------------------------------------------------#

def motion(data_block,dt,k):
    '''
    Compute the last block of data, and prints a new one based on the equations of motion.
    '''

    n_particles = len(data_block)

    def pol(p1,p2):

        x1 = float(data_block[p1][x_column])
        y1 = float(data_block[p1][y_column])
        x2 = float(data_block[p2][x_column])
        y2 = float(data_block[p2][y_column])
        dx = x2-x1
        dy = y2-y1
        d = (dx**2+dy**2)**(1/2)

        if d < 0.00000000001:
            d = 0.0001

        unit_x = dx/d
        unit_y = dy/d

        return [d,unit_x,unit_y]

    def EM_force(p1,p2):
        '''
        Calculate electromagnetic force betwen particles with ID p1 and p2, and returns an array with fx and fy.
        '''

        q1 = float(data_block[p1][q_column])
        q2 = float(data_block[p2][q_column])

        polar = pol(p1,p2)
        d = polar[0]
        unit_x = polar[1]
        unit_y = polar[2]


        Fx = -(k*q1*q2*unit_x)/(d**2)
        Fy = -(k*q1*q2*unit_y)/(d**2)

        return [Fx,Fy]


    
    for particle in range(n_particles):
        force_x = 0
        force_y = 0

        for i in range(n_particles):
            if i != particle:
                vec_f = EM_force(particle,i)
                force_x = force_x + vec_f[0]
                force_y = force_y + vec_f[1]
        
        #   Calcula la aceleraciones segun la fuerza neta en cada direccion
        aceleration_x = force_x/float(data_block[particle][mass_column])
        aceleration_y = force_y/float(data_block[particle][mass_column])

        #   Remplaza los valores anteriores de aceleracion por los nuevos valores
        data_block[particle][ax_column] = round(aceleration_x,dec)
        data_block[particle][ay_column] = round(aceleration_y,dec)

    for particle in range(n_particles):
        xo = float(data_block[particle][x_column])
        yo = float(data_block[particle][y_column])
        vxo = float(data_block[particle][vx_column])
        vyo = float(data_block[particle][vy_column])
        axo = float(data_block[particle][ax_column])
        ayo = float(data_block[particle][ay_column])

        xf = xo + vxo*dt + 0.5*axo*dt**2
        yf = yo + vyo*dt + 0.5*ayo*dt**2
        vxf = vxo + axo*dt
        vyf = vyo + ayo*dt

        data_block[particle][x_column] = round(xf,dec)
        data_block[particle][y_column] = round(yf,dec)
        data_block[particle][vx_column] = round(vxf,dec)
        data_block[particle][vy_column] = round(vyf,dec)

    return data_block
