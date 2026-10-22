def needleman_wunsch(a, b, match=1, mismatch=-1, gap=-1):
    """Global alignment. Return (score, aligned_a, aligned_b)."""
    n, m = len(a), len(b)

    # TODO: build the (n+1) x (m+1) score matrix F
    F = [[0] * (m + 1) for _ in range(n + 1)]

    # TODO: initialize first row and column with gap penalties
    for i in range(1, n + 1):
        F[i][0] = i * gap
    for j in range(1, m + 1):
        F[0][j] = j * gap

    # TODO: fill the matrix (max of diagonal, up, left)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                score = match
            else:
                score = mismatch
            F[i][j] = max(
                F[i - 1][j - 1] + score,
                F[i - 1][j] + gap,
                F[i][j - 1] + gap
            )

    # TODO: traceback from F[n][m] to F[0][0], building both aligned strings
    aligned_a = ""
    aligned_b = ""
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and F[i][j] == F[i - 1][j - 1] + (match if a[i - 1] == b[j - 1] else mismatch):
            aligned_a = a[i - 1] + aligned_a
            aligned_b = b[j - 1] + aligned_b
            i -= 1
            j -= 1
        elif i > 0 and F[i][j] == F[i - 1][j] + gap:
            aligned_a = a[i - 1] + aligned_a
            aligned_b = "-" + aligned_b
            i -= 1
        else:
            aligned_a = "-" + aligned_a
            aligned_b = b[j - 1] + aligned_b
            j -= 1
    return F[n][m], aligned_a, aligned_b



if __name__ == "__main__":
    print(needleman_wunsch("GCATGCG", "GATTACA"))