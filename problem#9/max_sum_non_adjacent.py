def get_max_non_adjacent_sum(arr:[]):
    incl = arr[0]
    excl = 0
    n_excl = 0
    for i in range(1, len(arr)):
        n_excl = max(incl, excl)
        incl = excl + arr[i]
        excl = n_excl
    return max(incl, excl)

print(get_max_non_adjacent_sum([5, 1, 1, 5])) # 10
print(get_max_non_adjacent_sum([5, 5, 10, 100, 10, 5])) #110
print(get_max_non_adjacent_sum([6, 7, 1, 3, 8, 2, 4])) # 19 #House Robber Problem
print(get_max_non_adjacent_sum([5, 3, 4, 11, 2])) # 16 #House Robber Problem