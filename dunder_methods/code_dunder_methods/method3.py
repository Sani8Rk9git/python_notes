def add(a , b):
    return a + b

def subtract(a , b):
    return a - b


print(__name__)

if __name__ == "__main__":
    print("Calculator")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(f"Sum is {add(num1 , num2)}")
    print(f"Difference is {subtract(num1 , num2)}")


