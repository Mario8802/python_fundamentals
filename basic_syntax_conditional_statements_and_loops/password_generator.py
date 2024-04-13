import random
import string

def generate_password(length=12):
    # Define character sets for password generation
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Example usage:
password = generate_password()
print("Generated password:", password)

#hot or not ? 
