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

def home_page(Username,Password):
    print("Welcome to the tuition center \n Here to help you advance in your programming journey")
    option_display()
    while True:
        try:
            if menu_selection not in [1,2,3,4]: 
                print("please choose a number between 1 and 4")
                option_display()
            elif menu_selection == 1:
                Loops_Lesson()
            elif menu_selection == 2:
                Lists_Lesson()
            elif menu_selection == 3:
                print("So you want to learn more about math operations in python, do you")
                print("Well we got the one stop shop for you")
                Math_op_Lesson()
            elif menu_selection == 4:
                print("After a while crocodile \n Hope to see you again")
                break
        
        except ValueError:
            print("Please choose a number between 1 and 4")
            option_display()

   
def option_display():
    print("Pick a number to learn more about that topic")
    print("1:Loops \n 2:Lists \n 3:Math operators \n 4:Exit application")
    menu_selection=int(input("Which option would you like to select? "))
    return menu_selection


def logging():
    return
