#!/usr/bin/env python3

##### DESCRIPTION:
# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python
# Kata 3kuy
#
# BATTLESHIPS or Sea Battle
#     Write a method that takes a field for well-known board game "Battleship"
#     as an argument and returns true if it has a valid disposition of ships,
#     false otherwise. Argument is guaranteed to be 10*10 two-dimension array.
#     Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.
#
#     Battleship (also Battleships or Sea Battle) is a guessing game for two players.
#     Each player has a 10x10 grid containing several "ships" and objective is to destroy
#     enemy's forces by targetting individual cells on his field. The ship occupies one or
#     more cells in the grid. Size and number of ships may differ from version to version.
#     In this kata we will use Soviet/Russian version of the game.
#
#     Before the game begins, players set up the board and place the ships accordingly to
#     the following rules:
#          -- There must be single battleship (size of 4 cells),
#             2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1).
#             Any additional ships are not allowed, as well as missing ships.
#          -- Each ship must be a straight line, except for submarines,
#              which are just single cell.
#          -- The ship cannot overlap or be in contact with any other ship,
#          neither by edge nor by corner.
#    If you're interested in more information about the game, visit this link:
#        http://en.wikipedia.org/wiki/Battleship_(game)
#
##### NOTES:
# HOLA! I spent a lot of time debugging when I decided to implement the
#      second version of the validate_ships () function to check ships.
#
#      Fuck! I cannot create a copy just using slising lst [:] or list ()
#      or lst.copy () for nested lists.
#
#      Luckily I found a solution (if not writing my own code).
#      This is the module: import copy
#         #line 122:       field = copy.deepcopy (fieldz)
# ADIOS!

import math
import copy

## fields for testing
battleField =[ [ [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

              [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ],

              [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0]
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0]
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
               [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
               [0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
               [0, 0, 1, 0, 1, 1, 1, 0, 1, 0]
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

              [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0]
               [1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
               [0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
               [1, 1, 0, 1, 0, 0, 0, 1, 1, 1]
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
               [1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
               [0, 1, 0, 0, 0, 1, 0, 1, 0, 0]
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 1]] ]

###################################################################################
# The first step is to check the field
###################################################################################
def validate_field(field):
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x]:  # if 1 (assuming True)
            # Check diagonals using cos and sin
            # Por que? Porque Yo se :)
            # A point on the coordinate plane is defined as
            # (cos (), sin ()) equal (x,y)
                for deg in range(45, 360, 90):
                    cosx = round(math.cos(math.radians(deg)))
                    siny = round(math.sin(math.radians(deg)))
                    if 0 <= y + siny < 10 and 0 <= x + cosx < 10:
                        if field[y + siny][x + cosx]:
                            return False
                # Preparing for vertically and horizontally validation
                # We know that cos (0) = 1 cos (90) = 0 cos (180) = - 1 cos (270) = 0
                #              sin (0) = 0 sin (90) = 1 sin (180) = 0 sin (270) = - 1
                # but the plane is transformed:
                #              flips over the Y-axis and rotates 180 degrees
                # Luckily You can use just movements without bothering with math
                #                -1
                #            -1 <-^-> 1
                #                 V
                #                 1
                if x + 1 > 9: expOne = False
                else:  expOne = bool(field[y][x + 1])

                if x - 1 < 0: expTwo = False
                else: expTwo = bool(field[y][x - 1])

                if y - 1 < 0: expThree = False
                else: expThree = bool(field[y - 1][x])

                if y + 1 > 9: expFour = False
                else: expFour = bool(field[y + 1][x])

                # And finally Check vertically and horizontally
                if (expOne or expTwo) and (expThree or expFour):
                    return False
    return True
###################################################################################
# FOR VALIDATION SHIPS  old version
# saved for testing
###################################################################################
def validate_ships_ver01(fieldz):
    ships = {'submarines': 0, 'destroyers': 0,
             'cruisers': 0, 'battleship': 0}
    #CREATE COPY. The list will be changed
    # Fuck!
    # https://www.geeksforgeeks.org/python-list-copy-method/
    # "shallow copy - changes to nested list is reflected,
    # " same as copy.copy(), slicing...
    # " deep copy - no change is reflected "
    field = copy.deepcopy(fieldz)
    #Check ships size
    for y in range(len(field)):
        for x in range(len(field)):
            #Quite first point only
            if field[y][x]:
                size = 1
                #Inspection horizontally
                while x + size < 10 and field[y][x + size]:
                    field[y][x + size] = 0
                    size += 1
                #Inspection vertically
                if size == 1:
                    while y + size < 10 and field[y + size][x]:
                        field[y + size][x] = 0
                        size += 1
                # and save result of inspection
                if size == 1:
                    ships['submarines'] += 1
                elif size == 2:
                    ships['destroyers'] += 1
                elif size == 3:
                    ships['cruisers'] += 1
                elif size == 4:
                    ships['battleship'] += 1
                    
    return ships['submarines'] == 4 and ships['destroyers'] == 3 \
       and ships['cruisers'] == 2 and ships['battleship'] == 1

 
###################################################################################  
# FOR VALIDATION SHIPS
# I thought i would just get the sum <of arrays>
# and compare against the checksum.
# This seems to be a simpler solution
#  Look below: ####################################################################
def validate_ships_ver02(fieldz):
    BATTLESHIP = 4 * 1
    CRUISER    = 3 * 2
    DESTROYER = 2 * 3
    SUBMARINE  = 4 * 1
    checksum = BATTLESHIP + CRUISER + DESTROYER + SUBMARINE
    s = 0

    for i in fieldz:
        s +=sum(i)

    return s == checksum
#Ya :)

###################################################################################
#  I implimented two functions for testing
#  This is ONE
###################################################################################
def validate_battlefield01(field):
    if not validate_field(field):
        return False
    if not validate_ships_ver01(field):
        return False
    return True

###################################################################################
# and TWO is here
###################################################################################
def validate_battlefield02(field):
    if not validate_field(field):
        return False
    if not validate_ships_ver02(field):
        return False
    return True

#----------------------------------------------------------------------------------
#   Let's go
#----------------------------------------------------------------------------------
if __name__ == "__main__":
    for i in battleField:
        print(validate_battlefield01(i))

    for i in battleField:
        print(validate_battlefield02(i))

