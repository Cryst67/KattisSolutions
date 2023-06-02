s = input()
if s.count(':)') and s.count(':('):
    print('double agent')
elif s.count(':)'): print('alive')
elif s.count(':('): print('undead')
else: print('machine')