#import external libraries
import sys

#call functions stored within files in the current working directory's path
from Math_Operator_File import Math_op_Lesson
from List_Lesson_File import list_lessons
from Loop_Lesson_File import Loops_Lesson

#initialize start page
def start(option=None):
    print("Welcome to our app")
    option = input("Signup or Signin: ").lower() #assess whether user wants to sign up or signin
    #allow activation of sign in and sign up function
    if option == "signin":
        signin_page()
    elif option == "signup":
        signup_page()
    elif option == "quit":
        sys.exit("Hope to see you again")
    #if either options are not selected, restart the start selection
    else:
        print("Make sure you type either 'Signin' or 'Signup', or 'quit' if you want to exit the application")
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
            continue

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
            print(f"You have successfully created your account {Username}")
            home_page(Username,Password)

#signin page function initialized
def signin_page(Username=None,Password=None):
    while True:
        #have users enter their credentials
        Username = input("Enter your username: ")
        Password = input("Enter your Password: ")
        
        #if the fields are left blank, they must redo the signin process
        if not Username or not Password:
            print("Both username and password are required. Please try again.")
            continue

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
                    home_page(Username,Password)
                    break
                else:
                    print("Wrong password.")
            else:
                print("Username doesn't exist.")

        #If there is no database information, a sign up must be made first
        except FileNotFoundError:
            print("Database file not found. Please sign up first.")
            signup_page()  


def home_page(home_user,home_pw):

    #Track user clicks on each topic through a dictionary pair
    topic_clicks = {'Loops': 0, 'Lists': 0, 'Math operations': 0}
    topic_clicks = load_user_data(home_user, topic_clicks) #check to see if a user has used the application before and collect that info from the database

    #welcome users
    print(f"Welcome to the tuition center {home_user}\nHere to help you advance in your programming journey \n")
    while True:
        menu_selection = option_display()  # Store the result of option_display() here
        try:
            #reminder user to pick one of the numerical options
            if menu_selection not in [1,2,3,4]: 
                print("please choose a number between 1 and 4 \n")
                continue
            #direct each option to an imported function from outside files
            elif menu_selection == 1:
                topic_clicks['Loops'] += 1 
                Loops_Lesson()
            elif menu_selection == 2:
                topic_clicks['Lists'] += 1
                Lists_Lesson()
            elif menu_selection == 3:
                topic_clicks["Math operations"] += 1
                print("So you want to learn more about math operations in python, do you")
                print("Well we got the one stop shop for you")
                Math_op_Lesson()
            elif menu_selection == 4:
                print("After a while crocodile \nHope to see you again")
                log_user_activity(home_user, topic_clicks)
                break
        #extra layer of user error prevention
        except ValueError:
            print("Please choose a number between 1 and 4")
            continue

def load_user_data(home_user, topic_clicks):
    try:
        # Open the database file in read mode to get existing users
        with open("database.txt", "r") as db:
            lines = db.readlines()

        # Search for the user's line in the database and load their topic click data
        for line in lines:
            username_stored, password_stored, *topic_data = line.strip().split(",")
            if username_stored == home_user:
                # Extract topic click counts and update the dictionary
                for topic in topic_data:
                    topic_name, count = topic.split(":")
                    if topic_name in topic_clicks:
                        topic_clicks[topic_name] = int(count)
                break
    except FileNotFoundError:
        print("Database file not found. New user session initiated.")
    
    return topic_clicks

# Function to log the user's activity to the database.txt file
def log_user_activity(home_user, topic_clicks):
    try:
        # Open the database file in read mode to get existing users
        with open("database.txt", "r") as db:
            lines = db.readlines()

        # Check if the user's data already exists
        user_found = False
        for i, line in enumerate(lines):
            username_stored, password_stored, *topic_data = line.strip().split(",")
            if username_stored == home_user:
                user_found = True
                # Update the user's topic click data in the database
                new_data = f"{home_user},{password_stored}," + ",".join([f"{key}:{value}" for key, value in topic_clicks.items()])
                lines[i] = new_data + "\n"
                break

        # If the user wasn't found, add a new line with their activity
        if not user_found:
            new_data = f"{home_user},<password_placeholder>," + ",".join([f"{key}:{value}" for key, value in topic_clicks.items()])
            lines.append(new_data + "\n")

        # Write the updated data back to the file
        with open("database.txt", "w") as db:
            db.writelines(lines)

    except FileNotFoundError:
        # If the file doesn't exist, create it and add the user's data
        with open("database.txt", "w") as db:
            new_data = f"{home_user},<password_placeholder>," + ",".join([f"{key}:{value}" for key, value in topic_clicks.items()])
            db.write(new_data + "\n")


#initialized function to display menu selections
def option_display():
    print("Pick a number to learn more about that topic")
    print(" 1:Loops \n 2:Lists \n 3:Math operators \n 4:Exit application")
    pick= int(input("Which option would you like to select? "))
    return pick


def logging():
    return

start()