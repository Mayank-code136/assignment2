
A = int(input("Enter a number: "))

if (A % 7 == 0) or (A % 10 == 5):
    print("The number is divisible by 7 OR has last digit 5.")
else:
    print("The number is NOT divisible by 7 and does not have last digit 5.")
