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
import CollisionDynamics

#-----------------------------------------------------------------------------------------#
#                                    Global Variables                                     #
#-----------------------------------------------------------------------------------------#



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