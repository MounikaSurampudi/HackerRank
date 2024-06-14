if __name__=="__main__":
    for i in range(int(input())):
        _,a,_,b=input(),set(map(int,input().split())),input(),set(map(int,input().split()))
        if(a.intersection(b)==a):
            print(True)
        else:
            print(False)
