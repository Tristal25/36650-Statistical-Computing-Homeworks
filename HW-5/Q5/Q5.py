def pyramid(n):
    if abs(int(n)) != n:
        print("Invalid Input")
        return
    l = n - 1
    for i in range(0,n):
        for j in range(0,l):
            print(" ", end = "")
        l -= 1
        for k in range(0,i+1):
            print("*", end = " ")
        print("\r")


pyramid(3)
pyramid(5)
pyramid(-1)
pyramid(1.5)
