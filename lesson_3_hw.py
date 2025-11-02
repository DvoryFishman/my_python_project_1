#1

list =[1,2,3,4,3,4,5,6,7,3,6]
def func(list):
    my_set=set(list)
    avg=sum(list)/len(list)
    max1=max(list)
    min1=min(list)
    return {
        "set":my_set,
        "avg":avg,
        "max":max1,
        "min":min1
    }
print(func(list))
#2
