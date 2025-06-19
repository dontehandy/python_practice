num1 = float(input("What's the first number?: "))
op = input("Add or subtract?: ")
num2 = float(input("What's the second number?: "))

def quick_cal(num1, op, num2):
    if op == "+":
        print(f"Adding {num1} & {num2} will give you {num1 + num2}.")
    elif op == "-":
        print(f"Taking away {num2} from {num1} will leave you with {num1 - num2}. ")
    else:
        print("Operator Error: Please Try Again")

quick_cal(num1, op, num2)

#this is just a test and to get familiar with python/vscode/github...again
#19JUN25 - 1935hrspwd


