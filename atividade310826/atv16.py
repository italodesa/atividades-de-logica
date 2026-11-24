hour = float(input("Enter a hours: "))
minute = float(input("Enter a minutes: "))
second = float(input("Enter a seconds: "))

all_seconds = (hour * 3600) + (minute * 60) + second
print(f"The time in seconds is: {all_seconds}")