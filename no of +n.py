
    N = int(input("Enter a positive integer: "))
    if N <= 0:
        print(" Enter a positive integer.")
    else:
        digit = 0
        while N > 0:
            N = N // 10
            digit = digit + 1
        print("Number of digits:", digit)

   