def getNums(n):
    arr = []
    while n > 0:
        rem = n%10
        arr.append(rem)
        n = int(n/10)
    return arr

def checkIsArmstrong(n):
    # allNums = getNums(n)
    allNums = [int(a) for a in str(n)]
    sum = 0
    for num in allNums:
        sum = sum + (num ** 3)
    return sum == n

T = int(input())
for i in range(T):
    N = int(input())
    isArmStr = checkIsArmstrong(N)
    print( 'Yes' if isArmStr else 'No')
