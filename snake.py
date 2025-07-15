import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

# Set up the window
curses.initscr()
curses.noecho()
curses.curs_set(0)
win = curses.newwin(20, 60, 0, 0)  # height, width, starty, startx
win.keypad(1)
win.timeout(100)  # snake speed (milliseconds)

# Initial snake and food
snake = [[10, 30], [10, 29], [10, 28]]
food = [randint(1, 18), randint(1, 58)]
win.addch(food[0], food[1], '*')

# Initial direction
key = KEY_RIGHT
score = 0

while True:
    next_key = win.getch()
    if next_key != -1:
        key = next_key
    
    # Calculate new head position
    head = snake[0].copy()
    if key == KEY_RIGHT:
        head[1] += 1
    elif key == KEY_LEFT:
        head[1] -= 1
    elif key == KEY_UP:
        head[0] -= 1
    elif key == KEY_DOWN:
        head[0] += 1

    # Check for collision with borders or self
    if (
        head[0] == 0 or head[0] == 19 or
        head[1] == 0 or head[1] == 59 or
        head in snake
    ):
        break

    snake.insert(0, head)

    if head == food:
        score += 1
        food = None
        while food is None:
            nf = [randint(1, 18), randint(1, 58)]
            if nf not in snake:
                food = nf
        win.addch(food[0], food[1], '*')
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    win.addch(head[0], head[1], '#')

curses.endwin()
print(f"Game Over! Your score is {score}")
