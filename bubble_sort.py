import random
from datetime import datetime

startTime = datetime.now()
my_num = []
for number in range(1,101):
    my_num.append(random.randint(1,10001))

def bubble_swap(arr):
    for num in range(len(arr) - 1,0,-1):
            for i in range(num):
                if arr[i] > arr[i + 1]:
                    arr[i],arr[i+1] = arr[i + 1],arr[i]

bubble_swap(my_num)


print my_num
print datetime.now() - startTime