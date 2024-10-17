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

#make a variable that will hold the highest numbers
highest_number = []
#define a function that will determine the highest number or numbers
def highest_picker(highest_number_placeholder, num1_placeholder, num2_placeholder, num3_placeholder, num4_placeholder, num5_placeholder):
    if number_1 >= number_2:
        temp_high_num_1 = number_1
        highest_number_placeholder.append(temp_high_num_1)

highest_num = highest_picker(highest_number, number_1, number_2, number_3, number_4, number_5)
print(highest_num)
#use if statement function to compare two numbers and push the higher or equal number to the highest_numbers list

#make a function if there is two or more equal numbers it will print the number and the amount of equal numbers

#print the highest_number

#the code will display the highest number even if there is two or more same values
