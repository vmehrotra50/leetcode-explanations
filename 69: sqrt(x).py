# Problem: https://leetcode.com/problems/sqrtx/
# Initial Thoughts: the key to understanding this solution is to understand that sqrt(x) must be bounded by 0 and x, and sqrt(x) being an integer
# means we  have an ordered "list" of all integers from [0...x]. Such a problem closely resembles the binary serach problem, which involves an
# efficient log(n) search of a sorted list. In this case, using a pointer i, we can start at the middle of [0...x] and determine whether i^2 is
# greater than, less than, or eqaul to x. The 3 outcomes are explained as follows:
#   1. i^2 > x: We must now search the bottom half [0...i)
#   2. i^2 < x: We must now search the top half (i...x]
#   3. i^2 = x: We've found sqrt(x)
# By repeating the above procedure until the 3rd condition is met, we can solve this problem in log(n) time and constant space.

def mySqrt(self, x: int) -> int:
    l, r = 0, x # initialize [0...x]

    while l <= r:
        i = (l + r) // 2
        if (i*i > x):
            r = i - 1
        elif (i*i < x):
            l = i + 1
        else:
            return i

    return r # if solution still not found, return r, representing truncated decimal solution
