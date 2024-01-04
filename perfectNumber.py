number = int(input("Enter a number: "))
if number <= 0:
    print(f"{number} is not a perfect number.")
else:
    divisor_sum = sum([i for i in range(1, number)if number % i == 0])
    if divisor_sum == number:
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")   