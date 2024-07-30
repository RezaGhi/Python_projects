import time
import random


def naive_search(li,target):
    for i in range(len(li)):
        if li[i]==target:
            return i
    return -1

def binary_search(li,target,low=None,high=None):
    if low==None:
        low=0
    if high==None:
        high=len(li)-1
    if high<low:
        return -1
    
    midpoint= (low+high) // 2

    if li[midpoint]==target:
        return midpoint
    elif target<li[midpoint]:
        return binary_search(li , target,low,midpoint-1)
    else:
        return binary_search(li,target,midpoint+1,high)

li=[1,3,6,7,8,10,11,12,15]
target=10
print(naive_search(li,target))
print(binary_search(li,target))


length=100000
source=set()
for i in range(length):
    source.add(random.randint(-2*length,2*length))
source = sorted(list(source))

start=time.time()
for target in source:
    naive_search(source,target)
end=time.time()
print(f'for naive search spend {end-start} s/iteration.')


start1=time.time()
for target in source:
    binary_search(source,target)
end1=time.time()

print(f'for binary search spend {end1-start1} s.')
