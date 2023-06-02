import random
import string

def is_valid(s):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    count_vowels = 0
    count_consonants = 0

    for c in s:
        if c in vowels:
            count_vowels += 1
            count_consonants = 0
        elif c in consonants:
            count_consonants += 1
            count_vowels = 0

        if count_vowels == 3 or count_consonants == 3:
            return False

    return True

def generate_unique_strings(n):
    unique_strings = set()

    while len(unique_strings) < n:
        length = random.randint(3, 20)
        s = "".join(random.choices(string.ascii_letters.lower(), k=length))

        if is_valid(s):
            unique_strings.add(s)

    return unique_strings

strings = generate_unique_strings(int(input()))
for name in strings: print(name)
