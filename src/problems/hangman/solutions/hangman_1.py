lives = 10
game = input()
guess = input()
game_len = len(game)
i = 0
while lives > 0 and game_len > 0:
    letter = guess[i]
    letter_count = game.count(letter)
    if letter_count == 0:
        lives -= 1
    else:
        game_len -= letter_count
    i += 1

if lives > 0:
    print('WIN')
    exit()
print('LOSE')