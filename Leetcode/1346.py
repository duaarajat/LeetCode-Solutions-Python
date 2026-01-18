"""Check If N and Its Double Exist
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
"""
"""arr=[3,14,1,8,7]

s = set()
for i in arr:
    if i*2 in s or i*0.5 in s:
        print(True)
    s.add(i)
    print(False)"""

arr=[6,1,3,19,65,9]
a=arr[0]
for i in arr:
    if i>a:
        a=i
print(a)