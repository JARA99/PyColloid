#-----------------------------------------------------------------------------------------#
#---------------------------------   Get Parameters   ------------------------------------#
#-----------------------------------------------------------------------------------------#
#   Date: 11/2021                                                                         #
#   File: GetParameters.py                                                                         #
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


with open('Parameters.txt','r') as file:
    Case = file.readline().replace('Case: ','')
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



print(Case,Particles,Mass)
