for number in range(1,101):
    if number % 3 or number % 5 == 0:#Here is the error shows only one condition is true .We need both condition true in this way we get correct answer.
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print([number])#This show the number is enveloped with square brackets