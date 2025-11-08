#3
import json


def fun(d):
    with open('data.txt','w') as f:
        f.write(str(d))
    f.close()
    with open('data.txt','r') as f:
        print(f.read())
        f.close()
d={
    "dvory":19,
    "michal": 12
}
fun(d)
