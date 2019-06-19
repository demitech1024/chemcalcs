import sys
import math
import re

def balanceEquation(leftList, rightList):
    i = 0
    findAllListRight = []
    findAllListLeft = []
    numberRight = []
    numberLeft = []
    while i < (len(rightList) - 1):
        findAllListRight.append(re.findall('[A-Z][^A-Z]*', rightList[i]))
        i = i + 1
    i = 0
    print(findAllListRight)
    while i < (len(leftList) - 1):
        findAllListLeft.append(re.findall('[A-Z][^A-Z]*', leftList[i]))
        i = i + 1
    i = 0
    print(findAllListLeft)
    numberRight = [findAllListRight[0][i].split('[0-9]') for i in range(0, len(findAllListRight[0]))]
    print(numberRight)
    i = 0
    numberLeft = [findAllListLeft[0][i].split('[0-9]') for i in range(0, len(findAllListLeft[0]))]
    print(numberLeft)
    return [leftList, rightList]

def scientificString(string):
    stringList = list(string)
    i = 0
    while i < len(stringList):
        if stringList[i] == "^":
            stringList[i] = "**"
            returnVar = ''.join(stringList)
            return eval(returnVar)
        i = i + 1
    returnVar = ''.join(stringList)
    return eval(returnVar)

def iceSolver():
    print("#  Determine the type of the reaction.")
    print("#  Note: As of the current version of this application (0.8.9), only acid and base ICE table solvers are functional.")
    reactionType = input("#  (Types include acid, base, general, or buffer):  ")
    if reactionType == "general":
        generalIce()
    print("")
    main()

def generalIce():
    correctEq = False
    while correctEq == False:
        leftSide = int(input("#  How many compounds are on the left side of the equation? \n#  (maximum of 3):  "))
        leftSideComp = []
        rightSideComp = []
        rightSideCoef = []
        leftSideCoef = []
        compounds = []
        rightSide = int(input("#  How many compounds are on the right side of the equation? \n#  (maximum of 3):  "))
        print("#  From left to right, enter the coeffecient and compounds of the equation.")
        ratios = []
        i = 0
        while i < (leftSide + rightSide):
            if i == 0:
                ratios.append(int(input("#  Enter 1st coeffecient:  ")))
                compounds.append(input("#  Enter 1st compound:  "))
            elif i == 1:
                ratios.append(int(input("#  Enter 2nd coeffecient:  ")))
                compounds.append(input("#  Enter 2nd compound:  "))
            elif i == 2:
                ratios.append(int(input("#  Enter 3rd coeffecient:  ")))
                compounds.append(input("#  Enter 3nd compound:  "))
            else:
                ratios.append(int(input("#  Enter " + str(i + 1) + "th coeffecient:  ")))
                compounds.append(input("#  Enter " + str(i + 1) + "th compound:  "))
            i = i + 1
        for x in range(0, leftSide):
            leftSideCoef.append(ratios[x])
            leftSideComp.append(compounds[x])
        for y in range(leftSide, leftSide + rightSide):
            rightSideCoef.append(ratios[y])
            rightSideComp.append(compounds[y])
        print("#  The chemical equation is")
        i = 0
        print("#  ", end="")
        while i < len(leftSideComp):
            if i < (len(leftSideComp) - 1):
                print(str(leftSideCoef[i]) + leftSideComp[i] + " + ", end="")
            else:
                print(str(leftSideCoef[i]) + leftSideComp[i] + " --> ", end="")
            i = i + 1
        i = 0
        while i < len(rightSideComp):
            if i < (len(rightSideComp) - 1):
                print(str(rightSideCoef[i]) + rightSideComp[i] + " + ", end="")
            else:
                print(str(rightSideCoef[i]) + rightSideComp[i])
            i = i + 1
        correctEq = input("#  Is this the correct equation?\n#  Choose either yes or no:  ")
        if correctEq == ("no" or "n" or "No" or "NO" or "N"):
            correctEq = False
        else:
            correctEq = True
    k = float(scientificString(input("#  Enter K value:  ")))




    # Need to finish this later.
    # Problem is that as the amount
    # of compounds increases, so does
    # the difficulty of calculating x.

def main():
    print("1: Calculate pOH of a buffer from Kb (Henderson Hasselbalch equation)")
    print("2: Calculate pH of a buffer from Ka (Henderson Hasselbalch equation)")
    print("3: Calculate the ratio of base/acid from pH and Ka")
    print("4: Calculate the ratio of acid/base from pOH and Kb")
    print("5: Solve an ICE table")
    global validResponse
    validResponse = False
    choice = input("#  What would you like to do? (Type 'exit' to exit):  ")
    if choice == "5":
        validResponse = True
        print()
        iceSolver()
    if choice == "exit":
        validResponse = True
        return
    else:
        return

def welcome():
    print()
    print("#  WELCOME TO THE EQUILIBRIUM HELL CALCULATOR. Ver. 0.8.9")
welcome()
validResponse = False
while validResponse == False:
    print()
    main()