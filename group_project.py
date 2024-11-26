#import external libraries
import sys
import os 

#call functions stored within files in the current working directory's path
from Math_Operator_File import Math_op_Lesson
from Dtype_File import dtype_Lesson
from Loop_Lesson_File import Loop_Lesson


#initialize start page
def start(option=None):#Function created by Haslett
    #welcom user
    print("-" * 80)
    print("Welcome to Python Journey")
    print("The app here to help you excel in your coding journey \n")
    print("Made by DHR Studios")
    print("-" * 80)
    option = str(input("Signup or Signin: ")).lower() #assess whether user wants to sign up or signin
    #allow options to run functions/calls related to selection
    if option == "signin":
        signin_page()
    elif option == "signup":
        signup_page()
    elif option == "quit":
        sys.exit("Hope to see you again")
    #if either options are not selected, restart the start selection
    else:
        print("Make sure you type either 'signin' or 'signup', or 'quit' if you want to exit the application")
        start(option=None)  

#signup page function initialized
def signup_page(Username=None, Password=None):#Function created by Haslett
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
                #initialize empty list
                stored_users = []
                #search through each user's details  
                for user_info in db:
                    #clear whitespace in extracted data
                    if user_info.strip():
                        #only extract the first two variables seperated by a comma 
                        parts = user_info.split(",", 2)
                        username_stored= parts[0] #obtain the username portion
                        username_stored=username_stored.strip()
                        stored_users.append(username_stored)#append the usernames to a list

        #if file not found or database is just initialized
        except FileNotFoundError:
            stored_users = []
        #make sure the user doesn't use a username that already exists 
        if Username in stored_users:
            print("Username already exists.")
            start()
        #if username is not used already, submit user and password into database
        else:
            with open("database.txt", "a") as db:
                db.write(f"{Username}, {Password}\n")  
            print(f"You have successfully created your account {Username}")
            print("-" * 80)
            home_page(Username) # have user immediately enter the application based on their username

#signin page function initialized
def signin_page(Username=None,Password=None):#Function created by Haslett
    while True:
        #have users enter their credentials
        Username = input("\nEnter your username: ")
        Password = input("Enter your Password: ")
        
        #if the fields are left blank, they must redo the signin process
        if not Username or not Password:
            print("Both username and password are required. Please try again.")
            continue

        try:
            #open database file
            with open("database.txt", "r") as db:
                #initialize empty lists
                stored_user = []
                stored_pw = []
                for user_info in db:
                    #find the seperated password and username within the database
                    if user_info.strip():
                        parts = user_info.split(",", 2)#extract first two variables 
                        username_stored, password_stored = parts[0], parts[1]#extract username and password values, respectively
                        username_stored=username_stored.strip()
                        password_stored = password_stored.strip()  # Remove extra spaces around password
                        #append username and passwords
                        stored_user.append(username_stored)
    
                        stored_pw.append(password_stored)

            #initialize dictionary to hold username as key and password as value
            user_dict = dict(zip(stored_user, stored_pw))

            #check to see if the value in the dictionary matches the entered data
            if Username in user_dict:
                stored_password = user_dict[Username]
                if Password == stored_password:
                    print("Login success!")
                    print("-" * 80)
                    home_page(Username)
                    break
                else:
                    print("Wrong password.")
                    start()  
            else:
                print("Username doesn't exist.")
                start()

        #If there is no database information, a sign up must be made first
        except FileNotFoundError:
            print("Database file not found. Please sign up first.")
            signup_page()  

#function to store home page detailing
def home_page(home_user):#Function created by Haslett

    #Track user clicks on each topic through a dictionary pair
    topic_clicks = {'Loops': 0, 'Dtypes': 0, 'Math operations': 0}
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
                print("-" * 80)
                topic_clicks['Loops'] += 1 
                Loop_Lesson()
            elif menu_selection == 2:
                print("-" * 80)
                topic_clicks['Dtypes'] += 1
                dtype_Lesson()
            elif menu_selection == 3:
                topic_clicks["Math operations"] += 1
                print("-" * 80)
                print("So you want to learn more about math operations in python, do you")
                print("Well we got the one stop shop for you")
                Math_op_Lesson()
            elif menu_selection == 4:
                #when exiting the application, log the final results of user's session
                log_user_activity(home_user, topic_clicks)
                sys.exit("\nAfter a while crocodile \nHope to see you again")
        #extra layer of user error prevention
        except ValueError:
            print("Please choose a number between 1 and 4")
            continue

#read in user details, specifically in regards to logging data
def load_user_data(home_user, topic_clicks): #Function created by Haslett
    try:
        # Open the database file to read in existing users
        with open("database.txt", "r") as db:
            lines = db.readlines()

        # Search for the user's line in the database and load their topic click data
        for line in lines:
            parts = line.strip().split(",")
            username_stored = parts[0]

            if username_stored == home_user:
                # If topic data is already present for the current user
                if len(parts) > 2: 
                    for topic in parts[2:]:
                        topic_name, count = topic.split(":") #split based on key:value pairing
                        if topic_name in topic_clicks:
                            topic_clicks[topic_name] = int(count) #collect count of user's prior clicks
                else:
                    # If no topic data exists for the user, initialize with default
                    print(f"Warning: {home_user} has no topic data, initializing default.")
                break
        else:
            # If the user isn't found in the database, return the default topic_clicks
            print(f"New user detected: {home_user}, initializing default data.")
    
    except FileNotFoundError:
        print("Database file not found. Starting new user session.")
    
    return topic_clicks

# Function to log the user's activity to the database file
def log_user_activity(home_user, topic_clicks):#Function created by Haslett
    user_found = False
    try:
        if os.path.exists("database.txt"):
            #read in database data
            with open("database.txt", "r+") as db:
                lines = db.readlines()

                # Check if the user already exists in the database
                for i, line in enumerate(lines):
                    parts = line.strip().split(",")
                    username_stored = parts[0]

                    #if the current user is found in the db
                    if username_stored == home_user:
                        user_found = True
                        # Retain the original password and update topic data
                        password_stored = parts[1]  # Store the original password
                        updated_data = f"{home_user},{password_stored}," + ",".join([f"{key}:{value}" for key, value in topic_clicks.items()]) # based on each topic click update the data
                        lines[i] = updated_data + "\n"
                        break

                # If the user wasn't found, print a message and exit the function
                if not user_found:
                    print(f"Error: User '{home_user}' not found in the database.")
                    return  # Exit early

                # Rewind and write back the modified file
                db.seek(0)
                db.writelines(lines)

        else:
            # Handle case where the database file doesn't exist
            print("Error: Database file not found.")
            return  # Exit early

    except FileNotFoundError:
        # Handle the case where the file doesn't exist or other IO errors
        print("Error: Database file not found.")
        return  # Exit early

#initialized function to display menu selections
def option_display():#Function created by Haslett
    print("Pick a number to learn more about that topic or quit the application:")
    print(" 1:Loops \n 2:Data Types \n 3:Math operators \n 4:Exit application\n")
    pick= int(input("Which option would you like to select? "))
    return pick



start()#start program when file is run
