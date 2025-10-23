# arr = [25, 23, 20, 21, 23, 21, 18, 19, 21, 19, 16, 17]
def func3(n):
    arr = [None] * (n + 1)

    count1 = -2
    count2 = -3
    count3 = 1
    count4 = 2

    arr[0] = 25
    for i in range(1, n+1):
        if i % 4 == 1:
            arr[i] = arr[i-1] + count1
        if i % 4 == 2:
            arr[i] = arr[i-1] + count2
        if i % 4 == 3:
            arr[i] = arr[i-1] + count3
        if i % 4 == 0:
            arr[i] = arr[i-1] + count4
    print(arr[n])
    
print("================Task3================")
func3(1)
func3(5)
func3(10)
func3(30)

