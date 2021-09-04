# cook your dish here
def main():
    for _ in range(int(input())):
        n,x = map(int,input().split())
        arr = list(map(int,input().split()))
        
        d1,d2 = {},{}
        for i in arr:
            d1[i] = d1.get(i,0)+1 # current element counter
            d2[i] = 1 # if element present or not
        
        # base case: if only one element in array
        if n==1: 
            print(1,0)
            continue
        
        ans,step = 0,0
        
        for i in d1:
            # if all element are equals
            if d1[i]==n:
                ans = n
                break
            # if freq of element is greater than ans
            if d1[i]>ans:
                ans = d1[i]
        # base case: if x==0 then print ans and step
        if x==0:
            print(ans,step)
            continue
        
        for i in d2:
            t = i^x # xor with element
            if d2.get(t,0) == 1: # if t is present in array
                if d1[i]+d1[t]>ans: # if freq is greater than ans
                    ans = d1[t]+d1[i] # update ans
                    step = min(d1[i],d1[t]) # update changes
                elif d1[i]+d1[t]==ans: # if freq na and ans both same 
                # update steps with minimum steps
                    step = min(step,d1[i],d1[t])
        print(ans,step)

if __name__ =='__main__':
    main()
