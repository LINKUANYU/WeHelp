def func4(sp, stat, n):
    
    
    # put passage in to car, the most fittest car (take differences and make new arr)
    new_sp = [None] * len(sp)
    
    for i in range(len(sp)):
        new_sp[i] = abs(sp[i] - n)
    
    # take out the unavalible car (give it big number)
    for i in range(len(stat)):
        if stat[i] == "1":
            new_sp[i] = 100
    # find the minimum number (most fittest)
    min = 1000
    for i in new_sp:
        if i < min:
            min = i
    # find the sequence of the car
    for n in range(len(new_sp)):
        if new_sp[n] == min:
            print(n)
            break
    
func4([3, 1, 5, 4, 3, 2], "101000", 2)
func4([1, 0, 5, 1, 3], "10100", 4)
func4([4, 6, 5,], "1000", 4)

