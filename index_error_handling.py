States_of_india = ["Kerala", "Karnataka", "Tamilnadu", "Goa", "Orissa"]
print(len(States_of_india))

#The abouve code shows the number of states in india are 5.

#but , in the case of list the index position starts with 0.

#print(States_of_india[5])  #This shows the error " IndexError: list index out of range " So, avoid this error we use the below statements:

number_of_states = len(States_of_india)

print(number_of_states)

print(States_of_india[number_of_states - 1]) # Using this we get the output "orissa"



