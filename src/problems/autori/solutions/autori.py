from functools import reduce
n = input()
fn = list(filter(lambda x: x.isupper(), n))
out = reduce(lambda x, y: x + y, fn)
print(out)