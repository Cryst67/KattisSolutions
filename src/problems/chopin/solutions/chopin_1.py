d = {
    'Ab': 'G#',
    'G#': 'Ab',
    'A#': 'Bb',
    'Bb': 'A#',
    'C#': 'Db',
    'Db': 'C#',
    'D#': 'Eb',
    'Eb': 'D#',
    'Gb': 'F#',
    'F#': 'Gb',
}

case = 1
while True:
    try: s = input()
    except EOFError: break
    if s[:2] in d: print(f'Case {case}:', d[s[:2]], s[3:])
    else: print(f'Case {case}: UNIQUE')
    case += 1