import math 
print("investment - to calculate the amount of interest you will recieve on your investment")
print("bond loan - to calculate the amount youll need to pay on a home loan")
#prompt user to choose between investment and bond
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
#if the user chooses 'investment' run the investment code, 
if choice.lower() == "investment":
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate (as a percentage): "))
    time = float(input("Enter the number of years: "))
    interest_type = input("Enter 'simple' for simple interest or 'compound' for compound interest: ").lower()
    
    if interest_type.lower() == "simple":
        interest = principal * (rate / 100) * time
        total_amount = principal + interest
        print(f"The total amount after {time} years is: {total_amount}")
    elif interest_type == "compound":
        total_amount = principal * math.pow((1 + rate / 100), time)
        print(f"The total amount after {time} years is: {total_amount}")
    else:
        print("Invalid interest type selected.")
#elif the user chooses 'bond' run the bond code
elif choice.lower() == "bond":
    present_value = float(input("Enter the present value of the house: "))
    annual_rate = float(input("Enter the annual interest rate (as a percentage): "))
    months = int(input("Enter the number of months to repay the bond: "))
    
    monthly_rate = annual_rate / 100 / 12
    monthly_payment = (present_value * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
    
    print(f"The monthly payment for the bond is: {monthly_payment}")
else:
    print("Invalid choice. Please enter either 'investment' or 'bond'.")
    #prompt user to re-enter their choice. loop until valid input is given
    while choice.lower() not in ["investment", "bond"]:
        choice = input("Invalid choice. Please enter either 'investment' or 'bond': ")
        if choice.lower() == "investment":
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the interest rate (as a percentage): "))
            time = float(input("Enter the number of years: "))
            interest_type = input("Enter 'simple' for simple interest or 'compound' for compound interest: ").lower()
            
            if interest_type.lower() == "simple":
                interest = principal * (rate / 100) * time
                total_amount = principal + interest
                print(f"The total amount after {time} years is: {total_amount}")
            elif interest_type == "compound":
                total_amount = principal * math.pow((1 + rate / 100), time)
                print(f"The total amount after {time} years is: {total_amount}")
            else:
                print("Invalid interest type selected.")
        elif choice.lower() == "bond":
            present_value = float(input("Enter the present value of the house: "))
            annual_rate = float(input("Enter the annual interest rate (as a percentage): "))
            months = int(input("Enter the number of months to repay the bond: "))
            
            monthly_rate = annual_rate / 100 / 12
            monthly_payment = (present_value * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
            
            print(f"The monthly payment for the bond is: {monthly_payment}")
        else:
            print("Invalid choice. Please enter either 'investment' or 'bond'.")
    #end of while loop
    # This will ensure that the user is prompted to re-enter their choice until a valid input
    # This will allow the user to re-enter their choice if they made a mistake
#end of code

