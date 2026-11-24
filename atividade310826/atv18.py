minutes = int(input("Enter the minutes: "))
total = 1.15
adicional = 0.26
if minutes > 3:
    total = total + ((minutes - 3) * adicional)

print(f"The total to paid is: {total:.2f}")

