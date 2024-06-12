print("Fizz Buzz Exercise")

# This is a game playing by children, if the number is divisible by 3 the children say fizz e
# if the number which is divisible by 5 the children say buzz
# if the number is divisible by both the children say "FizzBuzz".

for number in range(1 , 100):
    if number % 3 ==0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else :
        print(number)
