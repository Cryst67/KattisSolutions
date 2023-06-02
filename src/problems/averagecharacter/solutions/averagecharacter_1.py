s = input()
a = 0
for letter in s:
    a+=ord(letter)
print(chr(int(a/len(s))))