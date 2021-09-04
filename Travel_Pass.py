# cook your dish here
def main():
    for _ in range(int(input())):
        n,a,b = map(int,input().split())
        s = input()
        x = s.count('0')
        print(a*x+b*(n-x))

if __name__ == '__main__':
    main()
