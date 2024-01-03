num = int(input("Enter a number: "))
factorail = 1   #if starts from 0 then all values stay 0
for i in range(1, num + 1):
    factorail *= i
print(f"The factorial of {num} is: {factorail}")