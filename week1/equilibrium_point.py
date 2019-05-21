def findEquilibriumPoint(arr,n):
    sum = 0
    leftSum = 0
    for i in range(n):
        sum = sum + arr[i]
    for i in range(n):
        sum = sum - arr[i]
        if (sum == leftSum):
            return i
        leftSum=leftSum+arr[i]

eqIdx = findEquilibriumPoint([-7, 1, 5, 2, -4, 3, 0], 7)
print('equilibrium index', eqIdx)