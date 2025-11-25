# SLICING A LIST
# CODE SUMMARY FROM caude.ai
# This code demonstrates Python **list slicing** - extracting portions of a list using index ranges:

# 1. **`players[0:3]`** - Gets elements at indices 0, 1, 2 → `['charles', 'martina', 'michael']`

# 2. **`players[1:4]`** - Gets elements at indices 1, 2, 3 → `['martina', 'michael', 'florence']`

# 3. **`players[:3]`** - Gets from the start up to index 3 → `['charles', 'martina', 'michael']`

# 4. **`players[2:]`** - Gets from index 2 to the end → `['michael', 'florence', 'eli']`

# 5. **`players[-3:]`** - Gets the last 3 elements → `['michael', 'florence', 'eli']`

# **Key concept**: Slicing uses `[start:stop]` syntax where `start` is inclusive and `stop` is exclusive.
# Omitting `start` begins at the beginning; omitting `stop` goes to the end. 
# Negative indices count from the end of the list.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])

print(players[:3])

print(players[2:])

print(players[-3:])

# LOOPING THROUGH A SLICE
# print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())