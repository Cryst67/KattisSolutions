def main():
    line = input().split()
    tree_height = int(line[0])
    root = 2**(tree_height + 1) - 1
    try: commands = line[1]
    except IndexError:
        print(root)
        return
    start = 0
    for command in commands:
        if command == 'L':
            start = 2 * start + 1
        else: start = 2 * start + 2
    print(root - start)
    
if __name__ == '__main__':
    main()