def levenshtein_distance(s1: str, s2: str) -> int:
    ld = [[0] * (len(s2)+1) for i in range(len(s1)+1)]
    ld[0] = range(len(s2)+1)

    for i in range(1, len(s1)+1):
        ld[i][0] = i
        for j in range(1, len(s2)+1):
            diff = 0 if s1[i-1] == s2[j-1] else 1
            ld[i][j] = min(
                ld[i-1][j] + 1,
                ld[i][j-1] + 1,
                ld[i-1][j-1] + diff
            )
    return ld[len(s1)][len(s2)]


def levenshtein_distance_recursive(s1: str, s2: str) -> int:
    def lev(a, b, i, j):
        if i == 0: return j
        elif j == 0: return i
        else:
            diff = 0 if a[i-1] == b[j-1] else 1
            dist = min(
                lev(a, b, i-1, j) + 1,
                lev(a, b, i, j-1) + 1,
                lev(a, b, i-1, j-1) + diff
            )
            return dist
    return lev(s1, s2, len(s1), len(s2))
