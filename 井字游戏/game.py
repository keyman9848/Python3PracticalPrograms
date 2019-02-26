#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 15:46
# @Author  : Cunyu
# @Site    : cunyu1943.github.io
# @File    : game1.py
# @Software: PyCharm

# Tic-Tac-Toe 井字棋游戏

# 定义全局常量
X="X"
O="O"
EMPTY=" "

# 询问是否重开一局
def ask_yes_no(question):
    response=None;
    while response not in("y","n"):
        response=input(question).lower()
    return response

# 输入位置数字
def ask_number(question ,low,high):
    response=None
    while response not in range(low,high):
        response=int(input(question))
    return response

# 询问谁先走，先走方执X,后走方执O,然后返回两者的落子代号
def pieces():
    go_first=ask_yes_no("玩家你是否要先落子？（y/n):")
    if go_first=="y":
        print("\n玩家你先走.")
        human=X
        computer=O
    else:
        print("\n计算机先走.")
        computer=X
        human=O
    return computer,human

# 产生一个新的空棋盘列表
def new_board():
    board=[]
    for square in range(9):
        board.append(EMPTY)
    return board

# 显示棋盘
def display_board(board):
    board2=board[:]
    for i in range(len(board)):
        if board[i]==EMPTY:
            board2[i]=i
    print("\t",board2[0],"|",board2[1],"|",board2[2])
    print("\t","-" * 10)
    print("\t",board2[3],"|",board2[4],"|",board2[5])
    print("\t", "-" * 10)
    print("\t",board2[6],"|",board2[7],"|",board2[8],"\n")
    # 产生可以合法走棋位置序列（也就是还未下过子位置）
def legal_moves(board):
    moves=[]
    for square in range(9):
        if board[square]==EMPTY:
            moves.append(square)
    return moves

# 判断胜负
def winner(board):
    # 所有可能赢的情况，行、列、对角线连成3个即可，例如（0,1,2）就是第一行，（2,4,6）就是对角线，
    # 将其存在一个元祖当中，然后用每次下棋的结果对这个元祖进行遍历，若满足其中的一个元素，则判定下棋的一方为胜者
    WAYS_TO_WIN=((0,1,2,),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]]!=EMPTY:
            winner=board[row[0]]
            return winner
	# 棋盘落满子时则判定为平局
    if EMPTY not in board:
        return "DEUCE"
    return False

# 玩家下棋
def human_move(board,human):
    legal =legal_moves(board)
    move =None
    while move not in legal:
        move=ask_number("你要走哪个位置？（0-8）：",0,9)
        if move not in legal:
            print("\n此位置已经落过子了，请重新选择落子位置")
    return  move

# 计算机下棋
def computer_move(board,computer ,human):
    board=board[:]
    # 按优劣顺序排序的下棋走子
    BEST_MOVES=(4,0,2,6,8,1,3,5,7) # 最佳下棋位置顺序表
	# 如果计算机能赢，就走那个位置
    for move in legal_moves(board):
            board[move]=computer
            if winner(board)==computer:
                print("计算机正在计算下棋位置...",move)
                return move
                # 取消走棋方案
            board[move]=EMPTY
            # 若玩家能赢就堵住那个位置
    for move in legal_moves(board):
            board[move]=human
            if winner(board)==human:
                print("计算机正在计算下棋位置...",move)
                return move
                # 取消走棋方案
            board[move]=EMPTY
    # 如果不是上面情况，也就是这一轮赢不了
    # 则是从最佳下棋位置表中挑出第一个合法位置
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print("计算机正在计算下棋位置，请稍候....",move)
            return move

# 落子角色转换 
def next_turn(turn):
    if turn == X:
         return  O
    else:
        return  X

# 主函数
def main():
        computer,human=pieces()
        # 默认先手为X
        turn =X
        # 创建新棋盘
        board=new_board()
        display_board(board)
        while not winner(board):
            if turn ==human:
                move=human_move(board,human)
                board[move]=human
            else:
                move=computer_move(board,computer,human)
                board[move]=computer
            display_board(board)
            turn=next_turn(turn)   # 角色转换
		# 游戏结束输出输赢或和棋信息
        the_winner=winner(board)
        if the_winner==computer:
            print("计算机赢！")
        elif the_winner==human:
            print("玩家赢！")
        elif the_winner=="DEUCE":
            print("平局，游戏结束！")

if __name__ == '__main__':
	while True:
		main()
		print('是否退出?(y/n)')
		choice =input()
		if choice == 'y':
			break
		else:
			print('开始下一局')
