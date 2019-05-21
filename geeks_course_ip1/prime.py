import math

def findIsPrime(n):
    sqNum = int(math.sqrt(n))
    for i in range(2, sqNum+1):
        if n%i == 0:
            return "No"
    return "Yes"

T = int(input())
shouldProcess=True
if T<1 or T>100:
    shouldProcess = False

if shouldProcess:
    output = []
    for i in range(T):
        N = int(input())
        if N<0 or N>1000:
            continue
        output.append(findIsPrime(N))
    for op in output:
        print(op)

