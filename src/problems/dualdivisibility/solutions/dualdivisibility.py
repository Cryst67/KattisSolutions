a,b = input().split()
l = len(a)
a = int(a)
b = int(b)
i=1
count=0
while 1:
    if len(str(int(a/i))) < l:break
    if a%i==0: 
        if a//i%b==0:count+=1
    i+=1
print(count)
        