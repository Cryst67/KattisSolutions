a= input()
b=input()

for i in range(len(a)):
    c=(ord(a[i]))-65
    d=(ord(b[i]))-65
    if (i%2==0):
            print((chr(((c-d)%26)+65)),end='')
    else:
       print(chr(((c+d)%26)+65),end='')