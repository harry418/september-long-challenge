# cook your dish here
def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        odd,even = [],[]
        for i in arr:
            if i%2==0:even.append(i)
            else:odd.append(i)
            
        res = 0
        for i in range(n):
            if i%2==0:
                if len(even)>0:
                    res+=(even.pop()+i+1)%2
                else: res+=(odd.pop()+i+1)%2
            else:
                if len(odd)>0:
                    res+=(odd.pop()+i+1)%2
                else: res+=(even.pop()+i+1)%2
        print(res)

if __name__ == '__main__':
    main()
