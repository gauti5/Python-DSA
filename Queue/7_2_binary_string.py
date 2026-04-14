# Binary String with substrings representing 1 to N

# Leetcode -> 1016

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        queue=['1']
        checked=set()

        while queue:
            binary_str=queue.pop(0)
            num=int(binary_str,2)

            if num>n or num in checked:
                continue

            if binary_str not in s:
                return False
            checked.add(binary_str)

            queue.append(binary_str+'0')
            queue.append(binary_str+'1')
        return True