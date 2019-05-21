def findFactorial(n):
    if n == 1 or n == 0:
        return 1
    return n*findFactorial(n-1)

T = int(input())
shouldProcess=True
if T<1 or T>19:
    shouldProcess = False

if shouldProcess:
    output = []
    for i in range(T):
        N = int(input())
        if N<0 or N>18:
            continue
        output.append(findFactorial(N))
    for op in output:
        print(op)

