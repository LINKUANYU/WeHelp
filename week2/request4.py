def func4(sp, stat, n):
    # for loop put passage into car(difference), if meet car unavailable continue
    # renew the min and record the ans each loop
    # finish loop print result
    import math
    if len(sp) != len(stat):
        print("Error")
        return
    
    min = math.inf
    ans = -1
    for i in range(len(sp)):
        if stat[i] == "1":
            continue
        diff = abs(sp[i] - n)
        if diff < min:
            min = diff
            ans = i
    if ans == -1:
        print("Not Found")
        return
    print(ans)


print("================Task4================")
func4([3, 1, 5, 4, 3, 2], "101000", 2)
func4([1, 0, 5, 1, 3], "10100", 4)
func4([4, 6, 5, 8], "1000", 4)

