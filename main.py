try:
    import os
    
    # A simple calculator
    print("Welcome to Calculator")
    def main():
        while True:
            choice = input("Press \n 1 to Add \n 2 to Sub \n 3 to Multiple \n 4 to divide \n :")
            num1 = input("Enter first no : ")
            num2 = input("Enter second no : ")
            operators = ['+','-','*','/']
            operate(operators[choice-1],num1,num2)
            loop_check = input("Press 1 to Try Again : ")
            os.system('cls')
    
    def operate(operator,first,second):
        string = f"global var1; var1 = {first}{operator}{second}"
        exec(string)
        print(var1)
    
    main()
except:
    print("Error, try again\n")
    main()
