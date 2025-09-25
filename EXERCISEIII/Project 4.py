# Stack implementation using list
stack = []

# Push operations
stack.append("LabA")
stack.append("LabB")
stack.append("LabC")

# Undo all (pop all)
stack.pop()
stack.pop()
stack.pop()

# Final stack state
print("Remaining:", stack)  