def average(array):
    bota=set(array)
    return(round((sum(bota)/len(bota)),3))
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
