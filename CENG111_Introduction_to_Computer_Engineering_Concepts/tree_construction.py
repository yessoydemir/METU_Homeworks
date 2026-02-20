def findroot(list):
    root = list[0]
    minx = root.count("x")
    for i in list:
        currentx = i.count("x")
        if currentx < minx:
            root = i
            minx = currentx
    return root

def possiblechildrens(string):
    childrenscandidate = []
    for j in range(len(string)): 
        if string[j] == "o": 
            childrenscandidate.append(string[:j] + "x" + string[j+1:])
    return childrenscandidate

def IsInList(string, list): 
    realchildren = []  
    for i in list: 
        for j in possiblechildrens(string): 
            if i == j and j not in realchildren: 
                realchildren.append(j) 
    return realchildren 

def treestructure(string, list):
    realchildren = IsInList(string, list)  
    y = list.index(string)
    list.pop(y)
    if len(realchildren)==0:  
        return string 
    else: 
        result = []
        for i in realchildren:
            result.append(treestructure(i, list))  
        return [string] + result 

def OX_to_tree(list): 
    root = findroot(list)
    return treestructure(root,list)














