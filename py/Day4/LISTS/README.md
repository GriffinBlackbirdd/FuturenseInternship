```markdown
# 🦸‍♂️ The List League: A Superhero Adventure 🦸‍♀️

Welcome to the **List League**! This is a fun and educational Python script that showcases various list operations using a team of superheroes. Follow along as our heroes combine their powers, face challenges, and manage their team dynamics.

## 🚀 Features

1. **Combining Powers**: Using the `reduce` function to sum up the power levels of the superheroes.
2. **Power Boost**: Squaring the power levels of the superheroes using the `map` function.
3. **Filtering Heroes**: Filtering out heroes with power levels above a certain threshold using the `filter` function.
4. **Equipping Weapons**: Pairing superheroes with special weapons using the `zip` function.
5. **List Operations**: Demonstrating various list operations such as `append`, `insert`, `remove`, `pop`, `index`, `sort`, `reverse`, `count`, `extend`, slicing, searching, and `clear`.

## 📜 Script Overview

### Combining Powers
```python
from functools import reduce

superheroes = {
    "Superman": 1,
    "Ironman": 2,
    "Spiderman": 3,
    "Batman": 4,
    "Wonder Woman": 5
}

power_levels = list(superheroes.values())
total_power = reduce(lambda x, y: x + y, power_levels)
print("Total power of the List League:", total_power)
```

### Power Boost
```python
squaredPower = list(map(lambda x: x ** 2, power_levels))
print(squaredPower)
```

### Filtering Heroes
```python
filterHeroes = list(filter(lambda x: x > 15, squaredPower))
print(filterHeroes)
```

### Equipping Weapons
```python
heroes = ["Hulk", "Iron Man", "Spiderman"]
newWeapon = ["Embracer Gauntlet", "Electro Harnesser", "Flying Feet"]
strongTeam = list(zip(heroes, newWeapon))
print(strongTeam)
```

### List Operations
```python
superheroes = ["Superman", "Ironman", "Spiderman", "Batman", "Wonder Woman"]

# Append
superheroes.append("Hulk")

# Insert
superheroes.insert(1, "Flash")

# Remove
superheroes.remove("Ironman")

# Pop
superheroes.pop(3)

# Index
position = superheroes.index("Spiderman")

# Sort
superheroes.sort()

# Reverse
superheroes.reverse()

# Count
count_superman = superheroes.count("Superman")

# Extend
superheroes.extend(["Aquaman", "Cyborg"])

# Slicing
lastStanding = superheroes[4:]
print(lastStanding)

# Searching
hulkPresent = "Hulk" in superheroes
print(hulkPresent)

# Clear
superheroes.clear()
```

### Creating a List of Squares
```python
squares = [x ** 3 for x in range(100)]
```

## 📝 Final Output
```python
print("Final superheroes list:", superheroes)
print("Count of Superman:", count_superman)
```

## 📚 Learning Outcomes

- Understand how to use Python's `reduce`, `map`, and `filter` functions.
- Learn various list operations and their practical applications.
- Get familiar with list comprehensions for creating lists efficiently.

## 🎉 Enjoy the Adventure!

Made with ❤️ by [Arreyan Hamid](https://github.com/GriffinBlackbirdd)
For any inquiries or feedback, please contact [arreyanhamid@icloud.com](mailto:arreyanhamid@icloud.com).