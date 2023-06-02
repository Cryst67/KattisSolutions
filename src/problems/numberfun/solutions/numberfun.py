for i in [0]*int(input()):
 a,b,c = map(int, input().split())
 print('Possible' if a+b==c or abs(b-a)==c or a*b==c or a/b==c or b/a == c else 'Impossible')