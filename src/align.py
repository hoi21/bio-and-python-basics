def needleman_wunsch(a, b, match=1, mismatch=-1, gap=-1):
    """Global alignment. Return (score, aligned_a, aligned_b)."""
    n, m = len(a), len(b)

    # TODO: build the (n+1) x (m+1) score matrix F

    # TODO: initialize first row and column with gap penalties

    # TODO: fill the matrix (max of diagonal, up, left)

    # TODO: traceback from F[n][m] to F[0][0], building both aligned strings

    raise NotImplementedError


if __name__ == "__main__":
    print(needleman_wunsch("GCATGCG", "GATTACA"))