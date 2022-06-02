def findMinRec(A, n):
    if (n == 1):
        return A[0]
    return min(A[n - 1], findMinRec(A, n - 1))
if __name__ == '__main__':
    A = [1, 5, 50, 7, -60, 20, 3]
    n = len(A)
def findMaxRec(A, n):
    if (n == 1):
        return A[0]
    return max(A[n - 1], findMaxRec(A, n - 1))
if __name__ == "__main__":
    A = [-1, 4, 23, 6, 99, 10, 2]
    n = len(A)
print("Minimum Value:")
print(findMinRec(A, n))
print("Maximum Value:")
print(findMaxRec(A, n))