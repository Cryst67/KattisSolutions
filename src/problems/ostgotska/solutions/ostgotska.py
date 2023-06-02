s = input().split()
w = 0
for word in s:
    if 'ae' in word:
        w += 1
print('dae ae ju traeligt va' if w/len(s) >= 0.4 else 'haer talar vi rikssvenska')

