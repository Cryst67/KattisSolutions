s = input()
if len(s) < 3:
    print('Imposter!')
    exit()
if s[len(s) - 3:len(s)] == 'eh?':
    print('Canadian!')
else:print('Imposter!')