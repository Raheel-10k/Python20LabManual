a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("\n\nList: ", a)

print("\n4th Element of the List: ", a[3])

print("\nList from 0th to 4th Index: ", a[0:5])

print("\nList from -7th to 3rd Element: ", a[-7:4])

a.append(110)
print("\nv. List after Appending 110:", a)

a.sort()
print("\nvi. Sorted List:", a)

popped_element = a.pop()
print("\nvii. Popped Element:", popped_element)
print(" List after Popping:", a)

specified_element = 60
a.remove(specified_element)
print("\nviii. List after Removing",
specified_element, ":", a)

index_to_insert = 2
element_to_insert = 15
a.insert(index_to_insert, element_to_insert)
print("\nix. List after Inserting ", element_to_insert, " at index [", index_to_insert,"]: ", a)

element_to_count = 20   #Occurrence of specific element
count = a.count(element_to_count)
print("\nx. Count of", element_to_count, "in the List: ", count)

extended_list = [120, 130, 140]
a.extend(extended_list)
print("\nxi. List after Extending with ", extended_list, " is: \n", a)

a.reverse()
print("\nxii. Reversed List:", a)