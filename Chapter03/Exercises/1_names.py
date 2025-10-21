names = ["vusi", "tshepiso", "naledi", "kgosi"]

family = f"Family Members:\n\t{names[0].title()}\n\t{names[1]}"
family += f"\n\t{names[2].title()}\n\t{names[3]}"
print(family)
message = f"hello {names[0]}. You are invited"
print(message)
message = f"hello {names[1]}. You are invited"
print(message)
message = f"hello {names[2]}. You are invited"
print(message)
message = f"hello {names[3]}. You are invited"
print(message)

# LIST OF CARS
cars = ["bmw", "polo", "haval"]
print(f"I love {cars[0]}")
print(f"I love {cars[1]}")
print(f"I love {cars[2]}")

def print_guest_list():
    print("___________________________\n")
    for name in names:
        print(f"{name} is invited")
    print("___________________________")
    
print_guest_list()    