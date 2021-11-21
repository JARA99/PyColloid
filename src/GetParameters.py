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


# with open('Parameters.txt','r') as file:
#     Case = file.readline().replace('Case: ','')
#     Particles = int(file.readline().replace('Particles: ',''))
#     Mass = float(file.readline().replace('Mass: ',''))
#     MaxCharge = float(file.readline().replace('MaxCharge: ',''))
#     MinCharge = float(file.readline().replace('MinCharge: ',''))
#     MaxRadius = float(file.readline().replace('MaxRadius: ',''))
#     MinRadius = float(file.readline().replace('MinRadius: ',''))
#     MaxX = float(file.readline().replace('MaxX: ',''))
#     MinX = 0
#     MaxY = float(file.readline().replace('MaxY: ',''))
#     MinY = 0



# print(Case,Particles,Mass)


def AutoGnuplot(MaxX,MaxY,Palette,InvertPalette,DeltaTime):
    '''Automatic change of parameters on Gnuplot'''

    dt = int(DeltaTime*100)

    # if dt <= 0:
    #     dt = 1

    with open('Plot.gp','r') as GPfile:
        GPlist = GPfile.readlines()
        # print(GPlist[2])

        GPlist[3] = "load 'gnuplot-palettes/" + Palette + ".pal'\n"
        # print(GPlist[2])

        if InvertPalette:
            GPlist[4] = "set palette negative\n"
            # print('Palette set negative')
        else:
            GPlist[4] = "set palette positive\n"
        
        size_x = int(MaxX*(800+140))
        size_y = int(MaxY*(800))

        GPlist[6] = "set terminal gif enhanced font Arial 12 animate delay " + str(dt) + " size " + str(size_x) + ',' + str(size_y) + '\n'

        GPlist[14] = "set xrange [0:" + str(MaxX) + "]\n"
        GPlist[15] = "set yrange [0:" + str(MaxY) + "]\n"

        GPlist[23] = "set terminal png enhanced font Arial 12 size " + str(2*size_x) + "," + str(size_y) + '\n'

        NewGP = open('PlotCopy.gp','w')

        NewGP.writelines(GPlist)

        # print(GPlist)
        

# AutoGnuplot(0.8,0.8,'rdbu',False)