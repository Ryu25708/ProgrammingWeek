import getpass

def check_password():
    password = getpass.getpass("Please enter your password: ")

    if password == "secret123":
        print("Login successful!")
    else:
        print("Incorrect password!")

check_password()
