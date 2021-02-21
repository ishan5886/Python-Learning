num = int(input("Number : "))
factorial = 1

if num < 0:
    print("Negative Number -  No factorial")
elif num == 0:
    print("Factorial = 1")
else:
    for i in range(1, num + 1):  # (num+1) because last value in for loop range not included
        factorial = factorial * i

        print(factorial)
