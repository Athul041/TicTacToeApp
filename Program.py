import random

def tic_tac_check(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c
    if((ax==bx and bx==cx) or (ay==by and by==cy)):
        return True
    elif(ax==ay and bx==by and cx==cy):
        return True
    elif((ax+ay)==2 and (ax+ay)==(bx+by) and (bx+by)==(cx+cy)):
        return True
    else:
        return False

def get_o_selected_next(x_selected, o_selected, unselected):
    for x in o_selected:
        for y in [i for i in o_selected if i != x]:
            for z in unselected:
                if(tic_tac_check(x,y,z)):
                    print(f"z = {z}")
                    return z
    for x in x_selected:
        for y in [i for i in x_selected if i != x]:
            for z in unselected:
                if(tic_tac_check(x,y,z)):
                    print(f"z = {z}")
                    return z
    return random.choice(unselected)

def print_board(x_selected, o_selected, unselected):
    for i in range(3):
            for j in range(3):
                if not ((i,j) in unselected):
                    if (i,j) in x_selected:
                        print(" X ", end =" ")
                    elif (i,j) in o_selected:
                        print(" O ", end =" ")
                else:
                    print(f"{i},{j}", end =" ")
            print('\n')

def win_check(tArray):
    for x in tArray:
        for y in [i for i in tArray if i != x]:
            for z in [i for i in tArray if (i !=x and i != y)]:
                if(tic_tac_check(x,y,z)):
                    return True

x_selected = []
o_selected = []
unselected = [(x,y) for x in range(3) for y in range(3)]

game_on = 0

print("Press Enter to Start")
if(not input()):
    game_on = 1
    while game_on == 1 and len(unselected) > 0:
        
        print("You are X. Select cell")
        print_board(x_selected, o_selected, unselected)

        i = input()
        if i:
            if len(i.split(',')) == 2:
                x, y = [int(i) for i in i.split(',')]
                if (x, y) in unselected:
                    print("Unselected")
                    x_selected.append((x,y))
                    unselected.remove((x,y))
                    if win_check(x_selected):
                        game_on = 0
                        break
                    print_board(x_selected, o_selected, unselected)
                    o_next = get_o_selected_next(x_selected, o_selected, unselected)
                    o_selected.append(o_next)
                    unselected.remove(o_next)
                    if win_check(o_selected):
                        game_on = 0
                        break
                else:
                    print("Already selected")
    print("GAME OVER")
    print_board(x_selected, o_selected, unselected)
    inp = input()

