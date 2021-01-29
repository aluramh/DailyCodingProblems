def solution(A, B):
    A.sort()
    B.sort()
    i = 0

    for a in A:
        # Increase the pointer until the comaparing values are similar.
        while i < len(B) - 1 and B[i] < a:
            i += 1
        if a == B[i]:
            return a
    return -1


print(solution([1, 3, 2, 1], [4, 2, 5, 3, 2]))
print(solution([3, 5], [4, 2, 5, 3, 2]))
print(solution([3, 5], [4, 2, 5, 3, 2]))
