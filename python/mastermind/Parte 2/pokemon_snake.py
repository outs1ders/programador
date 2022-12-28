import random
import readchar
import os

POS_X = 0
POS_Y = 1

obstacle_difinition = """\
#################################
#                               #
#######                         #
#######                 #########
#######                 #########
#                       #########
#                               #
##################              #
#                               #
#                               #
##################              #
####                            #
#            ##############     #
#         ##############        #
####                            #
#                          ######
#                        ########
#################################
"""

my_position= [1,2]
NUMBER_OF_FIGHTER = 5

map_fighters=[]
end_game= None
died= None

# create obstacle map
obstacle_definition = [list(row) for row in obstacle_difinition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# generate position of the fighters before to draw in the map and "Draw map"
while len(map_fighters) < NUMBER_OF_FIGHTER:
    new_position_fighters = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

    if new_position_fighters not in map_fighters and new_position_fighters != my_position:
        map_fighters.append(new_position_fighters)
