# Get the lowest item in both of the arrays


def solution(A, B):
    A.sort()
    B.sort()
    i = 0

    for a in A:
        # Increase the pointer until the comaparing values are similar.
        # NOTE: - Had to change this line because it had an "if" instead of "while"
        while i < len(B) - 1 and B[i] < a:
            i += 1
        if a == B[i]:
            return a
    return -1


print(solution([1, 3, 2, 1], [4, 2, 5, 3, 2]))
print(solution([3, 5], [4, 2, 5, 3, 2]))
print(solution([3, 5], [4, 2, 5, 3, 2]))
