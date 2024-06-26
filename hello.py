import random
 
# Function to generate a random password
def generate_password(length=8):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
 
# Generate a random password of length 12
print("Generated Password:", generate_password(12))