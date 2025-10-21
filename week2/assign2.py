def function1(name):
    # your code
    
    
    
    people: dict[str, tuple[int, int]]={
        "悟空": (0, 0),
        "辛巴": (-3, 3),
        "貝吉塔": (-4, -1),
        "特南克斯": (1, -2),
        "佛利沙": (4, -1),
        "丁滿": (-1, 4)
    }
    section1 = ["悟空", "辛巴", "貝吉塔", "特南克斯"]
    section2 = ["佛利沙", "丁滿"]

    distance: dict[str, int] = {}
    
    def area(name):
        if name in section1:
            return 1
        elif name in section2:
            return 2
    sec0 = area(name)
    extra_point = 2

    for n in people:
        if n == name:
            continue
        else:
            diff = abs(people[n][0] - people[name][0]) + abs(people[n][1] - people[name][1])
        if area(n) != sec0:
            diff = diff + extra_point
        distance[n] = diff

    value_max = max(distance.values())
    value_min = min(distance.values())
    max_key = []
    min_key = []
    for key, value in distance.items():
        if value == value_max:
            max_key.append(key)
    min_key = []
    for key, value in distance.items():
        if value == value_min:
            min_key.append(key)
    print("最遠", "、".join(max_key), ";最近", "、".join(min_key))

print("================Task1================")
function1("辛巴")
function1("悟空")
function1("佛利沙")
function1("特南克斯")





def func3(n):
    arr = []

    count1 = -2
    count2 = -3
    count3 = 1
    count4 = 2

    arr.append(25)
    for i in range(1, n+1):
        if i % 4 == 1:
            arr.append(arr[i-1] + count1)
        if i % 4 == 2:
            arr.append(arr[i-1] + count2)
        if i % 4 == 3:
            arr.append(arr[i-1] + count3)
        if i % 4 == 0:
            arr.append(arr[i-1] + count4)
    print(arr[n])

print("================Task3================")
func3(1)
func3(5)
func3(10)
func3(30)