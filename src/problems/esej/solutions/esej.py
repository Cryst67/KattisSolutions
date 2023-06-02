import random
import string
words = set()
a, b = map(int, input().split())
while len(words) <= max(a, b//2 + 1):
    words.add(''.join(random.choices(string.ascii_lowercase,k=random.randint(1,15))))
print(' '.join(list(words)[0:max(a, b//2)]))