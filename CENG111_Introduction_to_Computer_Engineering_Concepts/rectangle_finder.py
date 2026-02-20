
def location(x, y, P):
    return P[y][x]

def possible_left_top_corners(P):
    result1 = []
    for y in range(len(P)):
        for x in range(len(P[0])):
            if location(x, y, P) == "1":
                if x + 1 < len(P[y]) and location(x + 1, y, P) == "1":
                    if y + 1 < len(P) and location(x, y + 1, P) == "1":
                        result1.append((x, y))
    return result1

def possible_right_bottom_corners(P):
    result2 = []
    for y in range(len(P)):
        for x in range(len(P[0])):
            if location(x, y, P) == "1":
                if (x - 1 >= 0 and location(x - 1, y, P) == "1") and (y - 1 >= 0 and location(x, y - 1, P) == "1"):
                    result2.append((x, y))
    return result2

def corner_combinations(pattern):
    result3 = []
    for i in possible_left_top_corners(pattern):
        for j in possible_right_bottom_corners(pattern):
            result3.append((i, j))
    return result3

def this_is_rectangle(top_left, bottom_right, P):
    x1 = top_left[0]
    y1 = top_left[1]
    x2 = bottom_right[0]
    y2 = bottom_right[1]
    
    if x1 >= x2 or y1 >= y2:
        return False
    
    for x in range(x1, x2 + 1):
        if location(x, y1, P) != "1" or location(x, y2, P) != "1":
            return False
   
    for y in range(y1, y2 + 1):
        if location(x1, y) != "1" or location(x2, y) != "1":
            return False

    for y in range(y1 + 1, y2):
        for x in range(x1 + 1, x2):
            if location(x, y) == "0":
                return True
    return False

def count_rectangles(pattern):    
    rectangles = 0
    for i in corner_combinations(pattern):
        a = i[0]
        b = i[1]
        if this_is_rectangle(a, b, pattern):
            rectangles += 1
    return rectangles
 

