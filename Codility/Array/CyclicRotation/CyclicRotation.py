def solution(A, K):
    if len(A) <= 1:
        return A
    shift = K%len(A)
    if shift == 0:
        return A
    return A[-shift:] + A[:len(A)-shift]

# this exercies reminds of how important the edge cases are, consider when the array length
# is 0, cannot do mod, when array length is 1 or when the rotation equals to the array length