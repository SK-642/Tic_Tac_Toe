l=['x','o','x','x','o','o','x','x','o','o']
def win(marker):
    print(l[1]==l[2]==l[3]==marker or l[4]==l[5]==l[6]==marker or l[7]==l[8]==l[9]==marker or 
    l[1]==l[4]==l[7]==marker or l[2]==l[5]==l[8]==marker or l[3]==l[6]==l[9]==marker or
    l[1]==l[5]==l[9]==marker or l[3]==l[5]==l[7]==marker)
win('o')