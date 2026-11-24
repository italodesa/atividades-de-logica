days = int(input("Enter a days worked: "))
money_day = 20.00
tax = 0.08
total = days * money_day

salary = (total - total * tax)
print(f"The salary liquid is: {salary:.2f}")