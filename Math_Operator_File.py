def Match_op_Lesson():
    math_user_inp=input("Pick from these options: addition, subtraction, multiplication, division, modulus, exponentiation").lower()
    if math_user_inp == "addition":
        print("Addition in python utilizes the + operator to  add")
        print("Ex:5+22=27")
        print("Try it yourself")
        while True:
            print("x+8=15")
            addition_input=int(input("pick the number that would add to 15 to see if it works"))
            addition_equation= addition_input+8
            if addition_equation != 15:
                print("try again and make sure its a number that adds to 15")
            elif addition_equation == 15:
                print("Well done, you have succesfully understood how the addition operator is used!!")
                break
    
    elif math_user_inp == "subtraction":
        print("Subtraction in python utilizes the - operator to subtract")
        print("Ex:13-5=8")
        print("Try it yourself")
        while True:
            print("21-x=9")
            subtraction_input=int(input("pick the number that would subtract from 21 to be 9 to see if it works"))
            subtraction_equation= 21-subtraction_input
            if subtraction_equation != 12:
                print("try again and make sure its a number that subtracts to 9")
            elif subtraction_equation == 12:
                print("Well done, you have succesfully understood how the subtraction operator is used!!")
                break
    
    elif math_user_inp == "multiplication":
        print("Multiplication in python utilizes the * operator to multiply")
        print("Ex:6*4=24")
        print("Try it yourself")
        while True:
            print("x*7=21")
            subtraction_input=int(input("pick the number that would multiply by 7 to be 21"))
            subtraction_equation= subtract
            if subtraction_equation != 12:
                print("try again and make sure its a number that subtracts to 9")
            elif addition_equation == 12:
                print("Well done, you have succesfully understood how the subtraction operator is used!!")
                break        