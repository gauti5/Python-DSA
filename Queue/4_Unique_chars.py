# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        cc={}
        for char in s:
            cc[char]=cc.get(char, 0)+1
        for i, char in enumerate(s):
            if cc[char]==1:
                return i
        return -1
        '''

        freq_char={}
        for char in s:
            freq_char[char]=freq_char.get(char,0)+1

        queue=[]
        for index, char in enumerate(s):
            queue.append((char, index))
        
        while queue:
            char, index=queue.pop(0)
            if freq_char[char]==1:
                return index
        return -1
            