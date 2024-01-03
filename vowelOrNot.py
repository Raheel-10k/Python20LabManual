char = input("Enter a character: ")[0]      #to take only the first character incase user inputs more than one.
if char.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f"{char} is a vowel.")
else:
    print(f"{char} is not a vowel.")