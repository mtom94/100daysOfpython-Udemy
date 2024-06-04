import  random

random_integer = random.randint(1 , 10)
print(random_integer)

random_float = random.random()
print(random_float)

#get random decimal between 0 and 5
#0.0000000000000......... to 4.9999999999 (not include 5)
decimal_between_numbers= random_float * 5
print(decimal_between_numbers)