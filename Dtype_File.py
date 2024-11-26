
#initializing dtype function
def dtype_Lesson():
    #welcoming user to lesson
    print("Welcome! Explore events based on different data types.")
    print("Pick a data type to learn more and try an example:")
    print("""
    1. String
    2. Integer
    3. Float
    4. List
    5. Boolean
    6. Exit to Home Page
    """)

    while True:
        lesson_learned_option = 0
        try:
            #ask the user to input a choice based on the menu options
            choice = int(input("Enter your choice (1-6): "))
            if choice == 1:
                lesson_learned_option=string_event()
            elif choice == 2:
                lesson_learned_option=integer_event()
            elif choice == 3:
                lesson_learned_option=float_event()
            elif choice == 4:
                lesson_learned_option=list_event()
            elif choice == 5:
                lesson_learned_option=boolean_event()
            elif choice == 6:
                print("Returning to the home page. Goodbye!")
                break
            #error handling if user doesn't pick a number between 1 and 6
            else:
                print("Please enter a valid number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        #continuation choice
        if lesson_learned_option == 1:
            dtype_Lesson() 
        elif lesson_learned_option == 2:
            break 



def string_event():
    print("Strings in python are surrounded by either single quotation marks, or double quotation marks")
    print("You can display a string literal with the function: print ()")
    print(" try using the print statement yourself to uilize a string")
    fav_food=str(input("what's your favorite food: "))
    print(f"I Love {fav_food} too")
    lesson_learned_option= int(input("\nPick from these options:\n 1: Learn more about data types\n 2: Back to the home page\n"))#ask the user if they want to learn more or go back to the home page
    print("-" * 80)
    return lesson_learned_option

def integer_event():
    print("Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.")
    print(" try using in statement yourself to utilize a integer")
    age = int(input("how old are you: "))
    print(f"You are wise for a {age} year old")
    lesson_learned_option= int(input("\nPick from these options:\n 1: Learn more about data types\n 2: Back to the home page\n"))#ask the user if they want to learn more or go back to the home page
    print("-" * 80)
    return lesson_learned_option
    
    
def float_event():
    print("Float, or floating point number is a number, positive or negative, containing one or more decimals.")
    print("You can display a float value with function:n float()")
    print("try using the float statments yourself")
    weight=float(input("what is your weight: "))
    print(f" So you weigh {weight} lbs")
    lesson_learned_option= int(input("\nPick from these options:\n 1: Learn more about data types\n 2: Back to the home page\n"))#ask the user if they want to learn more or go back to the home page
    print("-" * 80)
    return lesson_learned_option

def list_event():
    print("Lists are used to store multiple items in a single variable.")
    print("You can store multiple items using [] ")
    print("try using [] to ")
    tv_variable=input("what is your favorite tv show: ")
    movie_variable=input("what is your favorite movie: ")
    print(f"so these are what you like [ {tv_variable}  and {movie_variable} ]")
    lesson_learned_option= int(input("\nPick from these options:\n 1: Learn more about data types\n 2: Back to the home page\n"))#ask the user if they want to learn more or go back to the home page
    print("-" * 80)
    return lesson_learned_option

def boolean_event():
    print("Boolean represents whether a value will result or return in True or False.")
    print("you can display a booelean value with the function: bool()")
    print("-" * 80)
    print("try using the bool statement yourself to utilze a boolean value")
    likes_cats = input("Do you like cats? (y/n): ").strip().lower()
    is_true = bool(likes_cats == "y")
    if is_true:
        print("You really like cats!")
    else:
        print("You don't like cats? That's okay!")
    lesson_learned_option= int(input("\nPick from these options:\n 1: Learn more about data types\n 2: Back to the home page\n"))#ask the user if they want to learn more or go back to the home page
    print("-" * 80)
    return lesson_learned_option
    