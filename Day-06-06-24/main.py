'''
@author: Arreyan Hamid
@date: 2024-06-06

This program fulfills the requirements of Day 1 task of my Internship at Futurense PVT. LTD.
The program provides the following functionalities:
    1. Calculate the area of a certain Shapes - Made use of Lambda Functions
    2. Reverse the words in a string - Made use of Python's string manipulation functions
    3. Analyze a list of numbers - Made use of Python's built-in functions like min, max, sum, etc.
    4. Filter short names from a list of names - Made use of Python's filter function
    5. Analyze text by counting the number of words, characters, and finding the most frequent word - Made use of NLTK library for tokenization and Counter for counting

I have made a menu driven program to showcase the following tasks, and I have made use of various libraries like math, re, collections, nltk, rich, etc. to achieve the desired functionalities.

Mentored by - Mr Ziyaad Mahudawala.
'''


import math
import re
from collections import Counter
import nltk
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

nltk.download('punkt')

class MAIN:
    def __init__(self):
        self.area_calculators = {
            "rectangle": lambda dims: dims[0] * dims[1] if len(dims) == 2 else self._raise_value_error("Rectangle requires two dimensions: length and width."),
            "square": lambda dims: dims[0] ** 2 if len(dims) == 1 else self._raise_value_error("Square requires one dimension: side length."),
            "triangle": lambda dims: 0.5 * dims[0] * dims[1] if len(dims) == 2 else self._raise_value_error("Triangle requires two dimensions: base and height."),
            "trapezoid": lambda dims: 0.5 * (dims[0] + dims[1]) * dims[2] if len(dims) == 3 else self._raise_value_error("Trapezoid requires three dimensions: top base, bottom base, and height."),
            "circle": lambda dims: math.pi * (dims[0] ** 2) if len(dims) == 1 else self._raise_value_error("Circle requires one dimension: radius.")
        }
        self.console = Console()

    def _raise_value_error(self, message):
        raise ValueError(message)

    def calculate_area(self, shape, dimensions):
        shape = shape.lower()
        if shape in self.area_calculators:
            return self.area_calculators[shape](dimensions)
        else:
            raise ValueError("ONLY rectangle, square, triangle, trapezoid, and circle are supported. Please enter a valid shape.")

    def get_user_input(self):
        shape = Prompt.ask("Enter the shape (rectangle, circle)").strip().lower()
        
        if shape == "rectangle":
            length = float(Prompt.ask("Enter the length of the rectangle"))
            width = float(Prompt.ask("Enter the width of the rectangle"))
            dimensions = [length, width]
        elif shape == "square":
            side = float(Prompt.ask("Enter the side length of the square"))
            dimensions = [side]
        elif shape == "triangle":
            base = float(Prompt.ask("Enter the base of the triangle"))
            height = float(Prompt.ask("Enter the height of the triangle"))
            dimensions = [base, height]
        elif shape == "trapezoid":
            top_base = float(Prompt.ask("Enter the top base of the trapezoid"))
            bottom_base = float(Prompt.ask("Enter the bottom base of the trapezoid"))
            height = float(Prompt.ask("Enter the height of the trapezoid"))
            dimensions = [top_base, bottom_base, height]
        elif shape == "circle":
            radius = float(Prompt.ask("Enter the radius of the circle"))
            dimensions = [radius]
        else:
            raise ValueError("ONLY rectangle, square, triangle, trapezoid, and circle are supported. Please enter a valid shape.")
        
        return shape, dimensions

    def reverse_words(self, text):
        words = text.split()
        reversed_words = words[::-1]
        reversed_text = ' '.join(reversed_words)
        return reversed_text

    def analyze_list(self, numbers):
        if not numbers:
            raise ValueError("The list is empty. Please provide a list with at least one number.")
        min_value = min(numbers)
        max_value = max(numbers)
        average_value = sum(numbers) / len(numbers)

        statistics = {
            "min": min_value,
            "max": max_value,
            "average": average_value
        }
        
        return statistics

    def filter_short_names(self, names, max_length):
        filtered_names = list(filter(lambda name: len(name) < max_length, names))
        return filtered_names

    def analyze_text(self, text):
        words = nltk.word_tokenize(text.lower())
        word_count = len(words)
        characters = re.sub(r'\s+', '', text)
        char_count = len(characters)
        word_freq = Counter(words)
        most_frequent_word = word_freq.most_common(1)[0][0]
        return {
            'word_count': word_count,
            'char_count': char_count,
            'most_frequent_word': most_frequent_word
        }

    def display_menu(self):
        print("")
        menu_text = Text("Menu:", style="bold underline")
        menu_text.append("\n1. Calculate area", style="bold green")
        menu_text.append("\n2. Reverse words in a string", style="bold green")
        menu_text.append("\n3. Analyze a list of numbers", style="bold green")
        menu_text.append("\n4. Filter short names", style="bold green")
        menu_text.append("\n5. Analyze text", style="bold green")
        menu_text.append("\n6. Exit", style="bold green")
        self.console.print(menu_text)

    def run(self):
        while True:
            self.display_menu()
            choice = Prompt.ask("Enter your choice (1-6)").strip()
            
            if choice == '1':
                try:
                    shape, dimensions = self.get_user_input()
                    area = self.calculate_area(shape, dimensions)
                    self.console.print(f"The area of the {shape} is: {area}", style="bold blue")
                except ValueError as e:
                    self.console.print(f"[bold red]{e}[/bold red]")
            elif choice == '2':
                text = Prompt.ask("Enter the text to reverse words").strip()
                reversed_text = self.reverse_words(text)
                self.console.print(f"Original text: {text}", style="bold blue")
                self.console.print(f"Reversed words text: {reversed_text}", style="bold blue")
            elif choice == '3':
                try:
                    numbers = list(map(float, Prompt.ask("Enter a list of numbers separated by spaces").strip().split()))
                    stats = self.analyze_list(numbers)
                    self.console.print(f"Statistics: {stats}", style="bold blue")
                except ValueError as e:
                    self.console.print(f"[bold red]{e}[/bold red]")
            elif choice == '4':
                try:
                    names = Prompt.ask("Enter a list of names separated by spaces").strip().split()
                    max_length = int(Prompt.ask("Enter the maximum length for names"))
                    filtered_names = self.filter_short_names(names, max_length)
                    self.console.print(f"Filtered names: {filtered_names}", style="bold blue")
                except ValueError as e:
                    self.console.print(f"[bold red]{e}[/bold red]")
            elif choice == '5':
                text = Prompt.ask("Enter the text to analyze").strip()
                stats = self.analyze_text(text)
                self.console.print(f"Text analysis: {stats}", style="bold blue")
            elif choice == '6':
                self.console.print("Exiting the program.", style="bold yellow")
                break
            else:
                self.console.print("Invalid choice. Please enter a number between 1 and 6.", style="bold red")

if __name__ == "__main__":
    calculator = MAIN()
    calculator.run()