class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for char in s:
            if char not in mapping.keys():
                stack.append(char)
            else:
                if stack:
                    top_element = stack.pop()
                    if top_element != mapping[char]:
                        return False
                    else:
                        continue
                else:
                    return False
        return True if not stack else False


if __name__ == "__main__":
    s = "(]"
    print(Solution().isValid(s))
