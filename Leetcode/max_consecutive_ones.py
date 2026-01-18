arr=[1,0,1,1,0,1,1,1,1]
count=0
s=0
for i in arr:
    if i==0:
        count=0
    if i==1:
        count=count+1
        if count>s:
            s=count
print(s) 