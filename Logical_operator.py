print("Roller coaster Using Logical Operators")
height = int(input("Enter the height in cm:"))
age = int(input("Enter the age :"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    if age < 12:
        print("children tickets are  $5")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Adult tickets are $12")
        bill = 12
    want_photo = input("Do you want photo taken? Y or N:")
    if want_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry! You can't ride the rollercoaster")


