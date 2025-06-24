def split_bill(total_amount, num_people):
    if num_people == 0:
        return "Number of people cannot be zero."
    return round(total_amount / num_people, 2)

# Read input
total = float(input("Enter the total bill amount: "))
people = int(input("Enter the number of people: "))

# Calculate and display result
amount_each = split_bill(total, people)
print(f"Each person should pay: {amount_each}")
