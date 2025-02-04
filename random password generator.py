import random
import string

print("Welcome to Password Generator")
req_length = int(input("Enter the Specified Length for password: "))

# Character sets
uppercase_chars = string.ascii_uppercase
lowercase_chars = string.ascii_lowercase
digits = string.digits
special_chars = string.punctuation

# Ask user for character type preferences
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

# Build the character pool based on user input
char_pool = string.ascii_lowercase  # Always include lowercase letters
if use_uppercase:
    char_pool += uppercase_chars
if use_numbers:
    char_pool += digits
if use_special_chars:
    char_pool += special_chars

# Generate password
password = ''.join(random.choice(char_pool) for _ in range(req_length))

print("Your Generated Password is:", password)
