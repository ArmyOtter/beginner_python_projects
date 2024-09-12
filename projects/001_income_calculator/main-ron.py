# Edited Python code by Ron Deese
# 1. Create a function to calculate finances
import sys
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
    trys_allowed: int = 5
    salary_try_count: int = 0
    tax_try_count: int = 0
    while salary_try_count < trys_allowed:
        try:
            yearly_salary: float = float(input('Enter your annual salary: '))
            break # Exit the loop if no exception and less than the allowed trys.
        except:
            salary_try_count = salary_try_count + 1
            if salary_try_count < trys_allowed:
                print ("Not a valid input. Try again.")
            else:
                print ("You've exceeded the allowable amount of attempts.  Goodbye.") #Notify user and close program.
                sys.exit(1) #Close the program with an error code.
                
    while tax_try_count < trys_allowed:
        try:
            tax_rate: float = float(input('Enter your tax rate (%): '))
            break # Exit the loop if no exception and less than the allowed trys.
        except:
            tax_try_count = tax_try_count + 1
            if tax_try_count < trys_allowed:
                print ("Not a valid input. Try again.")
            else:
                print ("You've exceeded the allowable amount of attempts.  Goodbye.") #Notify user and close program.
                sys.exit(1) #Close the program with an error code.

    # 6. Call the function
    if salary_try_count < trys_allowed and tax_try_count < trys_allowed:
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
