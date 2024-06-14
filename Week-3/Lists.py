if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        command,*line = input().split()
        num = list(map(int,line))
        if command == 'insert':
            arr.insert(num[0],num[1])
        elif command == 'print':
            print(arr)
        elif command == 'remove':
            arr.remove(num[0])
        elif command == 'append':
            arr.append(num[0])
        elif command == 'sort':
            arr.sort()
        elif command == 'pop':
            arr.pop()
        elif command == 'reverse':
            arr.reverse()
