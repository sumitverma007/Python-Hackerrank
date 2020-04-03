if __name__ == '__main__':
    n = int(input())
    arr1 = map(int, input().split())
    arr=list(arr1)
    arr.sort()
    max=arr[-1]
    
    for idx in range(0,len(arr)):
        if arr[idx]==max:
            break

    print(arr[idx-1])        
