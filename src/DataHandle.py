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

#-----------------------------------------------------------------------------------------#
#                                    Global Variables                                     #
#-----------------------------------------------------------------------------------------#



#-----------------------------------------------------------------------------------------#
#                                          Code                                           #
#-----------------------------------------------------------------------------------------#

def getLastBlock(n_particles):
    '''
    Reads the last block of data and put it in a list.
    '''

    total_list = []
    sub_list = []

    with open('output.csv','r') as file:

        data = csv.reader(file)
        # print(data)
        tot = data.line_num 

        start = tot - n_particles

        for row in data:
            total_list.append(row)

    for i in range(start,tot):
        sub_list.append(total_list[i])
        
    return sub_list
