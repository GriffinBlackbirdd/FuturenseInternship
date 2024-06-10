# The List League: A Superhero Adventure
'''Now we are entering the Magical Verse of Madness, beware!'''
from functools import reduce

# Our team of superheroes and their power levels
superheroes = {
    "Superman": 1,
    "Ironman": 2,
    "Spiderman": 3,
    "Batman": 4,
    "Wonder Woman": 5
}

# One day, the List League decided to combine their powers to see how strong they were together.
# They used a special technique called "reduce" to sum up their power levels.
power_levels = list(superheroes.values())
total_power = reduce(lambda x, y: x + y, power_levels)
print("Total power of the List League:", total_power)
# Result: Total power of the List League: 15

# All of a sudden our superheroes came across a Power Potion that squares their Power! Let's find out their new powers:
squaredPower = list(map(lambda x: x ** 2, power_levels))
print(squaredPower)

# A very strong Enemy is troubling the civilians, we need to send our superhereos to control and defeat the enemy! The enemy can only be defeated by heroes with powers above 15.
filterHeroes = list(filter(lambda x: x > 15, squaredPower))
print(filterHeroes)

# The UN has given our superhereos with some special scientific weapons! Let's give it to our heroes to increase their powers even more.
# Only certain heroes are selected for the new weapons.
heroes = ["Hulk", "Iron Man", "Spiderman"]
newWeapon = ["Embracer Gauntlet", "Electro Harnesser", "Flying Feet"]
strongTeam = list(zip(heroes, newWeapon))
print(strongTeam)

# Our team of superheroes
superheroes = ["Superman", "Ironman", "Spiderman", "Batman", "Wonder Woman"]

# 1. append()
# One day, the List League decided they needed a new member. They called upon "Hulk" to join their team.
superheroes.append("Hulk")
# Result: ["Superman", "Ironman", "Spiderman", "Batman", "Wonder Woman", "Hulk"]

# 2. insert()
# The List League wanted to place "Flash" at the second position because he is super fast.
superheroes.insert(1, "Flash")
# Result: ["Superman", "Flash", "Ironman", "Spiderman", "Batman", "Wonder Woman", "Hulk"]

# 3. remove()
# "Ironman" decided to take a vacation, so he temporarily left the team.
superheroes.remove("Ironman")
# Result: ["Superman", "Flash", "Spiderman", "Batman", "Wonder Woman", "Hulk"]

# 4. pop()
# "Batman" had to leave for a secret mission, so he popped out of the team.
superheroes.pop(3)
# Result: ["Superman", "Flash", "Spiderman", "Wonder Woman", "Hulk"]

# 5. index()
# The List League wanted to know where "Spiderman" was standing in the lineup.
position = superheroes.index("Spiderman")
# Result: 2 (because "Spiderman" is at the 3rd position, and lists are zero-indexed)

# 6. sort()
# The List League decided to stand in alphabetical order for a photo.
superheroes.sort()
# Result: ["Flash", "Hulk", "Spiderman", "Superman", "Wonder Woman"]

# 7. reverse()
# The List League wanted to see how they looked in reverse order.
superheroes.reverse()
# Result: ["Wonder Woman", "Superman", "Spiderman", "Hulk", "Flash"]

# 8. count()
# The List League wanted to know how many times "Superman" appeared in the list.
count_superman = superheroes.count("Superman")
# Result: 1

# 9. extend()
# The List League decided to team up with another group of heroes: ["Aquaman", "Cyborg"].
superheroes.extend(["Aquaman", "Cyborg"])
# Result: ["Wonder Woman", "Superman", "Spiderman", "Hulk", "Flash", "Aquaman", "Cyborg"]

# 10. slicing()
#  The List Leaague decided to find out the last three standing heroes of the team.
lastStanding = superheroes[4:]
print(lastStanding)

# 11. searching:
# The List League got worried that Hulk has taken off, they need to make sure if he is still there.
hulkPresent = "Hulk" in superheroes
print(hulkPresent)

# 12. 
# 11. clear()
# After a long day, the List League decided to take a break and clear the list.
superheroes.clear()
# Result: []

# Creating a list of squares of numbers from 0 to 99
squares = [x ** 3 for x in range(100)]

# Print the final state of the superheroes list and the count of Superman
print("Final superheroes list:", superheroes)
print("Count of Superman:", count_superman)
# print(squares)  

