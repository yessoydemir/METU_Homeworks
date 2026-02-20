info = eval(input())
annual = float(input())


def basetaxrate():
    x = info.get("INCOME")
    if x == "low":
        return 0.1 * annual
    elif x == "middle":
        return 0.2 * annual
    elif x == "high":
        return 0.3 * annual


def maritaldeduction():
    y = info.get("MARITAL_STATUS")
    childnumber = len(info.get("CHILD"))
    if y == "single":
        return 0
    elif y == "married":
        return 500 + (300 * childnumber)
    elif y == "single_parent":
        return 600 * childnumber


def dependentadjustments():
    specialneedsdeduction = 1000 if info.get("SPECIAL_NEEDS") else 0
    elderlycarededuction = 800 if info.get("ELDERLY_CARE") else 0
    under18 = len(list(filter(lambda age: age < 18, info.get("CHILD"))))
    u18deduction = 200 * under18
    return specialneedsdeduction + elderlycarededuction + u18deduction


def propertystatus():
    p = info.get("PROPERTY_STATUS")
    if p == "owns":
        return 0
    elif p == "rents":
        return 300


def residencebaseddeduction():
    c = info.get("CITY_CATEGORY")
    if c == "urban":
        return 0
    elif c == "suburban":
        return 200
    elif c == "rural":
        return 400


def additionaldeductions():
    sumadditionaldeductions = 0
    if info.get("EDUCATION", True):
        sumadditionaldeductions += 500
    if info.get("HEALTHCARE", True):
        sumadditionaldeductions += 750
    if info.get("GREEN_INITIATIVES", True):
        sumadditionaldeductions += 300
    return sumadditionaldeductions


deduction = maritaldeduction() + residencebaseddeduction() + additionaldeductions() + dependentadjustments() + propertystatus()
rawfinal_tax_amount = basetaxrate() - deduction


def greaterzero(rawfinal_tax_amount):
    return max(rawfinal_tax_amount, 0)


def durationbaseddeduction(rawfinal_tax_amount):
    duration = info.get("TAXPAYER_DURATION")
    if duration == "new":
        return 1 * rawfinal_tax_amount
    elif duration == "regular":
        return (95 * rawfinal_tax_amount) / 100
    elif duration == "long_term":
        return (90 * rawfinal_tax_amount) / 100


final_tax_amount = durationbaseddeduction(greaterzero(rawfinal_tax_amount))

print("%.2f" % final_tax_amount)
    
    
    
        
    

        


 