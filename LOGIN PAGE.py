x = 'C:/Users/7seas/Desktop/PYTHON/user_information.txt'  # Set the global variable for the file path

def read_user_data():
    users_data = []

    with open(x, 'r') as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_password = (part.strip() for part in line.split(':'))
            user_data = {'username': stored_username, 'password': stored_password}
            users_data.append(user_data)

    return users_data

def login():
    users_data = read_user_data()

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if the entered username and password match the signup data
        for user_data in users_data:
            if username == user_data['username'] and password == user_data['password']:
                print("Login successful!")
                return

        print("Invalid username or password. Please try again.")

# Example usage
login()
