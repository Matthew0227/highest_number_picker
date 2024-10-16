#get 5 numbers from the user
print("Give 5 numbers and I'll display the highest")
number_1 = int(input("give the first number: "))
number_2 = int(input("give the second number: "))
number_3 = int(input("give the third number: "))
number_4 = int(input("give the fourth number: "))
number_5 = int(input("give the fifth number: "))

#make a variable that holds the highest number
highest_number = 0
#compare number 1 - 5 with highest number variable
if number_1 > highest_number:
    highest_number = number_1
if number_2 > highest_number:
    highest_number = number_2
if number_3 > highest_number:
    highest_number = number_3
if number_4 > highest_number:
    highest_number = number_4
if number_5 > highest_number:
    highest_number = number_5
#print the highest variable
print(highest_number)

#negative number problem