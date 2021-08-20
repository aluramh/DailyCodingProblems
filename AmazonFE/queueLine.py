"""
Some people are standing in a queue. A selection process follows a rule where
people standing on even positions are selected. Of the selected people a queue
is formed and again out of these only people on even position are selected.
This continues until we are left with one person. Find out the position of
that person in the original queue.

Input:
The first line of input contains an integer T denoting the number of test
cases. The first line of each test case is N,number of people standing in a
queue.

Output:
Print the position(original queue) of that person who is left.
Constraints:

1 ≤ T ≤ 1000
1 ≤ N ≤ 100000000

Example:
Input
1
5

Output
4
"""


def solution(N):
    def helper(arr):
        if len(arr) == 1:
            return arr[0]
        else:
            new_arr = []
            for i in range(len(arr)):
                if i % 2 == 0:
                    new_arr.append(arr[i])
            return helper(new_arr)

    arr = []
    for i in range(N):
        arr.append(i)

    single_person = helper(arr)
    return single_person


print(solution(12))
print(solution(15))


def other():
    for i in range(int(input())):
        a = int(input())
        b = range(1, a + 1)
        c = []

        for j in b:
            c.append(j)
        while True:
            if len(c) == 1:
                break
            else:
                c = c[1:len(c):2]
        d = b.index(c[0])
        print(d + 1)
