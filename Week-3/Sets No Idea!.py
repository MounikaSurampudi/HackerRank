if __name__ == "__main__":
    arr_len, sets_len = input().split(' ')
    arr = input().split(' ') # Array of elements
    A = input().split(' ') # A elements
    B = input().split(' ') # B elements

    AB = {k:1 for k in A} # cr8 & fill dict
    for k in B: # fill B
        AB[k]=-1
    happiness = 0
    for k in arr:
        try:
            happiness+=AB[k]
        except:
            pass
    print(happiness)
