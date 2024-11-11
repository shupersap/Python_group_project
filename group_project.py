#initialize start page
def start(option=None):
    print("Welcome to our app")
    option = input("Signup or Signin: ").lower() #assess whether user wants to sign up or signin
    #allow activation of sign in and sign up function
    if option == "signin":
        signin_page()
    elif option == "signup":
        signup_page()
    #if either option is not selected, restart the start selection
    else:
        print("Make sure you type either 'Signin' or 'Signup'")
        start(option=None)  

#signup page function initialized
def signup_page(Username=None, Password=None):
    while True:
        #Store user's username and password
        Username = input("Enter a username: ")
        Password = input("Create a password: ")
        
        #if field is left blank restart the process
        if not Username or not Password:
            print("Both username and password are required. Please try again.")
            signup_page

        try:
            #open up database text file
            with open("database.txt", "r") as db:
                stored_users = []
                #search through each user's details  
                for user_info in db:
                    if user_info.strip():  
                        #split the stored data for each user to obtain the username
                        username_stored, password_stored = user_info.split(",")
                        password_stored = password_stored.strip() 
                        stored_users.append(username_stored)

        except FileNotFoundError:
            stored_users = []
        #make sure the user doesn't use a username that already exists 
        if Username in stored_users:
            print("Username already exists.")

        #if username not found, submit user and password into database
        else:
            with open("database.txt", "a") as db:
                db.write(f"{Username}, {Password}\n")  
            print("You have successfully created your account.")
            break 

#signin page function initialized
def signin_page(Username=None, Password=None):
    while True:
        #have users enter their credentials
        Username = input("Enter your username: ")
        Password = input("Enter your Password: ")
        
        #if the fields are left blank, they must redo the signin process
        if not Username or not Password:
            print("Both username and password are required. Please try again.")
            signin_page()

        try:
            #open database file
            with open("database.txt", "r") as db:
                stored_user = []
                stored_pw = []
                for user_info in db:
                    #find the seperated password and user id within the database
                    if user_info.strip():  
                        username_stored, password_stored = user_info.split(",")
                        password_stored = password_stored.strip() 
                        stored_user.append(username_stored)
                        stored_pw.append(password_stored)

            #initialize dictionary to hold username as key and password as value
            user_dict = dict(zip(stored_user, stored_pw))

            #check to see if the value in the dictionary matches the entered data
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

        #If there is no database information, a sign up must be made first
        except FileNotFoundError:
            print("Database file not found. Please sign up first.")
            break  


def home_page(Username,Password):
    #welcome users
    print("Welcome to the tuition center \n Here to help you advance in your programming journey")
    #utilize options function
    option_display()
    while True:
        try:
            #reminder user to pick one of the numerical options
            if menu_selection not in [1,2,3,4]: 
                print("please choose a number between 1 and 4")
                option_display()
            #direct each option to an imported function from outside files
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

        #extra layer of user error prevention
        except ValueError:
            print("Please choose a number between 1 and 4")
            option_display()

#initialized function to display menu selections
def option_display():
    print("Pick a number to learn more about that topic")
    print("1:Loops \n 2:Lists \n 3:Math operators \n 4:Exit application")
    menu_selection=int(input("Which option would you like to select? "))
    return menu_selection


def logging():
    return

start()