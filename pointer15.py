import math

def geekout():
    while True:
        try:
            n = input("Please enter a number: ")
            if n == "":
                print("No input captured. Please enter a number: ")
                continue
            n = int(n)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
        except OverflowError:
            print("Number is too large. Please enter a smaller number")
    n = abs(n)
    if math.isclose(n % 2, 0, abs_tol=1e-9) and math.isclose(n % 3, 0, abs_tol=1e-9):
        print("GeekOut 2024!")
    elif math.isclose(n % 2, 0, abs_tol=1e-9):
        print("Geek")
    elif math.isclose(n % 3, 0, abs_tol=1e-9):
        print("Out")
    else:
        print("GeekOut")

geekout()
