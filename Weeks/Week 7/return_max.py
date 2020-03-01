def getmaxlist(input_list):
    return max(input_list)

print(getmaxlist([5, 6, 8]))

print(max([5,6,8]))




def getmax(n1, n2, n3):
    numberlist = []
    numberlist.append(n1)
    numberlist.append(n2)
    numberlist.append(n3)
    return max(numberlist)

def getmax2(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n3:
        return n2
    else:
        return n3

print(getmax(6,8,10))
