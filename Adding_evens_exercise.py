print("Adding Evens Exercise")
total = 0
for number in range (0 , 101):
    if number % 2 == 0 :
        total += number
print(total)

# or we can do in different way

total = 0
for number in range(2 , 101 , 2):
    total += number
print(total)