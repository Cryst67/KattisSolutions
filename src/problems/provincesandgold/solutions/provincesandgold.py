from functools import reduce
v=[['Province','Duchy','Estate'],[8, 5, 2]];t = [['Gold', 6, 3],['Silver', 3, 2],['Copper', 0, 1]]
k = reduce(lambda x,y:x+y,[t[i][2]*x for i,x in enumerate(list(map(lambda x: int(x),list(input().split(' ')))))],0);b = list(filter(lambda x: x - k <= 0, v[1]));q = list(filter(lambda x:x[1]-k<= 0,t))
f=[]
f.append(v[0][v[1].index(max(b))]) if len(b)>0 else None;f.append(q[0][0]) if len(q)>0 else None;print(f"{f[0]} or {f[1]}") if len(f)>1 else print(f[0])