def checking_username(username):
    # Check if the username already exists in the file
    with open('user_information.txt', 'r') as file:
        lines = file.readlines()
        existing_usernames = [line.split(':')[0].strip() for line in lines]

    return username in existing_usernames

def signup():
    while True:
        # Get user input
        username = input("Enter your username: ")

        # Check if the username is already taken
        while True:
            if checking_username(username):
                print("Username is already taken!!!. Please choose a different username.")
            else:
                break

        return

        password = input("Enter your password: ")

        # Validate password (at least 8 characters, one uppercase, one lowercase, one digit)
        if len(password) < 8 or not any(char.islower() for char in password) \
                or not any(char.isupper() for char in password) \
                or not any(char.isdigit() for char in password):
            print("Password must be at least 8 characters, include one uppercase letter, one lowercase letter, and one digit.")
        else:
            break
        
    # Save username and password to a file (append mode)
    with open('user_information.txt', 'a') as file:
        file.write(f"{username}:{password}\n")

    print("Signup successful!")

# Example usage
signup()
