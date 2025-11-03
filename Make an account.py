# In-memory storage for multiple accounts
accounts = {}
logged_in_user = None  # Tracks the currently logged-in user

# Function to create an account
def create_account(username, password):
    if username in accounts:
        print("Username already exists!")
    else:
        accounts[username] = password
        print("Account created successfully!")

# Function to log in
def login(username, password):
    global logged_in_user
    if accounts.get(username) == password:
        logged_in_user = username
        print(f"Login successful! Welcome, {username}.")
    else:
        print("Invalid username or password!")

# Function to log out
def logout():
    global logged_in_user
    if logged_in_user:
        print(f"{logged_in_user} has logged out.")
        logged_in_user = None
    else:
        print("You are not logged in.")

# Function to delete the logged-in user's account
def delete_account():
    global logged_in_user
    if logged_in_user:
        del accounts[logged_in_user]
        print(f"Account '{logged_in_user}' has been deleted.")
        logged_in_user = None  # Log out after deleting the account
    else:
        print("You must be logged in to delete your account.")

# Function to update the logged-in user's password
def update_account(new_password):
    global logged_in_user
    if logged_in_user:
        accounts[logged_in_user] = new_password
        print("Password updated successfully!")
    else:
        print("You must be logged in to update your password.")

# Main program loop
while True:
    if logged_in_user:
        choice = input("\n2. Logout\n3. Delete Account\n4. Update Password\nChoose an option (2, 3, or 4): ")
        if choice == "2":
            logout()
        elif choice == "3":
            delete_account()
        elif choice == "4":
            new_password = input("Enter your new password: ")
            update_account(new_password)
        else:
            print("Invalid option. Please choose 2, 3, or 4.")
    else:
        choice = input("\n1. Create Account\n2. Login\nChoose an option (1 or 2): ")
        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            create_account(username, password)
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login(username, password)
        else:
            print("Invalid option. Please choose 1 or 2.")
