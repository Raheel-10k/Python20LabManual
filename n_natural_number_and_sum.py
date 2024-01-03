n = int(input("Enter the value of n: "))
sums = 0    #sum is a keyword thus used variable sums.
print(f"First {n} natural numbers: ")
for i in range(1, n + 1):
    print(i, end=" ")
    sums += i
print(f"\nSum of the first {n} natural numbers: {sums}")