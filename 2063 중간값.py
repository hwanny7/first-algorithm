N=int(input())
num=list(map(int, input().split()))

a=int(N / 2)
num.sort()

print(num[a])