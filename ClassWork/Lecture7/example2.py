# Sorting a List

repeat_equal_sign_and_line_break = "\n" + ("=" * 60)

# Create a List with numeric values
list1 = [6, 4, -5, 2.5]

print(repeat_equal_sign_and_line_break)
print('TEST 1: Values being sorted: ', list1)

# Sort the List items by value.
# NOTE: This sort was done using the "less than" operator
list1.sort()

print("Sorted Values: ", list1)
print("Max value: ", max(list1))
print("Min value: ", min(list1))

# Create a List with string values
list2 = ["ha", "hi", 'B', '7']

print(repeat_equal_sign_and_line_break)
print("TEST 2: Values being sorted: ", list2)

# NOTE: This sort was done using the "less than" operator and the 
# ascii values for hte characters
list2.sort()

print("Sorted values: ", list2)
print("Max value: ", max(list2))
print("Min value: ", min(list2))