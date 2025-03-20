states = ['New York', 'New Jersey', "Delware", "Virginia", 'Georgia']

# Comma separated list.
print('All states: ',', '.join(states))

states.reverse();

print("All states reversed: ", ", ".join(states))

print(f"First state: {states[0]}\nLast state: {states[-1]}")

# Keep the middle index value to use for later.
middleIndex = int(len(states)/2)

print('Middle states: ', states[middleIndex])

# Delete middle index.
del states[middleIndex]

print('After removing middle state: {}'.format(", ".join(states)))

# Add Florida to the end of the list.
states.append("Florida")

joinedList = ", ".join(states)
print(f"Appended Florida to list: {joinedList}")

# Insert Alabama before New Jersey.
states.insert(2, 'Alabama')

joinedList = ", ".join(states)
print(f"After inserting Alabama to this list: {joinedList}")