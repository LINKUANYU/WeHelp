def function1(name):
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
    
    def find_section(name):
        if name in section1:
            return 1
        elif name in section2:
            return 2
    target_section = find_section(name)
    extra_point = 2

    for n in people:
        if n == name:
            continue
        else:
            diff = abs(people[n][0] - people[name][0]) + abs(people[n][1] - people[name][1])
        if find_section(n) != target_section:
            diff = diff + extra_point
        distance[n] = diff
        
    value_max = max(distance.values())
    value_min = min(distance.values())
    max_key = []
    min_key = []
    for key, value in distance.items():
        if value == value_max:
            max_key.append(key)
        if value == value_min:
            min_key.append(key)
    print("最遠", "、".join(max_key), ";最近", "、".join(min_key))


print("================Task1================")
function1("辛巴")
function1("悟空")
function1("佛利沙")
function1("特南克斯")