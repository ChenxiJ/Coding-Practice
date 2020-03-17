def solution(A):
    # write your code in Python 3.6
    mapp = {}
    for i in A:
        if i not in mapp:
            mapp[i] = 1
        else:
            mapp[i] += 1
    for key, value in mapp.items():
        if value % 2 == 1:
            return key