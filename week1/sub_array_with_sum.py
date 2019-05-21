def findSubArray(arr, n, sum):
    i = 1
    start = 0
    curr_sum = arr[0]
    while (i <= n):
        while curr_sum > sum and start < i-1:
            curr_sum = curr_sum - arr[start]
            start = start + 1
        if curr_sum == sum:
            print (start+1, i)
            return 1
        if i < n:
            curr_sum = curr_sum + arr[i]
        i = i + 1
    print ("No subarray found") 
    return 0

findSubArray([1, 4, 20, 3, 10, 5] , 6, 3)

