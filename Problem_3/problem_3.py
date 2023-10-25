import turtle as t

file = open('cs104_mysterydesign_two.txt', 'r')

lines = file.readlines()
for l in lines:
    l = l.split()
    for i in range(0, len(l), 2):
        x = int(l[i])
        y = int(l[i+1])
        print(f'goto ({x},{y})')
        t.goto(x, y)
        if i == 0:
            print('Pen down.')
            t.pendown()
    print('Pen up.')
    t.penup()

t.mainloop()
file.close()

