import random
import string

def generate_password(length=12):
    # Define characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting 'length' characters from the pool of 'characters'
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Usage example
if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    
    if password_length <= 0:
        print("Password length must be greater than 0.")
    else:
        generated_password = generate_password(password_length)
        print("Generated Password:", generated_password)
