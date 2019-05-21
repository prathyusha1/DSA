def printSpiralMatrix(arr, m, n):
    k = 0
    l = 0
    while k < m and l < n:
        # print first row
        for i in range(l, n):
            print(arr[k][i], end= " ")
        k = k + 1
        # print last column
        for i in range(k, m):
            print(arr[i][n-1], end= " ")
        n = n - 1
        # print last row
        for i in range(n-1, l-1, -1):
            print(arr[m-1][i], end= " ")
        m = m-1
        # print first column
        for i in range(m-1, k-1, -1):
            print(arr[i][l], end= " ")
        l = l+1


input_arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

printSpiralMatrix(input_arr, 4, 4)
