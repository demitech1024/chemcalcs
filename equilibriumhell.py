import sys
import math
import re

def henderson(boolean):
    if boolean == False:
        ka = input("#  Enter a Ka value:  ")
        pka = math.log(float(scientificString(ka)), 10) * -1
        base = float(scientificString(input("#  Enter base concentration:  ")))
        acid = float(scientificString(input("#  Enter acid concentration:  ")))
        ph = pka + math.log((base / acid), 10)
        print("#  pH = " + str('%.2f' % ph) + ".")
        print("")
        main()
    elif boolean == True:
        kb = input("#  Enter a Kb value:  ")
        pkb = math.log(float(scientificString(kb)), 10) * -1
        acid = float(scientificString(input("#  Enter acid concentration:  ")))
        base = float(scientificString(input("#  Enter base concentration:  ")))
        poh = pkb + math.log((acid / base), 10)
        print("#  pOH = " + str('%.2f' % poh) + ".")
        print("")
        main()

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

def ratio(boolean):
    if boolean  == False:
        ka = input("#  Enter a Ka value:  ")
        pka = math.log(float(scientificString(ka)), 10) * -1
        ph = float(input("#  Enter a pH value:  "))
        ratio = 10**-(ph - pka)
        ratio = '%.3e' % ratio
        ratio = eval(str(ratio))
        print("#  The base/acid ratio is " + str(ratio) + ".")
        print("")
        main()
    elif boolean == True:
        kb = input("#  Enter a Kb value:  ")
        pkb = math.log(float(scientificString(kb)), 10) * -1
        poh = float(input("#  Enter a pOH value:  "))
        ratio = 10**-(poh - pkb)
        ratio = '%.3e' % ratio
        ratio = eval(str(ratio))
        print("#  The acid/base ratio is " + str(ratio) + ".")
        print("")
        main()
    

def iceSolver():
    print("#  Determine the type of the reaction.")
    print("#  Note: As of the current version of this application (0.8.9), only acid and base ICE table solvers are functional.")
    reactionType = input("#  (Types include acid, base, general, or buffer):  ")
    if reactionType == "acid":
        ka = float(scientificString(input("#  Enter Ka value:  ")))
        acidConc = float(scientificString(input("#  Enter acid concentration:  ")))
        hydroniumConc = float(scientificString(input("#  Enter hydronium concentration:  ")))
        conjBaseConc = float(scientificString(input("#  Enter conj. base concentration:  ")))
        a = 1
        b = hydroniumConc + conjBaseConc + ka
        c = (hydroniumConc * conjBaseConc) - (acidConc * ka)
        x = ((-1 * b) + math.sqrt(b**2 - (4 * a * c)))/(2 * a)
        x = '%.2e' % x
        print("#  The variable x = " + str(x) + ".")
    if reactionType == "base":
        kb = float(scientificString(input("#  Enter Kb value:  ")))
        baseConc = float(scientificString(input("#  Enter acid concentration:  ")))
        ohConc = float(scientificString(input("#  Enter OH concentration:  ")))
        conjAcidConc = float(scientificString(input("#  Enter conj. acid concentration:  ")))
        a = 1
        b = ohConc + conjAcidConc + kb
        c = (ohConc * conjAcidConc) - (baseConc * kb)
        x = ((-1 * b) + math.sqrt(b**2 - (4 * a * c)))/(2 * a)
        x = '%.2e' % x
        print("#  The variable x = " + str(x) + ".")
    if reactionType == "general":
        #k = float(scientificString(input("Enter K value:  ")))
        leftSide = int(input("#  How many compounds are on the left side of the equation? \n(maximum of 3):  "))
        leftSideComp = []
        rightSideComp = []
        rightSide = int(input("#  How many compounds are on the right side of the equation? \n(maximum of 3):  "))
        print("#  From left to right, enter the coeffecient of each of the compounds.")
        ratios = []
        i = 0
        while i < (leftSide + rightSide):
            if i == 0:
                ratios.append(input("#  Enter 1st coeffecient:  "))
            elif i == 1:
                ratios.append(input("#  Enter 2nd coeffecient:  "))
            elif i == 2:
                ratios.append(input("#  Enter 3rd coeffecient:  "))
            else:
                ratios.append(input("#  Enter " + str(i + 1) + "th coeffecient:  "))
            i = i + 1
        for x in range(0, leftSide):
            leftSideComp[x] = ratios[x]
        for y in range(leftSide, rightSide):
            rightSideComp[y - leftSide] = ratios[y]
        leftSideBal = []
        rightSideBal = []
        leftSideBal, rightSideBal = balanceEquation(leftSideComp, rightSideComp)
        ratios = leftSideBal + rightSideBal
         # Need to finish this later.
         # Problem is that as the amount
         # of compounds increases, so does
         # the difficulty of calculating x.
    print("")
    main()

def balanceEquation(leftList, rightList):
    i = 0
    findAllListRight = []
    findAllListLeft = []
    numberRight = []
    numberLeft = []
    while i < (len(rightList) - 1):
        findAllListRight[i] = re.findall('[A-Z][^A-Z]*', rightList[i])
        i = i + 1
    i = 0
    while i < (len(leftList) - 1):
        findAllListLeft[i] = re.findall('[A-Z][^A-Z]*', leftList[i])
        i = i + 1
    i = 0
    numberRight = [i.split('[0-9]') for i in findAllListRight]
    print(numberRight)
    numberLeft = [i.split('[0-9]') for i in findAllListLeft]
    print(numberLeft)
    return [leftList, rightList]

def main():
    print("1: Calculate pOH of a buffer from Kb (Henderson Hasselbalch equation)")
    print("2: Calculate pH of a buffer from Ka (Henderson Hasselbalch equation)")
    print("3: Calculate the ratio of base/acid from pH and Ka")
    print("4: Calculate the ratio of acid/base from pOH and Kb")
    print("5: Solve an ICE table")
    global validResponse
    validResponse = False
    choice = input("#  What would you like to do? (Type 'exit' to exit):  ")
    if choice == "1":
        validResponse = True
        print()
        henderson(True)
    if choice == "2":
        validResponse = True
        print()
        henderson(False)
    if choice == "3":
        validResponse = True
        print()
        ratio(False)
    if choice == "4":
        validResponse = True
        print()
        ratio(True)
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
try:
    while validResponse == False:
        print()
        main()
except:
    print()
    print("###############################################")
    print("   A fatal error has occured. Shutting down.   ")
    print("###############################################")

