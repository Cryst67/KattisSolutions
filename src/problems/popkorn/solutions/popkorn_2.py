n = int(input())
pop = 0
grps = 4
per_group = n/grps
pop += 4*((per_group - 1)*(per_group))/2 + 2 + 1 + 1
print(int(pop))