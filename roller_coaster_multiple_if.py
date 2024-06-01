print("Roller Coaster using Multiple if")
height = int(input("Enter your height in cm:"))
age = int(input("Enter you age:"))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    if age <=12:
        print("Children tickets $5")
        bill = 5
    elif age >= 18:
        print("youth tickets $7")
        bill = 7
    else:
        print("Adult tickets $12")
        bill = 12
    want_photo = input("Do you want taken pictures? Y or N.:")
    if want_photo == "Y":
        #add their bill
        bill +=3
    print(f"final amount is ${bill}")
else:
    print("Sorry! You can't ride the roller coaster")
