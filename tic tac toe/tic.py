import os

def print_board(arr):
    one =   "X" if arr[0] == 1 else ("O" if arr[0] == 2 else "1")
    two =   "X" if arr[1] == 1 else ("O" if arr[1] == 2 else "2")
    three = "X" if arr[2] == 1 else ("O" if arr[2] == 2 else "3")
    four =  "X" if arr[3] == 1 else ("O" if arr[3] == 2 else "4")
    five =  "X" if arr[4] == 1 else ("O" if arr[4] == 2 else "5")
    six =   "X" if arr[5] == 1 else ("O" if arr[5] == 2 else "6")
    seven = "X" if arr[6] == 1 else ("O" if arr[6] == 2 else "7")
    eight = "X" if arr[7] == 1 else ("O" if arr[7] == 2 else "8")
    nine =  "X" if arr[8] == 1 else ("O" if arr[8] == 2 else "9")
    print()
    print(f"{one} | {two} | {three}")
    print(f"---------")
    print(f"{four} | {five} | {six}")
    print(f"---------")
    print(f"{seven} | {eight} | {nine}")
    print()

board = [0,0,0,0,0,0,0,0,0]
print_board(board)
for i in range(9):
    if i % 2 == 0:
        print("Enter P1:",end="")
        i = int(input())
        os.system("cls")
        board[i-1]=1
    else:
        print("Enter P2:",end="")
        i = int(input())
        os.system("cls")
        board[i-1]=2
    print_board(board)
