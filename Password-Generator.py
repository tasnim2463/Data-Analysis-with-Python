import random
import string

def generate_password(length=12):
    """Generates a strong password with a mix of characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length
length = int(input("Enter the desired password length: "))
strong_password = generate_password(length)
print(f"Your generated password: {strong_password}")
