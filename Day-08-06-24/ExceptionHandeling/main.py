# Custom Made Exception
'''Here we have made an invalid gender error.'''

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

# FILE HANDLEING
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


# REQUESTS OR WEB ERRORS
'''You may run into issues when submitting network queries, 
such as the server not being reachable or the request expiring too soon.'''
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

# User-input checker
'''It may be necessary to properly handle faulty input while receiving input from users.'''
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


# Nested Exception Handling
'''Sometimes, you might need to handle exceptions within nested blocks of code.'''
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

# Using else.
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is {result}")
finally:
    print("Exception handling with else complete.")