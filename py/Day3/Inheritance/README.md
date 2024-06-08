# 🧸 Toy Adventure! 🧸

Welcome to the world of toys! In this adventure, we'll meet some amazing toys and learn about their special features. Let's dive in! 🌟

## 📚 Introduction

In this adventure, we have a **Toy** class that represents the basic features of any toy. Then, we have a special kind of toy called **WildAnimal** that has some unique features like legs and a voice. Let's see how they work!

## 🛠️ Code Explanation

### 1. The Toy Class 🎨

The **Toy** class is like a blueprint for all toys. It has two main features:
- **Name**: What the toy is called.
- **Color**: The color of the toy.

Here's how we define the **Toy** class:

```python
class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def whatToy(self):
        print(f"Meet {self.name}, the vibrant {self.color} color of {self.name} is loved by children all around the world!")
```

### 2. The WildAnimal Class 🐾

The **WildAnimal** class is a special kind of toy that inherits from the **Toy** class. This means it gets all the features of a toy (name and color) and adds some new ones:
- **Legs**: How many legs the animal has.
- **Voice**: The sound the animal makes.

Here's how we define the **WildAnimal** class:

```python
class WildAnimal(Toy):
    def __init__(self, name, color, legs, voice):
        super().__init__(name, color)
        self.legs = legs
        self.voice = voice

    def sound(self):
        print(f"Our friend {self.name} makes a {self.voice} sound!")
    
    def whatToy(self):
        super().whatToy()
        print(f"Hello kids! I have {self.legs} legs, and I will stay very loyal to you!")
```

### 3. Meet Rufus! 🐶

Let's create a wild animal toy named **Rufus** and see what he can do!

```python
wildAnimal = WildAnimal("Rufus", "Greyish - White", 4, "Ruff - Ruff")
wildAnimal.whatToy()
wildAnimal.sound()
```

When we run this code, Rufus will introduce himself and make his special sound!

## 🎉 Output

When you run the code, you'll see:

```
Meet Rufus, the vibrant Greyish - White color of Rufus is loved by children all around the world!
Hello kids! I have 4 legs, and I will stay very loyal to you!
Our friend Rufus makes a Ruff - Ruff sound!
```

## 📝 Summary

- **Toy Class**: The basic blueprint for all toys with name and color.
- **WildAnimal Class**: A special toy that has legs and makes a sound.
- **Rufus**: Our friendly wild animal toy who loves to play and make sounds!

We hope you enjoyed this toy adventure! Keep exploring and have fun with your toys! 🎈
Made with ❤️ by [Arreyan Hamid](https://github.com/GriffinBlackbirdd)
For any inquiries or feedback, please contact [arreyanhamid@icloud.com](mailto:arreyanhamid@icloud.com).