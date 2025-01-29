class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with -1 to handle edge cases
        max_length = 0

        for cur_idx, char in enumerate(s):
            if char == '(':
                stack.append(cur_idx)  # Push index of '('
            else:
                stack.pop()  # Pop last element
                if not stack:
                    stack.append(cur_idx)  # Update base index
                else:
                    max_length = max(max_length, cur_idx - stack[-1])

        return max_length
