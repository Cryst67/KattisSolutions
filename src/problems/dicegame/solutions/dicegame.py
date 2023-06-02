gunnar = sum(list(map(int, input().split())))
emma = sum(list(map(int, input().split())))
if emma > gunnar:
    print("Emma")
elif emma < gunnar:
    print("Gunnar")
else:
    print("Tie")