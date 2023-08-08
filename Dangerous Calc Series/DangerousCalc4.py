import os
import pickle

print('''
        Okay, but we can make this quicker
        for multiple work calculations.
        and more secure so only authenticated
        users can run this script
        press 1 and type the calculation
        you want to work out , press enter
        and type the next one.
        To end the loop and go back to the
        selection menu, type ! and press enter.
        Choose option 2 to get the results from
        each calculation.
        ''')

def CalcListBuilder():
    calculations = {}
    currentCalc = int(input("Enter your calculation: "))
    while currentCalc != '!':
        calculations.append(currentCalc, '\n')
        currentCalc = int(input("Enter your calculation: "))
    else:
        print("Calculation list complete.")
        with open('calculations.pkl', 'wb') as file:
                pickle.dump(calculations, file)
    getChoice()

def RunCalcs():
    # Open and Use Exec() or Eval() to print the results of each calculation on each line in the calculations.pk1 file
    with open('calculations.pkl', 'rb') as file:
        calculations = pickle.load(file)
        for calculation in calculations:
            print(f"Calculating {calculation}...")
            print(calculation, "=", exec(calculation))
    print("Calculation results complete.")
    getChoice()
    
                
def LeaveMessage():
    print("Leave a message for the admin.")
    message = input("Message: ")
    with open('message.pkl', 'wb') as file:
        pickle.dump(message, file)
    print("Message saved.")


def choicePicker(choice):
        if choice == 1:
            CalcListBuilder()
            getChoice()
        
        if choice == 2:
            RunCalcs()
            getChoice()
                
        if choice == 3:
            LeaveMessage()
            getChoice()
        
        if choice == 4:
            exit()
        
        else:
            print("That's not a valid choice, try again.")
            getChoice()

def getChoice():
        choice = int(input("1. Enter Calculations, 2. Get Results, 3. Leave Message, 4. Exit >"))
        choicePicker(choice)

getChoice()