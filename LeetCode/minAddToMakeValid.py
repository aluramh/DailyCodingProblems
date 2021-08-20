# 921. Minimum Add to Make Parentheses Valid

# A parentheses string is valid if and only if:

# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.


class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Declare stack
        parens = []
        needed_parens = 0

        # Empty string
        if s == '':
            return 0

        for char in s:
            print(char)

            # If it opens, it has to close... add it to the stack
            if char == "(":
                parens.append(char)

            elif char == ")":
                # If we have an end parens, but no start paren in the stack,
                # then this is extra and it needs a parens
                if len(parens) == 0:
                    needed_parens += 1
                else:
                    # There is an item, and we have to make sure it is an open
                    # parens
                    top_item = parens[len(parens) - 1]
                    if top_item == '(':
                        parens.pop()
                    elif top_item == ')':
                        needed_parens += 1

        return needed_parens + len(parens)


r = Solution().minAddToMakeValid("())")
print(r)
