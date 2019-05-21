def findMissingNumberUsingSum(n, arr):
    sumOfN = (n * (n+1))/2
    sumofArrayElems = sum(arr)
    return sumOfN-sumofArrayElems


def findMissingSumUsingXor(n, arr):
    inputXor = arr[0]
    for i in range(1, n-1):
        # print(i)
        inputXor = inputXor ^ arr[i]
    allXor = 1
    for i in range(2, n+1):
        allXor = allXor ^ i
    return inputXor ^ allXor


print(findMissingNumberUsingSum(8, [1, 2, 4, 6, 3, 7, 8]))
print(findMissingSumUsingXor(8, [1, 2, 4, 6, 3, 7, 8]))
