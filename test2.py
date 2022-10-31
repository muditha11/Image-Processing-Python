N = int(input())
x = list(map(int,input().split()))
a,b,c=x[0],x[1],x[2]
arr=[0 for i in range(N)]
for i in range(N):
    s = a+b+c
    a1 = (a * a + 2 * b + 1) % 10007 - 5000
    b1 = (b * b + 2 * a -1) % 10007 - 5000
    c1 = (a + b + c) % 121 - 60
    a=a1
    b=b1
    c=c1
    arr[i] = s
    print(s)

max_sum = 0
for j in range(N):
    sum = 0
    totsum=0
    for k in range(j,N):
        totsum += arr[k]
        if (totsum > sum):
            sum=totsum

    if (sum > max_sum):
        max_sum=sum

print(max_sum)



