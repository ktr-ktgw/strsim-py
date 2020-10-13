def levenshtein_distance(s1, s2):
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
