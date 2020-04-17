"""
Given a string containing only three types of characters: '(', ')' 
and '*', write a function to check whether this string is valid. 
We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding 
right parenthesis ')'.

Any right parenthesis ')' must have a corresponding 
left parenthesis '('.

Left parenthesis '(' must go before the corresponding 
right parenthesis ')'.

'*' could be treated as a single right parenthesis ')' or 
a single left parenthesis '(' or an empty string.

An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True

Note:
The string size will be in the range [1, 100].
"""
def check_valid_string(s):
    lst = list(s)

    left_parens = []
    stars = []

    for i in range(len(lst)):
        if lst[i] == "(":
            left_parens.append(i)

        elif lst[i] == "*":
            stars.append(i)

        else: # if ")"
            if left_parens:
                left_parens.pop()

            elif stars:
                stars.pop()

            else:
                return False


    while left_parens:
        if not stars:
            return False
    
        elif left_parens[-1] < stars[-1]:
            left_parens.pop()
            stars.pop()

        else:
            return False

    return True

