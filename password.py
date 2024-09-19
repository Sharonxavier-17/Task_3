import random
import string

# Function to generate a password
def generate_password(length):
    # Define the character set (letters, digits, and punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main code
try:
    # Prompt the user to input the desired password length
    length = int(input("Enter the desired length for your password: "))
    
    if length < 6:
        print("Password length should be at least 6 characters for security.")
    else:
        # Generate the password
        password = generate_password(length)

        # Display the generated password
        print(f"Generated Password: {password}")

except ValueError:
    print("Invalid input! Please enter a valid number for the password length.")
            
