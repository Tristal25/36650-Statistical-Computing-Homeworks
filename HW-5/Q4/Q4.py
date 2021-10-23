def triangle(k):
    if abs(int(k)) != k:
        print("Invalid Input")
        return
    t, num = 1, 1
    while t <= k:
        for i in range(num, num + t, 1):
            print(i, end = " ")
        print("\r")
        t += 1
        num += (t-1)
