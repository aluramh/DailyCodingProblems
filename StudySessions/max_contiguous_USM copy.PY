def swap_pair(a1, a2):
    if len(a1) == 0 or len(a2) == 0:
        return None

    # choose L and R
    if len(a1) > len(a2):
        R = frozenset(a2)
        L = a1
        # O(n)
        L_sum = sum(a1)
        R_sum = sum(a2)
    else:
        R = frozenset(a1)
        L = a2
        # O(n)
        L_sum = sum(a2)
        R_sum = sum(a1)

    delta = R_sum - L_sum  

    for n in L:
        looking_for = delta - n

        if looking_for in R:
            return (n, looking_for)

    return None


r = swap_pair([4, 1, 2, 1, 1, 2], [3, 6, 3, 3])
print(r)
assert r == (1, 3)
