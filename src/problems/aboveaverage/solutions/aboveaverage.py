for i in range(int(input())):
    grades = list(map(int, input().split()))[1:]
    avg = sum(grades)/len(grades)
    above_avg = len(list(filter(lambda x: x > avg, grades)))
    print(f'{(100*above_avg/len(grades)):.3f}%')