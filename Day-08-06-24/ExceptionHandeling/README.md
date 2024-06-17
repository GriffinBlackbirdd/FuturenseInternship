# 🐍 Python Exception Handling Examples

Welcome to the **Python Exception Handling Examples** repository! This project showcases various ways to handle exceptions in Python, ensuring your programs run smoothly even when unexpected errors occur. Let's dive into the world of error handling with some cool examples! 🚀

## 📋 Table of Contents

1. [Custom Made Exception](#custom-made-exception)
2. [File Handling](#file-handling)
3. [Requests or Web Errors](#requests-or-web-errors)
4. [User Input Checker](#user-input-checker)
5. [Nested Exception Handling](#nested-exception-handling)
6. [Using Else](#using-else)

## Custom Made Exception

In this example, we create a custom exception called `InvalidGenderError` to handle invalid gender inputs. 🌈

```python
class InvalidGenderError(Exception):
    def __init__(self, gender, message="Gender must be 'male' or 'female'"):
        self.gender = gender
        self.message = message
        super().__init__(self.message)

def validate_gender(gender):
    if gender.lower() not in ['male', 'female']:
        raise InvalidGenderError(gender)
    return True

try:
    gender_input = "non-binary"
    validate_gender(gender_input)
except InvalidGenderError as e:
    print(f"InvalidGenderError: {e.gender} is not a valid gender. {e.message}")
```

## File Handling

Handling file operations can sometimes lead to errors like missing files or permission issues. Here's how to manage them gracefully. 📂

```python
try:
    with open('trial.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to read the file.")
finally:
    print("File handling operation complete.")
```

## Requests or Web Errors

When making network requests, you might encounter various errors. This example shows how to handle them. 🌐

```python
import requests

try:
    response = requests.get('https://example.com')
    response.raise_for_status()  # Raises an HTTPError for bad responses
    print(response.text)
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred: {req_err}")
finally:
    print("Network request operation complete.")
```

## User Input Checker

It's important to handle invalid user inputs gracefully. This example ensures the user enters a valid integer. 🔢

```python
def get_integer_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            value = int(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

number = get_integer_input("Enter an integer: ")
print(f"You entered: {number}")
```

## Nested Exception Handling

Sometimes, you need to handle exceptions within nested blocks of code. Here's how to do it. 🪆

```python
try:
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print(f"The result is {result}")
    except ValueError:
        print("Oops! That wasn't a number. Try again.")
except ZeroDivisionError:
    print("Oops! You can't divide by zero. Try again.")
finally:
    print("Nested exception handling complete.")
```

## Using Else

The `else` block runs if no exceptions are raised in the `try` block. This example demonstrates its usage. 🌟

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is {result}")
finally:
    print("Exception handling with else complete.")
```

Made with ❤️ by [Arreyan Hamid](https://github.com/GriffinBlackbirdd)
For any inquiries or feedback, please contact [arreyanhamid@icloud.com](mailto:arreyanhamid@icloud.com).