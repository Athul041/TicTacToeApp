import random

def tic_tac_check(arr):
    ax, ay = arr[0]
    bx, by = arr[1]
    cx, cy = arr[2]
    print("a = ", ax, ay)
    print("b = ", bx, by)
    print("c = ", cx, cy)
    if((ax==bx and bx==cx) or (ay==by and by==cy)):
        print("1")
        return True
    elif(ax==ay and bx==by and cx==cy):
        print("2")
        return True
    elif((ax+ay)==2 and (ax+ay)==(bx+by) and (bx+by)==(cx+cy)):
        print("3")
        return True
    else:
        print("4")
        return False

def get_O_next(X, O, Unselected):
    for x in O:
        for y in O.pop(O.indexof(x)):
            for row in Unselected:
                for z in row:
                    if(tic_tac_check(x,y,z)):
                        return z
    for x in X:
        for y in X.pop(X.indexof(x)):
            for z in Unselected:
                if(tic_tac_check(x,y,z)):
                    return z
    return random.choice(Unselected[0])

def print_board(X,O,Unselected):
    for i in range(3):
            for j in range(3):
                if(not Unselected[i][j]):
                    if((i,j) in X):
                        print("X")
                    elif((i,j) in O):
                        print("O")
                else:
                    print(i,j, end =" ")    
            print('\n')

def remove_Unselected(arr, Unselected):
    for row in Unselected:
        if((x,y) in row):
            row.remove(arr)
            return True
    return False

def check_in_Unselected(arr, Unselected):
    print("Checking {0} in Unselected", arr)
    for row in Unselected:
        print(row)
        if((x,y) in row):
            return True
    return False

X = []
O = []
Unselected = [[(x,y) for x in range(3)] for y in range(3)]

game_on = 0

print(Unselected)
print("Press Enter to Start")
if(not input()):
    game_on = 1
    while(game_on == 1):
        print("You are X. Select cell")
        print_board(X,O,Unselected)
        i = input()
        if i:
            x,y = i.split(',')
            if(check_in_Unselected((x,y), Unselected)):
                X.append((x,y))
                remove_Unselected((x,y), Unselected)
                print_board(X,O,Unselected)
                # get_O_next(X,O,Unselected)
                game_on = 0
                break
            else:
                game_on = 0
                break
            inp = input()
            if inp:
                game_on = 0

