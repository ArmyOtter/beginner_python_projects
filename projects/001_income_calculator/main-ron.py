# Edited Python code by Ron Deese
# 1. Create a function to calculate finances
import sys
def calculate_finances(monthly_income: float, tax_rate: float, currency: str) -> None:
    # 2. Do the math for each field
    yearly_salary: float = monthly_income * 12
    monthly_tax: float = monthly_income * (tax_rate / 100)
    yearly_tax: float = monthly_tax * 12
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_net_income: float = yearly_salary - yearly_tax

def calculate_finances_yearly(yearly_salary: float, tax_rate: float, currency: str) -> None:
    # 2. Do the math for each field
    monthly_income: float = yearly_salary / 12
    monthly_tax: float = monthly_income * (tax_rate / 100)
    yearly_tax: float = monthly_tax * 12
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_net_income: float = yearly_salary - yearly_tax

    # 3. Format the information nicely for the user
    print('--------------------------------')
    print(f'Monthly income: {currency}{monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Yearly salary: {currency}{yearly_salary:,.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax:,.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income:,.2f}')
    print('--------------------------------')

    # 4. Create a main entry point for the program
def main() -> None:
    # 5. Gather user input
    #monthly_income: float = float(input('Enter your monthly income: '))
    Trys_Allowed: int = 5
    Salary_Try_Count: int = 0
    Tax_Try_Count: int = 0
    while Salary_Try_Count < Trys_Allowed:
        try:
            yearly_salary: float = float(input('Enter your annual salary: '))
            break # Exit the loop if no exception and less than the allowed trys.
        except:
            Salary_Try_Count = Salary_Try_Count + 1
            if Salary_Try_Count < Trys_Allowed:
                print ("Not a valid input. Try again.")
            else:
                print ("You're an idiot!") #This dummy has entered too many invalid responses.
                sys.exit(1) #Close the program with an error code.
                
    while Tax_Try_Count < Trys_Allowed:     
        try:
            tax_rate: float = float(input('Enter your tax rate (%): '))
            break # Exit the loop if no exception and less than the allowed trys.
        except:
            Tax_Try_Count = Tax_Try_Count + 1
            if Tax_Try_Count < Trys_Allowed:
                print ("Not a valid input. Try again.")
            else:
                print ("You're an idiot!") #This dummy has entered too many invalid responses.
                sys.exit(1) #Close the program with an error code.

    # 6. Call the function
    ##calculate_finances(monthly_income, tax_rate, currency='$')
    if Salary_Try_Count < Trys_Allowed and Tax_Try_Count < Trys_Allowed:
        calculate_finances_yearly(yearly_salary, tax_rate, currency='$')

# 7. Run the script
if __name__ == "__main__":
    main()

"""
Homework:
1. Edit the script so that users can also enter their expenses (eg. rent, food, gym memberships) so they
can see how much they have left over each month.
2. Recreate the user input section to safely handle users inserting the wrong type without 
crashing the program.

"""
