import random
import readchar
import os

POS_X = 0
POS_Y = 1

obstacle_definition = """\
#####################################
#                                  ##
##########                         ##
##############             ##########
########               ##############
##                       ############
#                          ##########
#################                  ##
#################                  ##
#                                  ##
#                                  ##
######       ################      ##
###       ################         ##
#                                  ##
#                                  ## 
#####################################\
"""

my_position = [20, 13]
NUMBER_OBJECTS = 11

tail_length = 0

tail = []
map_objects = []

end_game = None
died = None

# create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
                                            # convierte en una lista a una sttring separada por saltos de linea
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

print(MAP_HEIGHT)
while not end_game:

    os.system("cls")

    # generate position of the objects before to draw in the map and "Draw map"
    while len(map_objects) < NUMBER_OBJECTS:  # len me parminte utlizar una variable por su largo
        new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]  # new position is for objects
        # random.randint genera numeros random en el rango establecido

        if new_position not in map_objects and new_position != my_position:  # not in my position and no in map objects
            map_objects.append(new_position)  # to append in map objects a new position

    # Draw map

    print("+" + "-" * MAP_WIDTH * 2 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")  # end es para cuando se hace el print no haga un salto de linea
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            my_objects = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    my_objects = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if my_objects:
                    map_objects.remove(my_objects)
                    tail_length += 1

                if tail_in_cell:
                    end_game = True
                    died = True

                if my_position[POS_X] == "#" and my_position[POS_Y] == "#":
                    end_game= True
                    died = True
            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"

            print("{} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 2 + "+")

    # ASk user where he wants to move
    # direction = input("a donde desea moverse |w|a|s|d|")

    # readchar allows line break
    direction = readchar.readchar().decode()  # decode transform bits to string

    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        end_game = True

    os.system("cls")

if died == True:
    print("Has muerto")
