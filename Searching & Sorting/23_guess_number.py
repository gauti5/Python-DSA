# Guess Number or lower 

# leetcode -> 374

def guess_number(n, pick):
    low=0
    high=n

    while low<=high:
        mid=(low+high)//2
        result=guess(mid)

        if result==0:
            return mid

        elif result==1:
            low=mid+1
        else:
            high=mid-1
    return result

n=10
pick=6

print(guess_number(n, pick))