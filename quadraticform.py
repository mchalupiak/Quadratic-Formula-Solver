import math

var_A = float(input("What is the A?: "))
var_B = float(input("What is the B?: "))
var_C = float(input("What is the C?: "))
bOne = var_B * -1
bTwo = var_B**2
aBottom = var_A * 2
sqrtSecond = 4 * var_A * var_C
underSqrt = bTwo - sqrtSecond
appendI = False
yesValues = ["y", "yes", "t", "true", 1, "Y", "Yes", "T", "True", "1"]

def isNegative(x):
    combinedVal = x + abs(x)
    return combinedVal == 0

def yN(val):
    return val in yesValues

if isNegative(underSqrt):
    stillSolve = input("The solution is complex. Solve anyway?(1 for Yes 0 for No): ")
    if yN(stillSolve):
        underSqrt = underSqrt * -1
        appendI = True
    else:
        exit()
sqrtedUndersqrt = math.sqrt(underSqrt)
evalTopsolutionOne = bOne + sqrtedUndersqrt
evalTopsolutionTwo = bOne - sqrtedUndersqrt
solutionOne = evalTopsolutionOne / aBottom
solutionTwo = evalTopsolutionTwo / aBottom

if appendI == False:
        print("The First Solution is " + str(solutionOne) + " and The Second Solution is " + str(solutionTwo))
elif appendI == True:
    print("The First Solution is " + str(solutionOne) + "i" + " and the Second Solution is " + str(solutionTwo) + "i")
