#If else statement
# print("Welcome to the rollercoaster!")
# height = int(input("Enter the height in cm :"))
#
# if height > 120 :
#     print("You can Ride the rollercoaster")
# else:
#     print("sorry! you can't ride the roller coaster")

#Nested If else statement
# print("Welcome to the rollercoaster!")
# height = int(input("Enter the height in cm :"))
# age = int(input("What is your age :"))
# if height >= 120 :
#     print("You can Ride the rollercoaster")
#     if age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("sorry! you can't ride the roller coaster")

#if/elif/else
print("Welcome to the rollercoaster!")
height = int(input("Enter the height in cm :"))
age = int(input("What is your age :"))
if height >= 120 :
    print("You can Ride the rollercoaster")
    if age < 12 :
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("sorry! you can't ride the roller coaster")