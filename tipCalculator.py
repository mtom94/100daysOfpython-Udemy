#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.

# print("Welcome to the tip calculator")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
# people = int(input("How many people to split the bill?"))
#
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill /people
# final_amount = round(bill_per_person,2)
#
# print(f"Each person should pay:${final_amount}")

# print("Hello"[0]) #Here the output shows the first character "H"
# print(len("Hello")) #Here the output shows the output of the strind
# print("123" + "456") #shows concatenation like 123456
#
# #Integer
# print(123 + 567)

# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + "characters")
#
# print(type("What is you name?"))

# print(70 + float("100.5"))
# print(str(70) + str(100))

two_digit_number = input("Type a two digit number:")
print(type(two_digit_number))
first_number = two_digit_number[0]
second_number = two_digit_number[1]

print(first_number)
print(second_number)

result = int(first_number) + int(second_number)
print(result)