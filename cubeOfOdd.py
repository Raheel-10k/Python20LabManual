start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
while end_range<start_range:
    end_range = int(input("Enter the end of the range: "))
odd_cubes_dict = {num: num**3 for num in range(start_range, end_range + 1) if num % 2 != 0}
print("Dictionary of Cube of Odd Numbers:")
print(odd_cubes_dict)