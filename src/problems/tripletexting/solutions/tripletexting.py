from collections import Counter
print(((lambda w,l: Counter((w[0:l],w[l:l<<1],w[l<<1:])))(*(lambda i: (i,len(i)//3))(input()))).most_common(1)[0][0])