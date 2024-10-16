#get 5 numbers from the user
print("Give 5 numbers and I'll display the highest")

while True:
    number_1 = input("give the first number: ")
    if number_1.isdigit():
        number_1 = int(number_1)
        break
    else:
        print("please put a number")
    
while True:
    number_2 = input("give the second number: ")
    if number_2.isdigit():
        number_2 = int(number_2)
        break
    else:
        print("please put a number")

while True:
    number_3 = input("give the third number: ")
    if number_3.isdigit():
        number_3 = int(number_3)
        break
    else:
        print("please put a number")
        
while True:
    number_4 = input("give the fourth number: ")
    if number_4.isdigit():
        number_4 = int(number_4)
        break
    else:
        print("please put a number")

while True:
    number_5 = input("give the fifth number: ")
    if number_5.isdigit():
        number_5 = int(number_5)
        break
    else:
        print("please put a number")

#make a variable that holds the highest number
highest_number = number_1
#compare number 1 - 5 with highest number variable
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
