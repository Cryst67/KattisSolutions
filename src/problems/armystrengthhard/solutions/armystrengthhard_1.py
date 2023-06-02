for i in range(int(input())):
    input()
    ng, nm = map(int, input().split())
    godzilla = max([*map(int, input().split())])
    mech_godzilla = max([*map(int, input().split())])
    if godzilla >= mech_godzilla:
        print('Godzilla')
    else:
        print('MechaGodzilla')