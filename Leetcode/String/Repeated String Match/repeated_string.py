# understand str.find(sub, start, end). A needs to be at least B long and also every c of A needs to have the chance to
# match the start of B, which is the n_A += A part

def repeated_string_match(A, B):
    n = (len(B) - 1) // len(A) + 1
    n_A_list = [A] * n
    n_A = ''.join(n_A_list)

    if n_A.find(B) >= 0:
        return n
    n_A += A
    if n_A.find(B) >= 0:
        return n + 1
    return -1