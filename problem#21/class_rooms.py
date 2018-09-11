def calculate(arr:[]):
    arr.sort()
    i = 1
    j = 0
    result = 1
    room = 1
    n = len(arr)

    while i < n and j < n:
        if arr[i][0] <= arr[j][1]:
            result+=1
            room = max(result,room)
            i+=1
        else:
            result-=1
            j+=1
    
    return result

arr = [(30, 75), (0, 50), (60, 150)]
print(calculate(arr)) #2 is the actual result
arr = [(900,910), (940,1200), (950,1120), (1100,1130), (1500,1900), (1800,2000)]
print(calculate(arr)) #3 is the actual result