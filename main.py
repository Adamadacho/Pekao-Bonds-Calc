import matplotlib.pyplot as plt

month_quantity = int(input("Enter number of month for simulation: "))
monthly_payment = int(input("Enter monthly payment in zl: "))

print(f"Simulation time range is {month_quantity} months.")
print(f"Monthly payment is {monthly_payment} zl.")

#Bonds parameters
interest = 0.03
investment_duration = 3

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