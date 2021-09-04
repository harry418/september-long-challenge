# cook your dish here
def main():
    for _ in range(int(input())):
        a,b,c,d,e = map(int,input().split())
        mini = float('-inf')
        for i in a,b,c:
            if mini<i and i<= e:
                mini = i
        if mini<=e and a+b+c-mini<=d:
            print('YES')
        else:
            print('NO')

if __name__ == "__main__":
    main()
