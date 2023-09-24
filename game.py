import os
import random
import sys

from Grid import *


if __name__ == '__main__':
    initialFlag = True
    gridObject = Grid()
    try:
        size = int(sys.argv[1])
    except Exception as e:
        print(e)
        print("Wrong input please enter a number from 2,4,6 as grid size")
        exit(0)

    if size != 2 and size != 4 and size != 6:
        print("Wrong input please enter a number from 2,4,6 as grid size")
        exit(0)

    while True:

        gridObject.menuSkeleton(size, initialFlag)
        try:
            initialFlag = False
            choice = int(input("Select: "))

        except:
            print("Wrong input")
            continue

        if choice == 1:
            gridObject.switchOption1()
            continue

        elif choice == 2:
            gridObject.switchOption2()
            continue

        elif choice == 3:
            gridObject.switchOption3(initialFlag)
            exit(0)

        elif choice == 4:
            os.system("clear")
            initialFlag = True
            continue

        elif choice == 5:
            print("Thanks for playing")
            exit(0)

        else:
            print("Please enter a valid option between 1 to 4")
            print()
