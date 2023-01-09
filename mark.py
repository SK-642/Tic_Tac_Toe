p1=input('p1, input your name: ')
p2=input('p2, input your name: ')
def mark():
    marker=''
    while marker!='X' and marker!='O':
        marker=input( f"{p1}, choose 'X' or'O': ").upper()
    if marker=='X':
        return('X','O')
    else:
        return('O','X')
    
    
(p1,p2)=mark()