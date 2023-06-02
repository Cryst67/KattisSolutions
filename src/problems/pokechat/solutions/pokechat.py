str_code = input()
srl_code = input()
final = ''

for i in range(int(len(srl_code)/3)):
    char = srl_code[i*3:i*3+3]
    final += str_code[int(char)-1]

print(final)