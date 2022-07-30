"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Radek Civin
email: radek.civin@gmail.com
discord: Radek C#3251
"""
import Analyze

# list of users
users = {'bob':'123','ann':'pass123', 'mike':'password123','liz':'pass123' }

#option to select
sel_opt = []

#formating
line_sep = 36*'-'

#User Input (usrid and psw)
user_login = input("Zadej uzivatelske jmeno:").lower()
user_heslo = input("Heslo :")
print(line_sep)
# user validation

if user_login in users.keys() and user_heslo == users[user_login] :
# If true
    print(f"Welcome to the app,: {user_login} \nWe have 3 texts to be analyzed.")
    print(line_sep)
# If false
else:
    print(f'Unregistered user, terminating the program..')
    quit()

#Select text to be analyzed

while True :
    options = input("Enter a number btw. 1 and 3 to select:")
    print(line_sep)
# if option is not properly selected then ask again for the proper value
    if int(options) not in {1,2,3} :
        print('insert number between 1 and 3')
        print(line_sep)
        continue
# if proper selection is provided then break the loop and carry on
    else :
        sel_opt = int(options)-1
        break

#Selection to string and replacing "," and "."
to_check_raw = Analyze.TEXTS[sel_opt]
to_check = to_check_raw.replace(",","").replace(".","")

#variable for loops

words = 0
upperC  = 0
lowerC  = 0
all_cap = 0
num_to_sum = []
digits = 0

#Count all words
for items in to_check.split() :
    words += 1

#Count when upper case
for items in to_check.split() :
      if  items.isalpha() and items[0] == items.upper()[0]:
            upperC += 1

#Count when lower case
for items in to_check.split() :
      if  items.isalpha() and items[0] == items.lower()[0]:
            lowerC += 1

#Count only when whole word is upper case
for items in to_check.split() :
      if  items.isalpha() and items == items.upper() :
            all_cap += 1

#Appending only numbers into the list
for items in to_check.split() :
      if  items.isdigit():
            num_to_sum.append(int(items))

#Counting numbber of digits
for items in to_check.split() :
      if  items.isdigit() :
            digits += 1

# Printing the output
print(f'There are {words} in the selected text')
print(f'There are {upperC} titlecase words.')
print(f'There are {all_cap} uppercase words.')
print(f'There are {lowerC} lowercase words')
print(f'There are {digits} numeric strings.')
print('sum of all the numbers', total := sum(num_to_sum))


# Chart
#var dict to store data
occ = dict()
#Starting point
start = 1

#Cycle to update occurances in the text
for items in to_check.split() :
#if length exists update occurance
       if len(items) in occ.keys() :
           incr = occ[len(items)] +1
           upd_dict = {len(items) : incr}
           occ.update(upd_dict)
#if length doesn't exist, create new entry with starting value of 1
       else :
           occ[len(items)] = start

#printing output
print(line_sep)
print('LEN|\tOccurence\t|NR')
print(line_sep)
#adding dictionary items into new variable to get them sorted
sort_order = sorted(occ.items())

#Loop for printing maybe not the best one, but it works :)
for i in sort_order :
    if len(str(i[0])) < 2 :
        print(i[0],' |', i[1]*'*',space:= (13 - i[1])*' ' ,'|',i[1])
    else:
        print(i[0], '|', i[1] * '*',space:= (13 - i[1])*' ' , '|', i[1])
print(line_sep)