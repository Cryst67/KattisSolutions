while True:
 try:
  s=int(input())
  if s ==0:print(0)
  if s== 1:print(1)
  else:print(s*2-2)
 except EOFError:
  break
    