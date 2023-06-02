def popular_vote():
    candidates = int(input())
    d = {}
    winner = -1
    winner_count = float('-inf')
    vote_count = 0
    majority = 0
    for i in range(candidates):
        votes = int(input())
        d[i + 1] = votes
        if votes > winner_count:
            winner = i + 1
            winner_count = votes
        vote_count += votes
    for key in d:
        if key == winner: continue
        if d[key] == winner_count: winner = -1
    if winner != -1 and winner_count > vote_count//2:
        majority = 1
    return winner, majority

def main():
    for i in range(int(input())):
        winner, majority = popular_vote()
        if winner == -1: print('no winner')
        else: print("majority" if majority else "minority", f"winner {winner}")

if __name__ == "__main__":
    main()