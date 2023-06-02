n = int(input())
pop = 0
grps = 4
per_group = int(n/grps)
pop += 2*((per_group - 1)*(per_group)) + 2 + 1 + 1
print(int(pop))