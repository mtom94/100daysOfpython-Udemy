# 1) Describe Problem
#
# def my_function():
#     for i in range(1, 20): #In this code we do not get the proper output becoz of the bug in for loop.The i does not reach upto 20
#         if i == 20:
#             print("You got it!")
# my_function()

#Actual code

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it!")
my_function()


# 2) Reproduce the bug
# from random import randint
# dice_imgs = ["1" , "2" , "3" , "4" , "5" , "6" ]
# dice_num = randint(1 , 6)# In this case the randint shows the numbers between the 1 and 6
# # and it also includes 1 and 6 but in the case of list it shows from 0 to 5
# # So the error occurs in the part of randint.Change it into randint(0,5).
# print(dice_imgs[dice_num])

#Actual code
from random import randint
dice_imgs = ["1" , "2" , "3" , "4" , "5" , "6" ]
dice_num = randint(0 , 5)
print(dice_imgs[dice_num])

#3) Play Computer

year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are Millenial.")
elif year >= 1994:
    print("You are a Gen Z")


# #4) Fix the Errors
# age = input("How old are you?") # This line shows the error of Typecasting.If you use any of the numerical operation ,we must use an integer variable.
# if age > 18:
#     print("You can drive at age {age}.")#This line shows  the error of formatted string.

#Actual code
age = int(input("How old are you?"))
if age > 18:
   print(f"You can drive at age {age}.")

#5) Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages:"))
#word_per_page == int(input("Number of words per page:"))# The error occur here is the equat to operator .Here we use == instead of the assignment = operator.
word_per_page = int(input("Number of words per page:"))
total_words = pages * word_per_page
print(total_words)

#6) Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)
mutate([1,2,3,4,5,6,7,8,13])