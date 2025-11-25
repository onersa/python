alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
 print(alien)

# Make an empty list for storing aliens.
print()
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
 new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
 aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
 print(alien)
print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# Make 30 green aliens.
# ===========================================================
# SUMMARY OF CODE SNIPPET FROM claude.ai
# This code demonstrates working with **lists of dictionaries** and modifying them:

# 1. **Creates 3 initial alien dictionaries** with different colors, points, and stores them in a list

# 2. **Generates 30 additional green aliens** using a loop:
#    - Each new alien is a dictionary with `'color': 'green'`, `'points': 5`, `'speed': 'slow'`
#    - Appends each to the `aliens` list (total: 33 aliens)

# 3. **Modifies the first 3 aliens** based on their current color:
#    - If **green**: upgrades to yellow, medium speed, 10 points
#    - If **yellow**: upgrades to red, fast speed, 15 points
#    - Red aliens would remain unchanged (no elif condition for them)

# 4. **Displays the first 5 aliens** to show the results:
#    - The first 3 will be upgraded (originally green/yellow/red → yellow/red/red)
#    - The next 2 remain green (not in the modification slice)
#    - Prints "..." to indicate more aliens exist

# **Key concepts**: Nested data structures (dictionaries inside lists),
# conditional logic to modify dictionary values, and list slicing to work with specific portions of the list.
# ===========================================================
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien_number in range (30):
   new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
   aliens.append(new_alien)
for alien in aliens[:3]:
 if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10
 elif alien['color'] == 'yellow':
    alien['color'] = 'red'
    alien['speed'] = 'fast'
    alien['points'] = 15
    
# Show the first 5 aliens.
for alien in aliens[:5]:
 print(alien)
print("...")