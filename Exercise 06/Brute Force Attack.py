# Brute Force Attack

# Define the correct password
True_Password = "12345"

# Step 1: Keep asking for the password until it's correct password 
while True:
    # Prompt the user to enter the password
    Input_Password = input("Enter your password: ")

    # Step 2: Check if the entered password is correct
    if Input_Password == True_Password:
        print("Password Is Correct. Access granted.")
        break  # Exit the loop when the correct password is entered
    else:
        print("Incorrect password. Please try again.")
