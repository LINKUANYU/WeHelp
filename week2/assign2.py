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

def func2(ss, start, end, criteria):
    # divide each element in criteria,
    def divide(criteria):
        criteria = criteria.replace(" ", "")
        for op in ("<=", ">=", "="):
            if op in criteria:
                field, raw = criteria.split(op, 1)
                if field == "name":
                    if op != "=":
                        raise ValueError("name can only use '='")
                    return field, op, raw
                elif field == "r":
                    return field, op, float(raw)
                elif field == "c":
                    return field, op, int(raw)
                else:
                    raise ValueError("Error")

    field, op, val = divide(criteria)
    # select qualified service and put into candidates
    raw_candidates = []
    for s in ss:
        if op == "=":
            if s[field] == val:
                raw_candidates.append(s)
        elif op == "<=":
            if s[field] <= val:
                raw_candidates.append(s)
        elif op == ">=":
            if s[field] >= val:
                raw_candidates.append(s)
    # take the best option
    if len(raw_candidates) == 0:
        print("Error") 
        return

    from operator import itemgetter

    if op == "=":
        candidates = raw_candidates
    elif op == ">=":
        candidates = sorted(raw_candidates, key = itemgetter(field))
    elif op == "<=":
        candidates = sorted(raw_candidates, key = itemgetter(field), reverse = True)

    # make a schedule to record time for each service by list[dict{name, start, end}]
    def overlap(start, end, s):
        if (start < s["end"] and end > s["start"]):
            return True
        return False
    # take each candidate compare to each schedule
    # if candidate and schedule use the same service, check if overlap exsist
    # if overlap exsist change candidate continue(outer loop)
    # if not exsist keep going(inner loop) finish all schedules -> success print result and push
    # if finish all candidates (outer loop) -> failure print sorry

    for candidate in candidates:
        conflict = False
        for schedule in schedules:
            if candidate["name"] == schedule["name"]:
                if overlap(start, end, schedule):
                    conflict = True
                    break
        if conflict:
            continue
        print(candidate["name"])
        schedules.append({"name": candidate["name"], "start": start, "end": end})
        return
    print("Sorry")
    return
    
services = [
    {"name": "S1", "r": 4.5, "c":1000},
    {"name": "S2", "r": 3, "c": 1200},
    {"name": "S3", "r": 3.8, "c": 800}
]
schedules = []

print("================Task2================")
func2(services, 15, 17, "c>=800")
func2(services, 11, 13, "r<=4")
func2(services, 10, 12, "name=S3")
func2(services, 15, 18, "r>=4.5")
func2(services, 16, 18, "r>=4")
func2(services, 13, 17, "name=S1")
func2(services, 8, 9, "c<=1500")

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

