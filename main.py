import matplotlib.pyplot as plt

#Bonds selection
interest = 0
investment_duration = 0
valid_bond_types = ["OTS", "ROR", "DOR", "TOS", "COI", "EDO"]

bond_type = input("Enter a type of bond (OTS, ROR, DOR, TOS, COI, EDO): ")
while bond_type not in valid_bond_types:
    print("Please enter correct type of bond")
    bond_type = input("Enter a type of bond (OTS, ROR, DOR, TOS, COI, EDO): ")
    
if bond_type == "OTS":
        interest = 0.03
        investment_duration = 3
elif bond_type == "ROR":
        interest = 0.0575
        investment_duration = 12
elif bond_type == "DOR":
        interest = 0.0590
        investment_duration = 24
elif bond_type == "TOS":
        interest = 0.0595
        investment_duration = 36
elif bond_type == "COI":
        interest = 0.0630
        investment_duration = 48
elif bond_type == "EDO":
        interest = 0.0655
        investment_duration = 120

#Investment definition

month_quantity = int(input("Enter number of month for simulation: "))
while month_quantity <= 0:
    print("Month quantity must be more than zero.")
    month_quantity = int(input("Enter correct number of month for simulation: "))

monthly_payment = int(input("Enter monthly payment in zl: "))
while monthly_payment <= 0:
    print("Monthly payment must be more than zero.")
    monthly_payment = int(input("Enter monthly payment in zl: "))

print(f"Simulation time range is {month_quantity} months.")
print(f"Monthly payment is {monthly_payment} zl.")

balance = 0
total_invested_cash = 0
total_balance = 0

invested_capitals = []
months = []
total_balances = []
invested_cash = []

for month in range(1, month_quantity + 1):
    balance = balance + monthly_payment
    total_invested_cash = total_invested_cash + monthly_payment
    print(f"Current balance: {balance} for month: {month}")

    max_payment = balance - (balance % 100) if balance >= 100 else 0

    print(f"max payment is: {max_payment}")

    invested_capitals.append((month + investment_duration, max_payment))
    balance = balance - max_payment

    invested_capitals = [
        (ending_month, amount)
        for ending_month, amount in invested_capitals
        if not (month >= ending_month and (balance := balance + amount + (amount * interest)))
    ]

    total_balance = balance + sum(amount for _, amount in invested_capitals)
        
    months.append(month)
    total_balances.append(total_balance)
    invested_cash.append(total_invested_cash)

    print(f"Month {month}: ending balance = {balance:.2f}, investments = {invested_capitals}")
    print(f"Total balance is: {total_balance}")
    print("___________________________________________________________________________")

print(f"Final balance after {month_quantity} months: {total_balance:.2f} zl.")
print(f"Invested cash after {month_quantity} months: {total_invested_cash:.2f} zl.")
print(f"Profit {total_balance - total_invested_cash:.2f} zl.")

plt.figure(figsize=(10, 6))
plt.plot(months, total_balances, label='Total Balance', marker='o')
plt.plot(months, invested_cash, label='Invested Cash', marker='x')
plt.xlabel('Months')
plt.ylabel('Amount (zl)')
plt.title('Comparison of Total Balance and Invested Cash Over Time')
plt.legend()
plt.grid()
plt.show()