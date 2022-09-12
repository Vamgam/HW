def dynamic(n):
    a=[0,0]
    a[0]=1
    a[1]=1
    if n<=2:
        print(a[n-1])
        return
    for i in range(n-2):
        a[0],a[1]=a[1],(a[0]+a[1])
    print(a[1])
for i in range(1,12):
   dynamic(i)
def reccur(n):
    if n<=2:
        return 1
    else:
        return reccur(n-1)+reccur(n-2)
for i in range(1,12):
   print(reccur(i))