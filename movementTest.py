'''
Developed by Cristiano Porretta
'''

from os import system
from msvcrt import getch
from random import randint
from time import sleep

# initialize playspace
columns = [["-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-"]]

playing = True

# initialize character data
character = "55"
charCol = int(character[0]) - 1
charRow = int(character[1]) - 1

# initializes item data
itemCol = randint(0, 8)
itemRow = randint(0, 8)

# initializes enemy data
enemyCol = randint(0, 8)
enemyRow = randint(0, 8)

# initialize score data
currentScore = 0
highScore = 0

def render(charCol, charRow, charIcon):
    '''
    renders object in map.

    Args:
        charCol: int value for objects y position.
        charRow: int value for objects x position.
        charIcon: string character to represent object.
    '''
    global columns
    columns[charCol].pop(charRow)
    columns[charCol].insert(charRow, charIcon)

def move(direction):
    '''
    Moves character

    Args:
        direction: String detailing the direction character will move in.
    '''
    print(direction)
    global charCol, charRow, playing
    if charCol != 0 and direction == "w":
        charCol -= 1
    elif charCol != 8 and direction == "s":
        charCol += 1
    elif charRow != 0 and direction == "a":
        charRow -= 1
    elif charRow != 8 and direction == "d":
        charRow += 1
    elif direction not in ["w", "s", "a", "d"]:
        playing = False

def enemyMove():
    '''
    Moves enemy based on character position.
    '''
    global columns, enemyCol, enemyRow
    columns[enemyCol].pop(enemyRow)
    columns[enemyCol].insert(enemyRow, "-")
    # moves enemy in cardinal direction, not on item
    if randint(0,1) == 1:
        if enemyCol < charCol:
            enemyCol += 1
        else:
            enemyCol -= 1
    else:
        if enemyRow < charRow:
            enemyRow += 1
        else:
            enemyRow -= 1

def itemGet():
    '''
    Erases item from map and generates new location.
    '''
    global columns, itemCol, itemRow
    columns[itemCol].pop(itemRow)
    columns[itemCol].insert(itemRow, "-")
    # generates new item location different from tile character is on
    while(itemCol == charCol and itemRow == charRow):
        itemCol = randint(0, 8)
        itemRow = randint(0, 8)

# welcome text
print("WASD to move. Any other input will quit program.\nCollect 'E', avoid 'Q'\n")

# main loop
while(True):
    while(playing):

        # inserts character and item into map
        render(itemCol, itemRow, "E")
        render(enemyCol, enemyRow, "Q")
        render(charCol, charRow, "@")

        # generates map
        i = 0
        for row in columns:
            for tile in row:
                if i != 0:
                    print(" " + tile + " ", end="")
                else:
                    print(tile + " ", end="")
                i += 1
            i = 0
            print()

        # erases character from map
        columns[charCol].pop(charRow)
        columns[charCol].insert(charRow, "-")
    
        # collects input for character movement, moves character
        move(getch().decode())

        enemyMove()

        # clears output
        system('cls')

        # detects item and character collision
        if charCol == itemCol and charRow == itemRow:
            itemGet()
            currentScore += 1
            if currentScore > highScore:
                highScore = currentScore

        # detects enemy and character collision
        if charCol == enemyCol and charRow == enemyRow:
            for num in range(0,4):
                # inserts character and item into map
                render(itemCol, itemRow, "E")
                render(enemyCol, enemyRow, "Q")

                # generates map
                print("\n\n")
                i = 0
                for row in columns:
                    for tile in row:
                        if i != 0:
                            print(" " + tile + " ", end="")
                        else:
                            print(tile + " ", end="")
                        i += 1
                    i = 0
                    print()
                sleep(.5)
                system('cls')

                # inserts character and item into map
                render(itemCol, itemRow, "E")
                render(enemyCol, enemyRow, "@")

                # generates map
                print("\n\n")
                i = 0
                for row in columns:
                    for tile in row:
                        if i != 0:
                            print(" " + tile + " ", end="")
                        else:
                            print(tile + " ", end="")
                        i += 1
                    i = 0
                    print()
                sleep(.5)
                system('cls')

            # inserts character and item into map
            render(itemCol, itemRow, "E")
            render(enemyCol, enemyRow, "Q")

            # generates map
            i = 0
            for row in columns:
                for tile in row:
                    if i != 0:
                        print(" " + tile + " ", end="")
                    else:
                        print(tile + " ", end="")
                    i += 1
                i = 0
                print()
            sleep(1)
            break

        # prints character coordinates and score data
        print("x: %i             Score: %i\ny: %i\n" % (charRow, currentScore, charCol))

    # lose state message
    print("Game Over\n\nFinal Score:", currentScore)
    if input("Play again? (y/n): ").lower() != "y":
        system('cls')
        break

# log off message
system('cls')
print("Thanks for playing!")
