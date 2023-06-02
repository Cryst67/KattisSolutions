for _ in range(int(input())):
    s = input().split()
    noises = []
    while True:
        animal_sound = input()
        if animal_sound == 'what does the fox say?': break
        noises.append(animal_sound.split()[-1])
    for noise in noises:
        while s.count(noise) != 0:
            s.remove(noise)
    for sound in s:
        print(sound, end=' ')
    print()