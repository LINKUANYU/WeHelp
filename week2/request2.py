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
                if field == "r":
                    return field, op, float(raw)
                if field == "c":
                    return field, op, int(raw)

    field, op, val = divide(criteria)
    # select qualified service
    candidates = []
    for s in services:
        if op == "=":
            if s[field] == val:
                candidates.append(s)
        if op == "<=":
            if s[field] <= val:
                candidates.append(s)
        if op == ">=":
            if s[field] >= val:
                candidates.append(s)
    if op == "=":
        best = candidates[0]
    if op == ">=":
        best = min(candidates, key = lambda s : s[field])
    if op == "<=":
        best = max(candidates, key = lambda s : s[field])
    # make a schedule to record time for each service by list[dict{name, start, end}]
    # first data print out directly
    if len(schedule) == 0:
        print(best["name"])
        schedule.append({"name": best["name"], "start": start, "end": end})
    
    else:
        # build a function to check schedule
        def occupy(start, end):
            for s in schedule:
                if (start < s["end"] and start > s["start"]) or (end > s["start"] and end < s["end"]):
                    return True
        # check the new service if it's avalible in the schedule
        for s in schedule:
            if best["name"] == s["name"]:
                if occupy(start, end):
                    print("Sorry")
                    return
        print(best["name"])
        schedule.append({"name": best["name"], "start": start, "end": end})
                    
    


    

services = [
    {"name": "S1", "r": 4.5, "c":1000},
    {"name": "S2", "r": 3, "c": 1200},
    {"name": "S3", "r": 3.8, "c": 800}
]
schedule = []
func2(services, 15, 17, "c>=800")
func2(services, 11, 13, "r<=4")
func2(services, 10, 12, "name=S3")
func2(services, 15, 18, "r>=4.5")
func2(services, 16, 18, "r>=4")
func2(services, 13, 17, "name=S1")
func2(services, 8, 9, "c<=1500")

