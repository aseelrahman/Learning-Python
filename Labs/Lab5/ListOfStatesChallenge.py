states = []
states_inputted = input("Enter a list of states comma separated without spaces: ")

# Inserting states in the list 'states'.
states = states_inputted.split(",")
print(f"States inputted: {states}")

# Finding the middle index number of the states varriabel.
middleIndex = int(len(states)/2)

# Printng the middle state name.
print('Middle state: ', states[middleIndex])

# Deleting the middle state.
del states[middleIndex]
print(f"After removing middle state: {states}")

# Appending the first state again in the end of the list.
states.append(states[0])
print(f"Appended first state to the end of the list: {states}")

# Deleting the first state.
del states[0]
print(f"Removed first state form the list: {states}")