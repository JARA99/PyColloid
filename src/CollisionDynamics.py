#-----------------------------------------------------------------------------------------#
#--------------------------------   Collision Dynamics   ----------------------------------#
#-----------------------------------------------------------------------------------------#
#   Date: 11/2021                                                                         #
#   File: CollisionDynamics.py                                                                         #
#-----------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------#
#                                        Packages                                         #
#-----------------------------------------------------------------------------------------#



#-----------------------------------------------------------------------------------------#
#                                    Global Variables                                     #
#-----------------------------------------------------------------------------------------#



#-----------------------------------------------------------------------------------------#
#                                          Code                                           #
#-----------------------------------------------------------------------------------------#

#   PP stands for Particle-Particles
def PP_Collision(v1_x,v1_y,v2_x,v2_y):
    '''
    Returns an array with the velocities after a colision between a two particles.
    '''
    #   Since we have same masses and no enery loss:
    return [v2_x,v2_y,v1_x,v1_y]

#   PW stands for Particle-Wall
def PW_Collision(v_x,v_y,wall):
    '''
    Returns an array with the velocity after a collision between a particle and a wall.
    '''

    #   When the wall is horizontal, the y component of the velocity inverts
    if wall == "x":
        return [v_x,-v_y]

    #   When the wall is vertical, the x component of the velocity inverts
    elif wall == "y":
        return [-v_x,v_y]

    #   Leave this here just for aesthetics
    else:
        return [v_x,v_y]
