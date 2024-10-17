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

#define a function that will determine the highest number or numbers
def highest_picker(highest_number_placeholder, num1_placeholder, num2_placeholder, num3_placeholder, num4_placeholder, num5_placeholder):
#compare num1 to num2, 3, 4, 5
  if number_1 >= number_2:
        if number_1 >= number_3:
            if number_1 >= number_4:
                if number_1 >= number_5:
                    highest_number_placeholder.append(number_1)
  if number_2 >= number_1:
        if number_2 >= number_3:
            if number_2 >= number_4:
                if number_2 >= number_5:
                    highest_number_placeholder.append(number_2)
  if number_3 >= number_1:
        if number_3 >= number_2:
            if number_3 >= number_4:
                if number_3 >= number_5:
                    highest_number_placeholder.append(number_3)
  if number_4 >= number_1:
        if number_4 >= number_2:
            if number_4 >= number_3:
                if number_4 >= number_5:
                    highest_number_placeholder.append(number_4)
  if number_5 >= number_1:
        if number_5 >= number_2:
            if number_5 >= number_3:
                if number_5 >= number_4:
                    highest_number_placeholder.append(number_5)

#this function returns the value of the highest number
def highest_num_display():
    if len(highest_number) >= 2:
        return highest_number[0]

#make a variable that will hold the highest numbers
highest_number = []

highest_num = highest_picker(highest_number, number_1, number_2, number_3, number_4, number_5)

if len(highest_number) == 1:
    print("the highest number is", highest_number)
if len(highest_number) >= 2:
    print(f"the highest number is {highest_num_display()}, appearing {len(highest_number)} times.")

#problem with input of user as it only accept non negative numbers