#prompts user to input their age and prints a message based on the input
age = int(input("Please enter your age:"))
if age ==(100):
    print("sorry, you're dead")
elif age >= (65):
    print("you're over the hill")
elif age >= (40):
    print("enjoy your retirement")
elif age < (13):
    print("you qualify for the kiddie discount")
elif age == (21):
    print("congrats on your 21st")
else:
    print("age is but a number")