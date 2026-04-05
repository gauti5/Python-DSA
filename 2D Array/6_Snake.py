# Snake in Matrix (leetcode - 3248)

def snake(n, commands):
    row=col=0
    for command in commands:
        if command=='UP':
            row-=1
        elif command=='DOWN':
            row+=1
        elif command=='RIGHT':
            col+=1
        elif command=='LEFT':
            col-=1
    return (row*n)+col

n=3
commands=['RIGHT','DOWN', 'LEFT']
print(snake(n, commands))