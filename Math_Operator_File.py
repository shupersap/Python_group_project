import sys

#function utilized to carry out prompt for each operator question, that will be utilized in the math_operator_lesson function
def get_math_input(prompt, correct_answer):#Function created by Haslett
    while True:
        try:
            user_input = int(input("Answer: ")) #have user input what they think the answer to the question is 
            if user_input == correct_answer: #if the user is right, the function ends
                return True
            else: #if user is wrong, present prompt that could help them understand the answer
                print(prompt)
        except ValueError:
            print("Please enter a valid number.")

#function that presents the details of each operator and their lesson
def math_operator_lesson(operator, example,question, prompt, correct_answer,operator_symbol):#Function created by Haslett
    #based on each operator present a different scenario
    print(f"\n{operator} in Python utilizes the corresponding operator: {operator_symbol}")
    print(f"Example: {example}")
    print(f"\nTry it yourself, with this equation:\n{question}")
    if get_math_input(prompt, correct_answer):
        print(f"\nWell done, you have successfully understood how the {operator} operator is used!!")#congratulate user for understanding the operator
        lesson_learned_option = int(input("\nPick from these options:\n 1: Learn more about the math operators\n 2: Back to the home page\n"))#ask the user if they want to learn more or go back to the home page
        return lesson_learned_option

#Lesson start function so users can pick what they want to learn about
def Math_op_Lesson():#Function created by Haslett
    while True:
        lesson_learned_option = 0
        try:
            #have users pick their option
            math_user_inp = int(input("Pick from these options:\n 1: Addition \n 2: Subtraction \n 3: Multiplication \n 4: Division \n 5: Modulus\n 6: Exponential\n 7: Home Page \noption: "))
            
            #within each math_operator_lesson, the parameters are shifted based on what operations are being used and how examples and answers should be structured
            if math_user_inp == 1:
                lesson_learned_option = math_operator_lesson("Addition", "5 + 22 = 27", "8 + x = 15", "What number would add to 8 to make 15? ", 7, "+")
            elif math_user_inp == 2:
                lesson_learned_option = math_operator_lesson("Subtraction", "13 - 5 = 8", "21 - x = 9", "What number would subtract from 21 to make 9? ", 12, "-")
            elif math_user_inp == 3:
                lesson_learned_option = math_operator_lesson("Multiplication", "6 * 4 = 24", "x * 7 = 21", "What number would multiply by 7 to be 21? ", 3, "*")
            elif math_user_inp == 4:
                lesson_learned_option = math_operator_lesson("Division", "15 / 5 = 3", "27 / x = 3", "What number would divide 27 by to make 3? ", 9, "/")
            elif math_user_inp == 5:
                lesson_learned_option = math_operator_lesson("Modulus", "20 % 15 = 5", "12 % x = 2", "What number would divide by 12 to give a remainder of 2? ", 10, "%")
            elif math_user_inp == 6:
                lesson_learned_option = math_operator_lesson("Exponential", "4 ** 3 = 64", "3 ** x = 27", "What number raised to the power of x will result in 27? ", 3, "**")
            elif math_user_inp == 7:
                break # Exit the loop if the user selects 'Home Page'
            else:
                print("Please input a number between 1 and 7")

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 7.")
            continue
        #based on the result returned in the math_operator_lesson function, on if the user wants to continue learning or go back home
        if lesson_learned_option == 1:
            continue #continue look
        elif lesson_learned_option == 2:
            break #go to home page







