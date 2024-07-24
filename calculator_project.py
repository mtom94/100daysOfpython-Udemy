from calculator_art import logo

def Add(n1 , n2):
    return n1 + n2
def Sub(n1 , n2):
    return n1 - n2
def Mul(n1 , n2):
    return n1 * n2
def Div(n1 , n2):
    return n1 / n2

operations = {
    "+": Add,
    "-": Sub,
    "*": Mul,
    "/": Div
}
def calculator():
    print(logo)
    num1 = float(input("What is the first number:"))

    for operator in operations:
        print(operator)
    should_continue = True
    while should_continue:
        select_operator = input("Pick an operation :")
        num2 = float(input("What is the next number:"))
        calculation_function = operations[select_operator]
        Answer = calculation_function(n1=num1 , n2=num2)

        print(f"{num1} {select_operator} {num2} = {Answer}")

        if input(f"Type 'y' to continue calculating with {Answer}, or type 'n' to start a new calculation:") == "y":
            num1 = Answer
        else:
            should_continue = False
            calculator()
calculator()