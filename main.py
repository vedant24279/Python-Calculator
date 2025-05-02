import art
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2
final_answer = 0
calculator = {"+":add,"-":sub,"*":mul,"/":div}
choice = "true"
while choice == "true":
    print(art.logo)
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

