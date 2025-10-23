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



