#print "*" pattern if user inputs number 5
number = int(input("Enter number 5: "))
if number == 5:
    for i in range(1, 6):
        print("* " * i )
#then reverse the pattern
    for i in range(4, 0, -1):
        print("* " * i)
else:
    print("Please enter the number 5.")
# This code will print a pattern of asterisks in increasing order from 1 to 5.



