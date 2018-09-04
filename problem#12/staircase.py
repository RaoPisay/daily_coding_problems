def count_ways(to:int, steps:[]):
    table = [0]*(to+1)
    table[0] = 1
    for i in range(1, to+1):
        for e in steps:
            if i - e > -1:
                table[i]+=table[i-e]
            else:#Assuming steps are in ascending order, if not either remove this or sort the steps in ascending order to keep as it is
                break
    return table[to]

ways = count_ways(5, [1,3,5])
print(ways)