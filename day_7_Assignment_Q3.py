list1=[(1,2,3),[1,2],['a','hit','less']]
list2=[]
for i in list1: 
    if type(i)==type(list1): 
        list2=list2+i
    elif type(i)==tuple:
        list2.extend(i)
    else: 
        list2.append(i)

print(list2)