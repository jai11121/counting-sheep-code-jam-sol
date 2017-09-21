import collections
print("enter no.")
n=int(input())
c={}
x=0
for i in range(1,100):
    c.update(collections.Counter(str(i*n)))
    for j in range(10):
        if str(j) in list(c.keys()):
            x+=1
    if x==10:
        print((i)*n)
        break
    else:
        x=0






