import numpy as np

arr = np.array([[1,2,4],[3,4,6],[5,6,7]])
for row in arr:
    print(row)

for row in arr.flat:
    print(row)

a=np.arange(6).reshape(3,2)
b=np.arange(6,12).reshape(3,2)

print(np.vstack((a,b)))

print(np.hstack((a,b)))

x=np.arange(30).reshape(2,15)

result = np.hsplit(x,3)

print("First array:",result[0],"\nSecond array:", result[1],"\nThird array:", result[2])

a=np.arange(12).reshape(3,4)

b = a > 4

print(a[b])