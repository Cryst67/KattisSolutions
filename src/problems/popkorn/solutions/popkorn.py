n = int(input())
grps = 4
per_group = n//grps
pop_per_group = 2*(per_group)*(per_group-1)
pop = pop_per_group + 4
print(int(pop))