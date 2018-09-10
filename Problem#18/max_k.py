def get_k_maxes(arr:[], k:int):
    queue = []
    for i in range(k):
        while len(queue) > 0 and arr[i] >= arr[queue[len(queue) - 1]]:
            del queue[len(queue) - 1]
        queue.append(i)
    for i in range(k, len(arr)):
        print(arr[queue[0]])
        if len(queue) >= k:
            del queue[0]
        while len(queue) > 0 and arr[i] >= arr[queue[len(queue) - 1]]:
            del queue[len(queue) - 1]
        queue.append(i)
    if len(queue) >= k:
            del queue[0]
    print(arr[queue[0]])

arr = [10, 5, 2, 7, 8, 7]
k = 3
get_k_maxes(arr, k)
print("#########")
arr = [12, 1, 78, 90, 57, 89, 56]
k = 3
get_k_maxes(arr, k)