print("Welcome to pizza Delivaries!")
size = (input("what size of pizza do you want?S, M, L:"))
add_peppaeroni = input("Do you want pepperoni? Y or N:")
extra_cheese = input("Do you want extra cheese? Y or N:")
bill = 0

if size == "S":
    bill +=15
elif size == "M":
    bill +=20
elif size == "L":
    bill +=25

if add_peppaeroni == "Y":
    if add_peppaeroni == "S":
        bill +=2
    else:
        bill +=3

if extra_cheese == "y":
    bill +=1
print(f"Your final bill is {bill}")
