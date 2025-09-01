from calculators.simple import calculate_simple_interest
from calculators.compound import calculate_compound_interest
from calculators.accrued import calculate_accrued_interest
from calculators.amortized import *
from calculators.daily import calculate_daily_interest
from calculators.tax_adjusted import *
from calculators.effective_rate import calculate_effective_rate
import os
import sys


if __name__ == "__main__":
    '''
    This is the functional tester for the library
    '''
    try:
      
        print("Choose interest calculation type:")
        interest_options = {
            "1": {"name": "Simple Interest", "function": calculate_simple_interest},
            "2": {"name": "Compound Interest", "function": calculate_compound_interest}, 
            "3": {"name": "Amortized Interest", "function": calculate_amortized_payment}, 
            "4": {"name": "Accrued Interest", "function": calculate_accrued_interest},
            "5": {"name": "Daily Interest", "function": calculate_daily_interest},
            "6": {"name": "Tax-Adjusted Interest", "function":calculate_tax_adjusted_income},
            "7": {"name": "Real After Tax Interest", "function": calculate_real_after_tax_interest},
            "8": {"name": "Effective Rate", "function": calculate_effective_rate},
            "10":{"name": "Exit Application","function":None}
        }
        for key, value in interest_options.items():
            print(f"{key}. {value['name']}")
        
        choice = input("Enter your choice ({}): ".format("/".join(interest_options.keys())))
        selected_option = interest_options.get(choice)
        if not selected_option or not selected_option["function"]:
            print("You have entered an invalid selection")
            print("Returning to main menu...\n")
            # Restart the main menu loop
            os.execl(sys.executable, sys.executable, *sys.argv)
           
        selected_function = selected_option["function"]


        if choice == "1":
            print("\nSimple Interest")

            principal = float(input("Please enter the Principal Amount: "))
            annual_rate = float(input("Please enter the Annual Interest rate (e.g., 0.05 for 5%): "))
            years = int(input("Please enter the Enter the number of years: "))
            simple_int = calculate_simple_interest(principal, annual_rate, years)
            print(f"Simple Interest: {simple_int}")
        elif choice == "2":
            print("\nCompound Interest")

            principal = float(input("Please enter the Principal Amount: "))
            annual_rate = float(input("Please enter the Annual Interest rate (e.g., 0.05 for 5%): "))
            years = int(input("Please enter the umber of years: "))
            n_periods = input("Please enter the Number of compounding periods per year (default is 1): ")
            n_periods = int(n_periods) if n_periods.strip() else 1

            result = calculate_compound_interest(principal, annual_rate, years)
            print(f"\nCompound interest: {result}")
        elif choice == "3":
            # Amortized
            principal = float(input("Please enter the Principal Amount: "))
            annual_rate = float(input("Please enter the Annual Interest rate (e.g., 0.05 for 5%): "))
            years = int(input("Please enter the number of years: "))
            payment = calculate_amortized_payment(principal, annual_rate, years)
            print(f"Monthly Payment: ${payment}")

            schedule = generate_amortization_schedule(principal, annual_rate, years)
            for entry in schedule[:5]:  # Show first 5 periods
                print(entry)
        elif choice == "4":
            print("\nAccrued Interest")
            principal = float(input("Please enter the Principal Amount: "))
            annual_rate = float(input("Please enter the Annual Interest rate (e.g., 0.05 for 5%): "))
            days_accrued = int(input("Please enter the Number of days interest has accrued: "))
            year_basis_input = input("Please enter the Select how interest is calculated: Actual (365) – Precise daily accrual or Bank (360) – Standardized for commercial finance (365 is default): ")
            year_basis = int(year_basis_input) if year_basis_input.strip() else 365
            accrued_int = calculate_accrued_interest(principal, annual_rate, days_accrued)
            print(f"Accrued Interst: {accrued_int}")
        elif choice == "5":
            print("\nDaily Interest")


            principal = float(input("Please enter the Principal Amount: "))
            annual_rate = float(input("Please enter the Annual Interest rate (e.g., 0.05 for 5%): "))
            days_accrued = int(input("Please enter the Number of days interest has accrued: "))
            year_basis_input = input("Please enter the Select how interest is calculated: Actual (365) – Precise daily accrual or Bank (360) – Standardized for commercial finance (365 is default): ")
            year_basis = int(year_basis_input) if year_basis_input.strip() else 365
            format = input("choices are json/dict/text (default is text): ")
            result = calculate_daily_interest(
                principal,
                annual_rate,
                days_accrued,
                year_basis,
                format
            )
            print(result)
        elif choice == "6":
            print("\nTax-Adjusted Interest")
            income = float(input("Please enter you interest income: "))
            taxable_rate = float(input("Please enter your tax rate: "))
            result = calculate_tax_adjusted_income(income, taxable_rate)
            print(f"Taxable Rate: ${round(result,2)}")

        elif choice == "7":
            print("\nReal After Tax Interest")
            nominal = float(input("Please enter the nominal interest rate: "))
            tax = float(input("Please enter the tax rate: "))
            inflation = float(input("Please enter the inflation rate: "))
            result = calculate_real_after_tax_interest(nominal, tax, inflation)
            print(f"\nThe real after tax interest is: {result:.4f}")

        elif choice == "8":
            print("\nEffective Rate")
            nominal = float(input("Please enter the nominal interest rate: "))
            n_periods = input("Please enter the Number of compounding periods per year (default is 1): ")
            n_periods = int(n_periods) if n_periods.strip() else 1
            result = calculate_effective_rate(nominal,n_periods)
            print(f"Effective Rate: {round(result * 100, 2)}%")

        else:
            print("Exiting by user choice.")
            exit(1)

    except KeyboardInterrupt:
        print("\nExited by User using Ctrl-C")

   
