original_list = []
num_elements = int(input("Enter the number of elements in the list: "))

for i in range(num_elements):
    element = int(input(f"Enter element {i + 1}: "))
    original_list.append(element)

unique_list = list(set(original_list))  #set a built in data type that has unordered collection of unique elements.

print("Original List:", original_list)
print("List with Distinct Elements:", unique_list)
