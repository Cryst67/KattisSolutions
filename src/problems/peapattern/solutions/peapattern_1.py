n,m=input().split();s,i=str,1
while n!=m and i<101:n=''.join(f'{n.count(s(j))}{j}'for j in range(10)if n.count(s(j)));i+=1
print(i if n==m else'Does not appear')