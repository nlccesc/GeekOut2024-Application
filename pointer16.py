import math

def geekout_and_count_chars():
    while True:
        n = input("Please enter a number: ")
        if n == "":
            print("No input captured. Please enter a number.")
            continue
        try:
            n = int(n)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except OverflowError:
            print("Number is too large. Please enter a smaller number.")

    if n % 2 == 0 and n % 3 == 0:
        message = "GeekOut 2024!"
    elif n % 2 == 0:
        message = "Geek"
    elif n % 3 == 0:
        message = "Out"
    else:
        message = "GeekOut"

    message_length = len(message)
    print(f"{message} (Character length: {message_length})")

# Run the function
geekout_and_count_chars()
