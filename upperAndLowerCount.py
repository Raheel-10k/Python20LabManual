def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

stringToTest = str(input("Enter a long string:\n"))
upper, lower = count_upper_lower(stringToTest)
print("Original String: ", stringToTest)
print("Uppercase count: ", upper)
print("Lowercase count: ", lower)