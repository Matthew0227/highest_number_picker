#get 5 numbers from the user
print("Give 5 numbers and I'll display the highest")

def input_number(ask_user):
 while True:
    try:
        return int(input(ask_user))
    except ValueError:
        print("please put a number")

number_1 = input_number("give the first number: ")
number_2 = input_number("give the second number: ")
number_3 = input_number("give the third number: ")
number_4 = input_number("give the fourth number: ")
number_5 = input_number("give the fifth number: ")
    

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
    print("the highest number is", {highest_number})
if len(highest_number) >= 2:
    print(f"the highest number is {highest_num_display()}, appearing {len(highest_number)} times.")

#using try block to ask user to input a number until they do