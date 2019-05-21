def printSum():
    matrix1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    matrix2 = [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
    sum = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            sum[i][j] = matrix1[i][j] + matrix2[i][j]
    
    print('sum is', sum)

printSum()
