guest = ["Ann", "Joe", "Pam"]

print(f"Hi {guest[0]}. You are invited")
print(f"Hi {guest[1]}. You are invited")
print(f"Hi {guest[2]}. You are invited")

# REMOVE JOE AND REPLACE WITH TOM
print(f"{guest[1]} cannot make it")
print(guest)
guest.pop(1)
print(guest)

guest.append("tom")
print(guest)
guest.insert(1, "jerry")
print(guest)
print(len(guest))
del guest[1]
print(guest)
guest.remove("Pam")
print(guest)

