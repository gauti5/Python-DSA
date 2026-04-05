# Build an Array With Stack Operations

# Leetcode -> 1441

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result=[]
        index=0
        length=len(target)
        for i in range(1, n+1):
            if index<length and i==target[index]:
                result.append("Push")
                index+=1
            else:
                result.append("Push")
                result.append("Pop")

            if index==length:
                break
        return result