from texttable import Texttable
from math import *
import sys


def mathFunction(function, value):
    x = value
    result = float(eval(function))
    return result


def bisection(function, range, error):

    i = 0
    resultOfFunction = 10000.
    t = Texttable()
    t.header(["Iteration", "a", "b", "m", "f(c)"])
    t.set_cols_width([9, 9, 9, 9, 20])
    t.set_cols_dtype(["t", "t", "t", "t", "t"])
    t.set_cols_align(["c", "c", "c", "c", "c"])
    t.set_cols_valign(["m", "m", "m", "m", "m"])
    t.set_header_align(["c", "c", "c", "c", "c"])

    while resultOfFunction > float(error) or resultOfFunction < float(-error):
        i += 1
        x: float = (float(range[0]) + float(range[1])) / 2
        resultOfFunction = mathFunction(function, x)

        t.add_row([str(i), str(range[0]), str(range[1]), str(x), str(resultOfFunction)])

        if resultOfFunction == 0.:
            continue

        if resultOfFunction > 0.:
            range[1] = x
            continue

        if resultOfFunction < 0.:
            range[0] = x
            continue

    print(t.draw())
    return None


def info():
    
    print("\nHow to write different mathematical functions in the function's expression: \n")
    print(" LOGARITHM: log(number, base) -> example: x + log(x, 2)\n"
          " EXPONENTIATION: pow(base, exponent) -> example: x + pow(x, 3)\n"
          " SQUARE ROOT: sqrt(x) -> example: x + sqrt(x + 2)\n"
          " SINE: sin(x) -> example: x + sin(x)\n"
          " COSINE: cos(x) -> example: x + cos(x)\n"
          " TANGENT: tan(x) -> example: x + tan(x)\n")


def userInput():
    
    while True:

        functionUser = input("\n Write a function: ")
        a = input(" Write the first number of the range: ")
        b = input(" Write the second number of the range: ")
        errorUser = float(input(" Write the error range: "))
        rangeUser = [float(a), float(b)]

        if mathFunction(functionUser, float(a)) * mathFunction(functionUser, float(b)) < 0:
            print(bisection(functionUser, rangeUser, errorUser))
            break
        else:
            print("\nError. Wrong range of values: Retry")
            continue


def main():
    
    print("BISECTION METHOD")
    while True:

        print("\n 1. Start \n 2. Info \n 3. Quit \n ")
        userSelection = int(input("Select an option: "))

        if userSelection == 1:
            userInput()
        if userSelection == 2:
            info()
        if userSelection == 3:
            sys.exit()
        else:
            continue


# Start the program
if __name__ == "__main__":
    main()
