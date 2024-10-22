if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max1 = -float('inf')  
    max2 = -float('inf')  
    for num in arr:
        if num > max1:
            max2 = max1  
            max1 = num   
        elif num > max2 and num != max1:
            max2 = num   
    print(max2)