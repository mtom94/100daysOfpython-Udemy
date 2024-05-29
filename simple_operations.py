print("Hello"[0]) #Here the output shows the first character "H"
print(len("Hello")) #Here the output shows the output of the strind
print("123" + "456") #shows concatenation like 123456

#Integer
print(123 + 567)

num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + "characters")

print(type("What is you name?"))

print(70 + float("100.5"))
print(str(70) + str(100))

two_digit_number = input("Type a two digit number:")
print(type(two_digit_number))
first_number = two_digit_number[0]
second_number = two_digit_number[1]

print(first_number)
print(second_number)

result = int(first_number) + int(second_number)
print(result)



print(float(8/3))
print(type(8/3))

#we can use the round fn change it into integer

print(round(8/3))
print(round(8/3,2)) #indicate that round the values upto 2nd position of decimal point
#or we can prin this way
print(round(2.6666666666666,2))

#or we can use floor division(//) we ge
print(8 // 3)
print(type(8 // 3))

#f-String - which is important pythhon programming in the case of different  datatypes
#The convenent way for this is:

score = 0 #int
height = 1.9 #float
iswinning = True #boolean
print(f"your score is {score},Your height is {height},You are winning is {iswinning}")

