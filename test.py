# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    li=[]
    lis=list(t)
    li.append(lis[0].lower())
    li.append(lis[1])
    return tuple(li)
L2 = sorted(L, key=by_name)
print(L2)