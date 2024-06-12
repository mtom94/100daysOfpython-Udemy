print("for loop with range")
for number in range(0 , 11 , 5): #the number 5 represents increase to the next number
    print(number)


#find the total number by counting natural number from 1 to 100 and 100 to 1

total = 0
for number in range(1 , 101):
    total += number
print(total)