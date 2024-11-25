import sys

def get_math_input(prompt, correct_answer):
    while True:
        try:
            user_input = int(input("Answer: "))
            if user_input == correct_answer:
                return True
            else:
                print(prompt)
        except ValueError:
            print("Please enter a valid number.")

def math_operator_lesson(operator, example,question, prompt, correct_answer,operator_symbol):
    print(f"\n{operator} in Python utilizes the corresponding operator: {operator_symbol}")
    print(f"Example: {example}")
    print(f"\nTry it yourself, with this equation:\n{question}")
    if get_math_input(prompt, correct_answer):
        print(f"\nWell done, you have successfully understood how the {operator} operator is used!!")
        lesson_learned_option = int(input("\nPick from these options:\n 1: Learn more about the math operators\n 2: Back to the home page \n 3: Exit the application\n"))
        return lesson_learned_option

def Math_op_Lesson():
    while True:
        lesson_learned_option = 0
        try:
            math_user_inp = int(input("Pick from these options:\n 1: Addition \n 2: Subtraction \n 3: Multiplication \n 4: Division \n 5: Modulus\n 6: Exponential\n 7: Home Page \noption: "))
            
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

        if lesson_learned_option == 1:
            continue
        elif lesson_learned_option == 2:
            break
        elif lesson_learned_option == 3:
            sys.exit()




"""def Math_op_Lesson():
    math_user_inp=int(input("Pick from these options:\n 1:addition \n 2:subtraction \n 3:multiplication \n 4:division \n 5:modulus\n 6:exponential\n option: "))
    if math_user_inp == 1:
        print("\nAddition in python utilizes the + operator to  add")
        print("Ex:5+22=27")
        print("\nTry it yourself")
        while True:
            print("x+8=15")
            addition_input=int(input("pick the number that would add to 15 to see if it works: "))
            addition_equation= addition_input+8
            if addition_equation != 15:
                print("try again and make sure its a number that adds to 15")
            elif addition_equation == 15:
                print("\nWell done, you have succesfully understood how the addition operator is used!!")
                lesson_learned_option=int(input("\nPick from these options:\n 1:Learn more about the math operators,\n 2:go to the home page,\n 3:Exit the application"))
                if lesson_learned_option == 1:
                    Math_op_Lesson()
                elif lesson_learned_option == 2:
                    home_page()
                elif lesson_learned_option == 3:
                    sys.exit()
    
    elif math_user_inp == 2:
        print("\nSubtraction in python utilizes the - operator to subtract")
        print("Ex:13-5=8")
        print("\nTry it yourself")
        while True:
            print("21-x=9")
            subtraction_input=int(input("pick the number that would subtract from 21 to be 9 to see if it works: "))
            subtraction_equation= 21-subtraction_input
            if subtraction_equation != 9:
                print("try again and make sure its a number that subtracts to 9")
            elif subtraction_equation == 9:
                print("\nWell done, you have succesfully understood how the subtraction operator is used!!")
                lesson_learned_option=int(input("\nPick from these options:\n 1:Learn more about the math operators,\n 2:go to the home page,\n 3:Exit the application"))
                if lesson_learned_option == 1:
                    Math_op_Lesson()
                elif lesson_learned_option == 2:
                    home_page()
                elif lesson_learned_option == 3:
                    sys.exit()
        
    
    elif math_user_inp == 3:
        print("\nMultiplication in python utilizes the * operator to multiply")
        print("Ex:6*4=24")
        print("\nTry it yourself")
        while True:
            print("x*7=21")
            multiplication_input=int(input("pick the number that would multiply by 7 to be 21: "))
            multiplication_equation= multiplication_input * 7
            if multiplication_equation != 21:
                print("try again and make sure x is a number that multiplies to 21")
            elif multiplication_equation == 21:
                print("\nWell done, you have succesfully understood how the multiplication operator is used!!")
                lesson_learned_option=int(input("\nPick from these options:\n 1:Learn more about the math operators,\n 2:go to the home page,\n 3:Exit the application"))
                if lesson_learned_option == 1:
                    Math_op_Lesson()
                elif lesson_learned_option == 2:
                    home_page()
                elif lesson_learned_option == 3:
                    sys.exit()      

    elif math_user_inp == 4:
        print("\nDivision in python utilizes the / operator to divide")
        print("Ex:15/5=3")
        print("\nTry it yourself")
        while True:
            print("27/x=9")
            division_input=int(input("pick the number that would divide 27 by x into 9: "))
            division_equation= 27 / division_input 
            if division_equation != 3:
                print("try again and make sure its a number that the number multiplies to 21")
            elif division_equation == 3:
                print("\nWell done, you have succesfully understood how the division operator is used!!")
                lesson_learned_option=int(input("\nPick from these options:\n 1:Learn more about the math operators,\n 2:go to the home page,\n 3:Exit the application"))
                if lesson_learned_option == 1:
                    Math_op_Lesson()
                elif lesson_learned_option == 2:
                    home_page()
                elif lesson_learned_option == 3:
                    sys.exit()

    elif math_user_inp == 5:
        print("\nModulus in python utilizes the %" +  "to find the remainder")
        print("Ex:15%20=5")
        print("\nTry it yourself")
        while True:
            print("12%" + "x=2")
            modulus_input=int(input("pick the number that when divided by x will result in a remainder of 2: "))
            modulus_equation= 12 % modulus_input
            if modulus_equation != 2:
                print("try again and make sure x divides into 12 to get a remainder of 2")
            elif modulus_equation == 2:
                print("\nWell done, you have succesfully understood how the modulus operator is used!!")
                lesson_learned_option=int(input("\nPick from these options:\n 1:Learn more about the math operators,\n 2:go to the home page,\n 3:Exit the application"))
                if lesson_learned_option == 1:
                    Math_op_Lesson()
                elif lesson_learned_option == 2:
                    home_page()
                elif lesson_learned_option == 3:
                    sys.exit()          

    elif math_user_inp == 6:
        print("\nExponential in python utilizes the ** operator to raise the power")
        print("Ex:4**3=64")
        print("\nTry it yourself")
        while True:
            print("3**x=27")
            exponential_input=int(input("pick the number that when raised to the power of x will result in 27: "))
            exponential_equation= 12 % exponential_input
            if exponential_equation != 3:
                print("try again and make sure x can be raised to the power that will yield 27")
            elif exponential_equation == 3:
                print("\nWell done, you have succesfully understood how the exponential operator is used!!")
                lesson_learned_option=int(input("\nPick from these options:\n 1:Learn more about the math operators,\n 2:go to the home page,\n 3:Exit the application"))
                if lesson_learned_option == 1:
                    Math_op_Lesson()
                elif lesson_learned_option == 2:
                    home_page()
                elif lesson_learned_option == 3:
                    sys.exit()
"""




