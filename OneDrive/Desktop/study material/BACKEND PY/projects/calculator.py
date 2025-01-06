first = int(input("Enter first number :"))
operator = input("enter operator (+,-,*,/,%): ")
second = int(input("Enter second number :"))

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first%second)
else:
    print("invalid operation")