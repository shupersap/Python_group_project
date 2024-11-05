def start(option=None):
    print("Welcome to our app")
    option = input("Signup or Signin: ").lower()
    if option == "signin":
        signin_page()
    elif option == "signup":
        signup_page()
    else:
        print("Make sure you type either 'Signin' or 'Signup'")
        start(option=None)  


def signup_page(Username=None, Password=None):
    while True:
        Username = input("Enter a username: ")
        Password = input("Create a password: ")

        if not Username or not Password:
            print("Both username and password are required. Please try again.")
            continue

        try:
            with open("database.txt", "r") as db:
                stored_users = []
                for user_info in db:
                    if user_info.strip():  
                        username_stored, password_stored = user_info.split(",")
                        password_stored = password_stored.strip() 
                        stored_users.append(username_stored)

        except FileNotFoundError:
            stored_users = []

        if Username in stored_users:
            print("Username already exists.")
        else:
            with open("database.txt", "a") as db:
                db.write(f"{Username}, {Password}\n")  
            print("You have successfully created your account.")
            break 

def signin_page(Username=None, Password=None):
    while True:
        Username = input("Enter your username: ")
        Password = input("Enter your Password: ")

        if not Username or not Password:
            print("Both username and password are required. Please try again.")
            continue


        try:
            with open("database.txt", "r") as db:
                stored_user = []
                stored_pw = []
                for user_info in db:
                    if user_info.strip():  
                        username_stored, password_stored = user_info.split(",")
                        password_stored = password_stored.strip() 
                        stored_user.append(username_stored)
                        stored_pw.append(password_stored)

            user_dict = dict(zip(stored_user, stored_pw))


            if Username in user_dict:
                stored_password = user_dict[Username]
                if Password == stored_password:
                    print("Login success!")
                    print(f"Hi, {Username}")
                    break  
                else:
                    print("Wrong password.")
            else:
                print("Username doesn't exist.")

        except FileNotFoundError:
            print("Database file not found. Please sign up first.")
            break  
start()