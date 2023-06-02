n=int(input())

def get_sequence(n):
    return (n + n **2)//2

form = lambda n: 2*get_sequence(n) + get_sequence(n-1)
while form(n) % 4 != 0:
    n +=1
print(n)