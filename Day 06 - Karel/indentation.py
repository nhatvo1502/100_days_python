

def jump_straight():
    turn_left()
    move()
    turn_right()
    height = 0
    while wall_in_front()==True:
        jump_straight()
        height+=1
        print(height)
    turn_right()
    move()
    turn_right()
    for h in height:
        move()
    turn_left
    