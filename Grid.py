import os
import random
import time


class Grid:
    # global variables and matrix
    matrix_with_digits = []
    matrix_without_digits = []
    size = 0
    flag = True
    occuredElementSet = set()
    actualGuesses = 0
    minimumGuessesRequired = 0
    cheatingFlag = False

    def __init__(self):
        self.matrix_without_digits = []
        self.matrix_with_digits = []
        self.menuOptions = {
            1: 'Let me select two elements',
            2: 'Uncover one element for me',
            3: 'I give up - reveal the grid',
            4: 'New Game',
            5: 'Exit',
        }
        self.size = 0
        self.occuredElementSet = set()
        self.minimumGuessesRequired = 0
        self.actualGuesses = 0
        self.cheatingFlag = False

    # function for printing the user UI skeleton
    def menuSkeleton(self, size, initialFlag):
        self.size = size
        print("-------------------------------")
        print("|          PEEK-A-BOO         |")
        print("-------------------------------")
        for key in self.menuOptions.keys():
            print(key, '.', self.menuOptions[key])
        print()

        self.printInitialColumnHeading()
        self.matrixWithoutDigits(initialFlag)
        self.matrixWithDigits(initialFlag)

    # functions for user options
    def switchOption1(self):
        while True:

            cell1 = input("Enter the first cell coordinates (e.g., a0): ")
            cell2 = input("Enter the second cell coordinates (e.g., a0): ")
            col1 = ord(cell1.lower()[0]) - 96
            row1 = int(cell1[1])
            col2 = ord(cell2.lower()[0]) - 96
            row2 = int(cell2[1])
            try:

                if len(cell1) == 2 and len(cell2) == 2:
                    if self.size == 2:
                        if (cell1.lower()[0] and cell2.lower()[0] in ['a', 'b']) and (
                                cell1[1] and cell2[1] in ['0', '1']):
                            self.actualGuesses = self.actualGuesses + 1
                            element1 = self.matrix_with_digits[row1][col1]
                            element2 = self.matrix_with_digits[row2][col2]

                            if element2 == element1:
                                self.matrix_without_digits[row1][col1] = self.matrix_with_digits[row1][col1]
                                self.matrix_without_digits[row2][col2] = self.matrix_with_digits[row2][col2]
                                self.occuredElementSet.add(cell1)
                                self.occuredElementSet.add(cell2)
                                break

                            startTime = time.time()
                            self.matrix_without_digits[row1][col1] = self.matrix_with_digits[row1][col1]
                            self.matrix_without_digits[row2][col2] = self.matrix_with_digits[row2][col2]

                            self.printInitialColumnHeading()
                            self.matrixWithoutDigits(False)
                            time.sleep(2)

                            if cell1 not in self.occuredElementSet:
                                self.matrix_without_digits[row1][col1] = 'X'

                            if cell2 not in self.occuredElementSet:
                                self.matrix_without_digits[row2][col2] = 'X'

                            os.system("clear")
                            break
                        else:
                            print("Input error: column entry is out of range for this grid. Please try again.")

                    elif self.size == 4:
                        if (cell1.lower()[0] and cell2.lower()[0] in ['a', 'b', 'c', 'd']) and (
                                cell1[1] and cell2[1] in ['0', '1', '2', '3']):
                            self.actualGuesses = self.actualGuesses + 1
                            element1 = self.matrix_with_digits[row1][col1]
                            element2 = self.matrix_with_digits[row2][col2]

                            if element2 == element1:
                                self.matrix_without_digits[row1][col1] = self.matrix_with_digits[row1][col1]
                                self.matrix_without_digits[row2][col2] = self.matrix_with_digits[row2][col2]
                                self.occuredElementSet.add(cell1)
                                self.occuredElementSet.add(cell2)
                                break

                            startTime = time.time()

                            self.matrix_without_digits[row1][col1] = self.matrix_with_digits[row1][col1]
                            self.matrix_without_digits[row2][col2] = self.matrix_with_digits[row2][col2]

                            self.printInitialColumnHeading()
                            self.matrixWithoutDigits(False)
                            time.sleep(2)

                            if cell1 not in self.occuredElementSet:
                                self.matrix_without_digits[row1][col1] = 'X'

                            if cell2 not in self.occuredElementSet:
                                self.matrix_without_digits[row2][col2] = 'X'

                            os.system("clear")
                            break
                        else:
                            print("Input error: column entry is out of range for this grid. Please try again.")
                    elif self.size == 6:
                        if (cell1.lower()[0] and cell2.lower()[0] in ['a', 'b', 'c', 'd', 'e', 'f']) and (
                                cell1[1] and cell2[1] in ['0', '1', '2', '3', '4', '5']):
                            element1 = self.matrix_with_digits[row1][col1]
                            element2 = self.matrix_with_digits[row2][col2]
                            self.actualGuesses = self.actualGuesses + 1

                            if element2 == element1:
                                self.matrix_without_digits[row1][col1] = self.matrix_with_digits[row1][col1]
                                self.matrix_without_digits[row2][col2] = self.matrix_with_digits[row2][col2]
                                self.occuredElementSet.add(cell1)
                                self.occuredElementSet.add(cell2)
                                break

                            startTime = time.time()

                            self.matrix_without_digits[row1][col1] = self.matrix_with_digits[row1][col1]
                            self.matrix_without_digits[row2][col2] = self.matrix_with_digits[row2][col2]

                            self.printInitialColumnHeading()
                            self.matrixWithoutDigits(False)
                            time.sleep(2)
                            if cell1 not in self.occuredElementSet:
                                self.matrix_without_digits[row1][col1] = 'X'

                            if cell2 not in self.occuredElementSet:
                                self.matrix_without_digits[row2][col2] = 'X'

                            os.system("clear")
                            break
                        else:
                            print("Input error: column entry is out of range for this grid. Please try again.")
                else:
                    print("Input error: column entry is out of range for this grid. Please try again.")
            except Exception as e:
                print(e)

        if len(self.occuredElementSet) == self.size * self.size:
            self.printInitialColumnHeading()
            for row in self.matrix_without_digits:
                print('  '.join(str(num) for num in row))
            score = self.result()
            if self.cheatingFlag:
                print("You cheated - Loser! You 're score is 0!")
                exit(0)

            else:
                print("Oh Happy Day. You 've won!! You score is:", score)
                exit(0)

    def switchOption2(self):
        self.cheatingFlag = True
        while True:
            cell1 = input("Enter the first cell coordinates (e.g., a0): ")
            col1 = ord(cell1.lower()[0]) - 96
            row1 = int(cell1[1])
            try:
                if len(self.occuredElementSet) == self.size * self.size:
                    score = self.result()
                    if self.cheatingFlag:
                        print("You cheated - Loser! You 're score is 0!")
                        break

                    else:
                        print("Oh Happy Day. You 've won!! You score is:", score)
                        break
                if len(cell1) == 2:
                    if self.size == 2:
                        if (cell1.lower()[0] in ['a', 'b']) and (cell1[1] in ['0', '1']):
                            self.matrix_without_digits[row1][col1] = self.matrix_with_digits[row1][col1]
                            self.occuredElementSet.add(cell1)
                            break
                        else:
                            print("Input error: column entry is out of range for this grid. Please try again.")

                    elif self.size == 4:
                        if (cell1.lower()[0] in ['a', 'b', 'c', 'd']) and (cell1[1] in ['0', '1', '2', '3']):
                            self.matrix_without_digits[row1][col1] = self.matrix_with_digits[row1][col1]
                            self.occuredElementSet.add(cell1)
                            break
                        else:
                            print("Input error: column entry is out of range for this grid. Please try again.")

                    elif self.size == 6:
                        if (cell1.lower()[0] in ['a', 'b', 'c', 'd', 'e', 'f']) and (
                                cell1[1] in ['0', '1', '2', '3', '4', '5']):
                            self.matrix_without_digits[row1][col1] = self.matrix_with_digits[row1][col1]
                            self.occuredElementSet.add(cell1)
                            break
                        else:
                            print("Input error: column entry is out of range for this grid. Please try again.")
                else:
                    print("Input error: column entry is out of range for this grid. Please try again.")
            except Exception as e:
                print(e)

        if len(self.occuredElementSet) == self.size * self.size:
            self.printInitialColumnHeading()
            for row in self.matrix_without_digits:
                print('  '.join(str(num) for num in row))
            score = self.result()
            if self.cheatingFlag:
                print("You cheated - Loser! You 're score is 0!")
                exit(0)

            else:
                print("Oh Happy Day. You 've won!! You score is:", score)
                exit(0)


    def switchOption3(self, initialFlag):
        self.printInitialColumnHeading()
        for row in self.matrix_with_digits:
            print('  '.join(str(num) for num in row))
        print("Grid Revealed, You 're score is 0!")

    def matrixWithDigits(self, initialFlag):
        global matrix_with_digits

        if initialFlag:

            if self.size != 2:
                numbers_in_list = list(range((self.size * self.size) // 2)) * 2
            elif self.size == 2:
                numbers_in_list = list(range(self.size)) * 2
            random.shuffle(numbers_in_list)
            self.matrix_with_digits = [[[i // self.size]] + numbers_in_list[i:i + self.size] for i in
                                       range(0, self.size * self.size,
                                             self.size)]

    # initializes the matrix with 'X' hiding the number in the matrix
    def matrixWithoutDigits(self, initialFlag):
        global matrix_without_digits

        if initialFlag:
            if self.size != 2:
                numbers_in_list = ['X'] * ((self.size * self.size) // 2) * 2
            elif self.size == 2:
                numbers_in_list = ['X'] * self.size * 2
            random.shuffle(numbers_in_list)
            self.matrix_without_digits = [[[i // self.size]] + numbers_in_list[i:i + self.size] for i in
                                          range(0, self.size * self.size, self.size)]

            for row in self.matrix_without_digits:
                print('  '.join(str(num) for num in row))

        else:
            for row in self.matrix_without_digits:
                print('  '.join(str(num) for num in row))

    # function for printing the user UI skeleton
    def printInitialColumnHeading(self):
        first_line = []
        for i in range(0, self.size):
            if i == 0:
                first_line.append("  ")

            first_line.append(("[" + chr(i + 65) + "]"))
        print(" ".join(first_line))

    def result(self):
        self.minimumGuessesRequired = (self.size * self.size) / 2
        score = (self.minimumGuessesRequired / self.actualGuesses) * 100

        return score
