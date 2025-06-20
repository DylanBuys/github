# manipulation.pym
str_manip = input("please enter a sentence: ")
print(len(str_manip))
# find last letter in str_manip
last_letter = str_manip[-1]
print("The last letter is:", last_letter)
# replace every occurance of last letter with '@'
str_manip = str_manip.replace(last_letter, '@')
print("The modified string is:", str_manip)
# print the last three chacters of str_manip backwards
last_three = str_manip[-3:]
print("The last three characters backwards are:", last_three[::-1])
# create a five-letter word that is mage up of the first three characters and last two characters of str_manip
first_three = str_manip[:3]
last_two = str_manip[-2:]
five_letter_word = first_three + last_two
print("The five-letter word is:", five_letter_word)





