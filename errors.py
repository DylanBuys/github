# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") #syntax error fixed
print("/n") #syntax error fixed

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = (" years old") # syntax error fixed
age = str("24") # logical error
age_int= int(24) # syntax error fixed #logical error fixed
print("I'm " + age + " years old.") # syntax error fixed

    # Variables declaring additional years and printing the total years of age
years_from_now = int(3) # syntax error fixed
total_years_int = age_int + years_from_now
total_years = str(total_years_int) # logical error fixed

print("The total number of years:" +  total_years) # syntax error fixed

# Variable to calculate the total number of months from the given number of years and printing the result
total_months_int = total_years_int * 12 + 6 # logical error fixed
total_months = str(total_months_int) # logical error fixed
print("In 3 years and 6 months, I'll be " + total_months + " months old") # syntax error fixed

#HINT, 330 months is the correct answer
