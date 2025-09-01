from calculators.simple import calculate_simple_interest
from calculators.compound import calculate_compound_interest
from calculators.accrued import calculate_accrued_interest
from calculators.amortized import *
from calculators.daily import calculate_daily_interest
# import argparse



if __name__ == "__main__":
    try:
      
        print("Choose interest calculation type:")
        interest_options = {
            "1": {"name": "Simple Interest", "function": calculate_simple_interest},
            "2": {"name": "Compound Interest", "function": calculate_compound_interest}, 
            "3": {"name": "Amortized Interest", "function": calculate_amortized_payment}, 
            "4": {"name": "Accrued Interest", "function": calculate_accrued_interest},
            "5": {"name": "Daily Interest", "function": calculate_daily_interest},
        }
        for key, value in interest_options.items():
            print(f"{key}. {value['name']}")
        
        choice = input("Enter your choice ({}): ".format("/".join(interest_options.keys())))
        selected_option = interest_options.get(choice)
        if not selected_option or not selected_option["function"]:
            print("Invalid choice or function not implemented.")
            exit(1)
        selected_function = selected_option["function"]



        # parser = argparse.ArgumentParser(description="Calculate daily interest.")
       
       
        # parser.add_argument("--year_days", type=int, default=365, help="Days in year  (default: 365)")
        # parser.add_argument("--format", choices=["text", "json", "dict"], default="text", help="Output Format")
        
        # args = parser.parse_args()




        if choice == "1":
            print("Simple Interest")

            principal = float(input("Principal Amount: "))
            annual_rate = float(input("Annual Interest rate (e.g., 0.05 for 5%): "))
            years = int(input("Enter the number of years: "))
            simple_int = calculate_simple_interest(principal, annual_rate, years)
            print(f"Simple Interest: {simple_int}")
        elif choice == "2":
            print("Compound Interest")

            principal = float(input("Principal Amount: "))
            annual_rate = float(input("Annual Interest rate (e.g., 0.05 for 5%): "))
            years = int(input("Enter the number of years: "))
            n_periods = input("Number of compounding periods per year (default is 1): ")
            n_periods = int(n_periods) if n_periods.strip() else 1

            result = calculate_compound_interest(principal, annual_rate, years)
            print(f"Compound interest: {result}")
        elif choice == "3":
            # Amortized
            principal = float(input("Principal Amount: "))
            annual_rate = float(input("Annual Interest rate (e.g., 0.05 for 5%): "))
            years = int(input("Enter the number of years: "))
            payment = calculate_amortized_payment(principal, annual_rate, years)
            print(f"Monthly Payment: ${payment}")

            schedule = generate_amortization_schedule(principal, annual_rate, years)
            for entry in schedule[:5]:  # Show first 5 periods
                print(entry)
        elif choice == "4":
            print("Accrued Interest")
            principal = float(input("Principal Amount: "))
            annual_rate = float(input("Annual Interest rate (e.g., 0.05 for 5%): "))
            days_accrued = int(input("Number of days interest has accrued: "))
            year_basis_input = input("Select how interest is calculated: Actual (365) – Precise daily accrual or Bank (360) – Standardized for commercial finance (365 is default): ")
            year_basis = int(year_basis_input) if year_basis_input.strip() else 365
            accrued_int = calculate_accrued_interest(principal, annual_rate, days_accrued)
            print(f"Accrued Interst: {accrued_int}")
        elif choice == "5":
            print("Daily Interest")


            principal = float(input("Principal Amount: "))
            annual_rate = float(input("Annual Interest rate (e.g., 0.05 for 5%): "))
            days_accrued = int(input("Number of days interest has accrued: "))
            year_basis_input = input("Select how interest is calculated: Actual (365) – Precise daily accrual or Bank (360) – Standardized for commercial finance (365 is default): ")
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

    except KeyboardInterrupt:
        print("\nExited by User using Ctrl-C")

   
