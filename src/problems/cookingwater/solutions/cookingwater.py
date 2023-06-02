a, b = float('-inf'), float('inf')
n = int(input())
for i in range(n):
    obs_a, obs_b = map(int, input().split())
    if obs_a >= a and obs_a <= b:
        a = obs_a
    elif obs_a > b:
        print('edward is right')
        exit()
    if obs_b <= b and obs_b >= a:
        b = obs_b
    elif obs_b < a: 
        print('edward is right')
        exit()
print('gunilla has a point')
