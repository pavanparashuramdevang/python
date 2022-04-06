import os
board={'tl':' ','tm':' ','tr':' ','ml':' ','mm':' ','mr':' ','ll':' ','lm':' ','lr':' '}
a='X'
b='X'
flag=1
flagperson=0

def pboard():
    print(f"{board['tl']}|{board['tm']}|{board['tr']}")
    print('-+-+-')
    print(f"{board['ml']}|{board['mm']}|{board['mr']}")
    print('-+-+-')
    print(f"{board['ll']}|{board['lm']}|{board['lr']}")

def clear():
    command='cls'
    os.system(command)
pboard()

while flag!=0:
    clear()
    #hardcoding the conditions

    if((board['tl']=='X' and board['tm']=='X' and board['tr']=='X') or(board['ml']=='X' and board['mm']=='X' and board['mr']=='X') or (board['ll']=='X' and board['lm']=='X' and board['lr']=='X') or (board['tl']=='X' and board['ml']=='X' and board['ll']=='X') or (board['tm']=='X' and board['mm']=='X' and board['lm']=='X') or (board['tr']=='X' and board['mr']=='X' and board['lr']=='X') or (board['tl']=='X' and board['mm']=='X' and board['lr']=='X') or (board['tr']=='X' and board['mm']=='X' and board['ll']=='X')):
        pboard()
        print("x won")
        flag=0
        break
    if((board['tl']=='0' and board['tm']=='0' and board['tr']=='0') or(board['ml']=='0' and board['mm']=='0' and board['mr']=='0') or (board['ll']=='0' and board['lm']=='0' and board['lr']=='0') or (board['tl']=='0' and board['ml']=='0' and board['ll']=='0') or (board['tm']=='0' and board['mm']=='0' and board['lm']=='0') or (board['tr']=='0' and board['mr']=='0' and board['lr']=='0') or (board['tl']=='0' and board['mm']=='0' and board['lr']=='0') or (board['tr']=='0' and board['mm']=='0' and board['ll']=='0')):
        pboard()
        print("0 won")
        flag=0
        break
    if " " not in board.values():
        print("there is no winner")
        break



    pboard()
    if flagperson==0:
        ina=input("enter the place of move first person x\n")
        if ina not in board.keys():
            print("choose the correct cell name")
            continue

        if board[ina]==' ':
            board[ina]=a
            flagperson=1
        else:
            print("please choose the null cell")
            
            continue
    
    else:
        ina=input("enter the place of move second person 0\n")
        if ina not in board.keys():
            print("choose the correct cell name")
            continue


        if board[ina]==' ':
            board[ina]='0'
            flagperson=0
        else:
            print("please choose the null cell")
            
            continue
