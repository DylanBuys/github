#prompt user to enter a number continuously 
import math
while True:
    try:
        num = int(input("Enter a number")
        if num == 0:
            print("Invalid input.")
        elif num == -1:
            print("Exiting the program.")
            break
#if user enters an invalid input, print an error message
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    else:
        print(f"You entered: {num}")
#after exiting loop, calaculate average of all number ecxept 0 and -1
        if num != 0 and num != -1:
            if 'total' not in locals():
                total = 0
                count = 0
            total += num
            count += 1
            average = total / count
            print(f"Current average of entered numbers: {average:.2f}")
        else:
            print("No valid numbers entered yet.")
