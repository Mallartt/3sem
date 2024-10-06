from random import randint

def get_random(n,minn,maxx):
    l=[]
    for i in range(n):
        l.append(randint(minn,maxx))
    yield from l
if __name__ =='__main__':
    print(*get_random(5, 1, 3))
