waveform sorting

n=int(input())
arr=list(map(int,input().split()))
for i in range(n-1):
    if i%2==0 and arr[i]<arr[i+1]:
        arr[i],arr[i+1]=arr[i+1],arr[i]
    elif i%2==1 and arr[i]>arr[i+1]:
        arr[i],arr[i+1]=arr[i+1],arr[i]
for i in range(n):
    print(arr[i],end=' ')
            