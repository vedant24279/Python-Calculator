logo = r"""
 _____________________
|  _________________  |
| | PythonCalc   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


#ADDITION 
def add(n1, n2):
    return n1 + n2

#SUBTRACTION
def sub(n1, n2):
    return n1 - n2

#MULTIPLICATION
def mul(n1, n2):
    return n1 * n2

#DIVISION
def div(n1, n2):
    return n1 / n2
final_answer = 0
calculator = {"+":add,"-":sub,"*":mul,"/":div}
choice = "true"
while choice == "true":
    print(logo)
    first_letter = int(input("Enter the first number : "))
    operation = str(input('''which operation do you want to perform?
    "+" "-" "*" "/"
    choice : '''))
    last_letter = int(input("Enter the second number : "))
    final_answer = calculator[operation](n1=first_letter,n2=last_letter)
    print(f"{first_letter} {operation} {last_letter} = {final_answer}")
    continuee_or_not = str(input(f"Type 'Y' to continue calculation with {final_answer} or Type 'N' to start new calculation or Type 'C' to close the calculator. :")).lower()
    while continuee_or_not == "y":
        first_letter = final_answer
        operation = str(input('''which operation do you want to perform?
            "+" "-" "*" "/"
            choice : '''))
        last_letter = int(input("Enter the second number : "))
        final_answer = calculator[operation](n1=first_letter, n2=last_letter)
        print(f"{first_letter} {operation} {last_letter} = {final_answer}")
        continuee_or_not = str(input(f"Type 'Y' to continue calculation with {final_answer} or Type 'N' to start new calculation or Type 'C' to close the calculator. :")).lower()
    if continuee_or_not == "c":
        choice = "false"
        break
    while continuee_or_not == "n":
        choice = "true"
        break

