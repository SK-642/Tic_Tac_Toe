
def board(l):
    print(l[1]+'|'+l[2]+'|'+l[3])
    print(l[4]+'|'+l[5]+'|'+l[6])
    print(l[7]+'|'+l[8]+'|'+l[9])


def mark():
    marker=''
    while marker!='X' and marker!='O':
        marker=input( f"{p1}, choose 'X' or'O': ").upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

def first():
    flip=int(input("choose your lucky no. "))
    if (flip%7)//2==0:
        return (f'{p1}')
    else:
        return (f'{p2}')


#def placemark(board,mark,position):
   # l[position]=mark
   # return board(l)

def spacecheck(l,position):
    return (l[position]==' ')

def fullboard(l):
    for i in range(1,10):
        if l[i]==' ':
            return True
    else:
        return False

def playerinput(m,P,l):
    position=int(input(f'{m} choose position for your mark(1-9): '))
    while (not spacecheck(l,position)) or (position not in [1,2,3,4,5,6,7,8,9]):
        position=int(input(f'{m} choose position for your mark(1-9): '))
    if spacecheck(l,position):
        #return position
        l[position]=P
        board(l)

def win(l,marker):
    return (l[1]==l[2]==l[3]==marker or l[4]==l[5]==l[6]==marker or l[7]==l[8]==l[9]==marker or 
    l[1]==l[4]==l[7]==marker or l[2]==l[5]==l[8]==marker or l[3]==l[6]==l[9]==marker or
    l[1]==l[5]==l[9]==marker or l[3]==l[5]==l[7]==marker)

def replay():
    t=input('wanna play again, press y: ')
    return(t=='y')

#Actual Compilation

print("Welcome!! Thanos, son of A'lars")

#A loop to keep the game continued
while True:
    p1=input('p1, input your name: ')
    p2=input('p2, input your name: ')
    #get a board
    l=[' ']*10
    #who will go first
    turn=first()
    print(turn + ' will move first')
    pl1,pl2=mark()
    play_game=input('r u ready?(y or n): ')
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn== p1:
            #display board
            #choose a position
            playerinput(p1,pl1,l)
            #placemark(board,mark,position)
            #check for win
            if win(l,pl1):
                print(f'{p1} has won')
                game_on=False
            else:
                if not fullboard(l):
                    print('tie game')
                    game_on=False
                else:
                    turn=p2
        else:
            #display board
            #choose a position
            playerinput(p2,pl2,l)
            #placemark(board,mark,position)
            #check for win
            if win(l,pl2):
                print(f'{p2} has won')
                game_on=False
            else:
                if not fullboard(l):
                    print('tie game')
                    game_on=False
                else:
                    turn=p1
    #break out off loop
    if not replay():
        break








