def reccur(n):
    if n<=2:
        return 1
    else:
        return reccur(n-1)+reccur(n-2)
for i in range(1,12):
   print(reccur(i))