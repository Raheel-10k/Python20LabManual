num = int(input("Enter a number: "))
num_str = str(num)
num_digits = len(num_str)
armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)  #Simple composition is used where each digit has first the exponent of number of digit and then added with the next in line.
if armstrong_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")