import sys
#function utilized to carry out prompt for each operator question, that will be utilized in the math_operator_lesson function
def get_loop_input(prompt, correct_answer):#Function created by Haslett
    while True:
        try:
            user_input = int(input("Answer: ")) #have user input what they think the answer to the question is 
            if user_input == correct_answer: #if the user is right, the function ends
                return True
            else: #if user is wrong, present prompt that could help them understand the answer
                print(f"Answer incorrect \n{prompt}")
        except ValueError:
            print("Please enter a valid number.")

#function that presents the details of each operator and their lesson
def loop_operator_lesson(operator, example,question, prompt, correct_answer,operator_symbol):#Function created by Daniel
    #based on each operator present a different scenario
    print(f"\n{operator} in Python utilizes the corresponding statement: {operator_symbol}")
    print(f"Example: {example}")
    print(f"\nTry it yourself, with this example:\n{question}")
    if get_loop_input(prompt, correct_answer):
        print(f"\nWell done, you have successfully understood how the {operator} loop feature is used!!")#congratulate user for understanding the operator
        lesson_learned_option = int(input("\nPick from these options:\n 1: Learn more about the loop features\n 2: Back to the home page\n"))#ask the user if they want to learn more or go back to the home page
        return lesson_learned_option

#Lesson start function so users can pick what they want to learn about
def Loop_Lesson():#Function created by Daniel
    while True:
        lesson_learned_option = 0
        try:
            #have users pick their option
            loop_user_inp = int(input("Pick from these options:\n 1: While loop \n 2: For loop \n 3: Continue statement \n 4: Pass statement \n 5: Break statement\n 6: Range function\n 7: Home Page \noption: "))
            
            #within each loop_lesson, the parameters are shifted based on what features are being used and how examples and answers should be structured
            if loop_user_inp == 1:
                lesson_learned_option = loop_operator_lesson("While loop,", "i = 0 \nwhile i < 6: print(i)  \ni = i + 1 \n i printed 5 times", "i = 1 \nwhile i != 10: print(i)  \ni = i + 1", "How many times is i printed? ", 9, "while:")
            elif loop_user_inp == 2:
                lesson_learned_option = loop_operator_lesson("For loop,", "fruits = [apple, banana, orange] \nfor x in fruits: \n  print(x)", "fruits = [apple,banana,orange,pineapple]","how many things are printed?", 4, "For:")
            elif loop_user_inp == 3:
                lesson_learned_option = loop_operator_lesson("Continue statement", "This statement allows you to continue a loop without breaking it", "if you put this after asking if x == banana if fruits = [apple, banana, orange]", "How many things would it print?", 2, "Continue")
            elif loop_user_inp == 4:
                lesson_learned_option = loop_operator_lesson("Pass statement", "This statement allows you to add a hidden variable that means nothing", "if you put pass after a loop went 3 times out of four, printing every time", "How many would it print?", 3, "Pass")
            elif loop_user_inp == 5:
                lesson_learned_option = loop_operator_lesson("Break statement", "This statement allows you to exist the current loop", "if you put this in a loop that went 5 times out of 10","How many times would it print?", 5, "Break")
            elif loop_user_inp == 6:
                lesson_learned_option = loop_operator_lesson("Range function", "Range function allows you to go through a loop a certain amount of times, starting from zero till it reaches the number", "if it was Range(6)","How many times would it print?", 6, "Range()")
            elif loop_user_inp == 7:
                break # Exit the loop if the user selects 'Home Page'
            else:
                print("Please input a number between 1 and 7")

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 7.")
            continue
        #based on the result returned in the loop_lesson function, on if the user wants to continue learning or go back home
        if lesson_learned_option == 1:
            continue #continue look
        elif lesson_learned_option == 2:
            break #go to home page