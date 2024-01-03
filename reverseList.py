sample_list = [1, 2, 3, 4, 5]
reversed_list1 = list(sample_list)   #stores the sample list to a new variable reversed list
# Method 1: Using reverse() function
reversed_list1.reverse()
# Method 2: Using slicing
reversed2 = sample_list[::-1]
print("Original List: ", sample_list)
print("Reversed List (Method 1): ",reversed_list1)
print("Reversed List (Method 2): ", reversed2)