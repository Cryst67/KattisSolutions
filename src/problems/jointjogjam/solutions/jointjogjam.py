from math import dist
a,b,c,d,e,f,g,h=map(int,input().split())
print(max(dist([a,b],[c,d]),dist([e,f],[g,h])))