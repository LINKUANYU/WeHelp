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
    candidates = []
    for s in ss:
        if op == "=":
            if s[field] == val:
                candidates.append(s)
        elif op == "<=":
            if s[field] <= val:
                candidates.append(s)
        elif op == ">=":
            if s[field] >= val:
                candidates.append(s)
    # take the best option
    if len(candidates) == 0:
        print("Error") 
        return
    if op == "=":
        best = candidates[0]
    elif op == ">=":
        best = min(candidates, key = lambda s : s[field])
    elif op == "<=":
        best = max(candidates, key = lambda s : s[field])

    # make a schedule to record time for each service by list[dict{name, start, end}]
    def check_available(start, end, s):
        if (start < s["end"] and end > s["start"]):
            return False
        return True

    for s in schedules:
        # same service about to be used
        if s["name"] == best["name"]:
            if check_available(start, end, s) == False:
                print("Sorry")
                return
    print(best["name"])
    schedules.append({"name": best["name"], "start": start, "end": end})
    

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

