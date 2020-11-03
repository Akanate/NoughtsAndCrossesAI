######################
# Created By Akanate #
######################


import os
import time
class NoughtsAndCrosses:
    def __init__(self):
        self.board = [
            '1','2','3',
            '4','5','6',
            '7','8','9'
        ]
        self.turn = False
        self.score = None
        self.ai = 'O'   
        self.human = 'X'
        self.depthMin = 0
        self.depthMax = 0
        self.execution = None
        self.menu()

    def menu(self):
        #MAIN MENU
        print(''' 
    | \\ | |                 | |   | |       /\\             | |  / ____|                                 /\\   |_   _|
    |  \\| | ___  _   _  __ _| |__ | |_     /  \\   _ __   __| | | |     _ __ ___  ___ ___  ___  ___     /  \\    | |  
    | . ` |/ _ \\| | | |/ _` | '_ \\| __|   / /\\ \\ | '_ \\ / _` | | |    | '__/ _ \\/ __/ __|/ _ \\/ __|   / /\\ \\   | |  
    | |\\  | (_) | |_| | (_| | | | | |_   / ____ \\| | | | (_| | | |____| | | (_) \\__ \\__ \\  __/\\__ \\  / ____ \\ _| |_ 
    |_| \\_|\\___/ \\__,_|\\__, |_| |_|\\__| /_/    \\_\\_| |_|\\__,_|  \\_____|_|  \\___/|___/___/\\___||___/ /_/    \\_\\_____|
    ____               __/ |                     _                                                                 
    |  _ \\            /\\___/ |                   | |                                                                
    | |_) |_   _     /  \\  | | ____ _ _ __   __ _| |_ ___                                                           
    |  _ <| | | |   / /\\ \\ | |/ / _` | '_ \\ / _` | __/ _ \\                                                          
    | |_) | |_| |  / ____ \\|   < (_| | | | | (_| | ||  __/                                                          
    |____/ \\__, | /_/    \\_\\_|\\_\\__,_|_| |_|\\__,_|\\__\\___|                                                          
            __/ |                                                                                                   
            |___/  ''')
        choice = input('1.Start a game against an AI\n2.Exit\nEnter a choice: ')
        if choice == '1':
            self.drawGrid()
             
        elif choice == '2':
            exit()
        else:
            print('Invalid Choice!')
            self.menu()

    def resetBoard(self):
        self.board = [
            '1','2','3',
            '4','5','6',
            '7','8','9'
        ]
        self.menu()


    def drawGrid(self):
        #CREATES NOUGHTS AND CROSSES GRID
        os.system('cls')
        print('\n')
        print(f'\t\t   {self.board[0]}  |  {self.board[1]}  |  {self.board[2]}')
        print('                  ---------------')
        print(f'\t\t   {self.board[3]}  |  {self.board[4]}  |  {self.board[5]}')                                
        print('                  ---------------')
        print(f'\t\t   {self.board[6]}  |  {self.board[7]}  |  {self.board[8]}')
        print('\n')
        print(f"YOU: {self.human} AI: {self.ai}")
        print(f"Max Depth: {self.depthMax} Min Depth: {self.depthMin}")
        if self.execution != None:
            print(self.execution)
        self.markGrid(self.turn)
    
    def markGrid(self,player):
        #MARKS THE GRID AND CHECKS TO SEE IF THE PLAYER OR AI HAS WON OR NOT YET
        values = {'X':'Crosses','O': 'Nought'}
        CheckWin = self.checkWinner()
        if CheckWin == 1:
            print(f'{values.get(self.ai)} has won!')
            time.sleep(2)
            os.system('cls')
            self.resetBoard()
            self.menu()

        elif CheckWin == -1:
            print(f'{values.get(self.human)} has won!')
            time.sleep(2)
            os.system('cls')
            self.resetBoard()
        
        elif CheckWin == 0:
            print('Draw')
            time.sleep(2)
            os.system('cls')
            self.resetBoard()

        #CHECKING WHOS TURN IT IS NOUGHTS OR CROSSSES AND DEPENDENT ON TURN DOING MIN OR MAX
        try:
            if self.turn == False:
                choice = input(f'Enter the number where you want to go >> ')
                if self.board[int(choice)-1].isdigit():
                    self.board[int(choice)-1] = self.human
                self.turn = True
                self.drawGrid()
            else:
                self.turn = False
                self.AI()
        except IndexError:
            print('Invalid Choice')
            time.sleep(5)
            self.drawGrid()


    def AI(self):
        #AI TRIES TO MAKE BEST MOVE POSSIBLE
        bestScore = float('-inf')
        self.depthMax = 0
        self.depthMin = 0
        bestMove = 0
        start_time = time.time()
        for i in range(len(self.board)):

            if self.board[i].isalpha():
                continue
            else:
                self.depthMax += 1
                self.board[i] = self.ai
                score = self.minimax(self.depthMax,False)
                if score > bestScore: bestScore = score; bestMove = i
                self.board[i] = str(i+1)
                self.depthMax+=1

        end_time = time.time()
        self.board[bestMove] = self.ai
        self.execution = f'Calculation Time: {abs(start_time-end_time)}'
        self.turn = False
        self.drawGrid()

        
         
    def minimax(self,depth,returnValue):
        #MINIMAX ALGORITHM TO FIND OUT BEST MOVE TO PERFORM
        result = self.checkWinner()
        if result != None:
            return result
        if returnValue:
            bestScore = float('-inf')
            for i in range(len(self.board)):
                #CHECKS IF SPOT IS AVAILABLE ON THE BOARD AND THEN PERFORMS MINIMAX
                if self.board[i].isalpha():
                    continue
                else:
                    self.depthMax += 1
                    self.board[i] = self.ai
                    score = self.minimax(self.depthMax,False)
                    bestScore = max(score,bestScore)
                    self.board[i] = str(i+1)
            return bestScore
        else:
            bestScore = float('inf')
            for i in range(len(self.board)):
                #CHECKS IF A SPOT IS AVAILABLE ON THE BOARD AND THEN PERFORMS MINIMAX
                if self.board[i].isalpha():
                    continue
                else:
                    self.depthMin += 1
                    self.board[i] = self.human
                    score = self.minimax(self.depthMin,True)
                    bestScore = min(score,bestScore)
                    self.board[i] = str(i+1)
            return bestScore


    def checkWinner(self):
        #CHECKS IF X OR O HAS WON BY GOING ACROSS THE BOARD.
        if(self.board[0] == self.ai and self.board[1] == self.ai and self.board[2] == self.ai or self.board[3] == self.ai and self.board[4] == self.ai and self.board[5] == self.ai or self.board[6] == self.ai and self.board[7] == self.ai and self.board[8] == self.ai):
            return 1

        if(self.board[0] == self.human and self.board[1] == self.human and self.board[2] == self.human or self.board[3] == self.human and self.board[4] == self.human and self.board[5] == self.human or self.board[6] == self.human and self.board[7] == self.human and self.board[8] == self.human):
            return -1

        #CHECKS IF X OR O HAS WON GOING UP OR DOWN THE BOARD.
        if(self.board[0] == self.ai and self.board[3] == self.ai and self.board[6] == self.ai or self.board[1] == self.ai and self.board[4] == self.ai and self.board[7] == self.ai or self.board[2] == self.ai and self.board[5] == self.ai and self.board[8] == self.ai):
            return 1

        if(self.board[0] == self.human and self.board[3] == self.human and self.board[6] == self.human or self.board[1] == self.human and self.board[4] == self.human and self.board[7] == self.human or self.board[2] == self.human and self.board[5] == self.human and self.board[8] == self.human):
            return -1

        #CHECKS IF X OR O HAS WON VIA GOING DIAGNOL ON THE BOARD.
        if(self.board[0]  == self.ai and self.board[4]  == self.ai and self.board[8] == self.ai or self.board[2]  == self.ai and self.board[4]  == self.ai and self.board[6] == self.ai):
            return 1

        if(self.board[0] == self.human and self.board[4] == self.human and self.board[8] == self.human or self.board[2] == self.human and self.board[4] == self.human and self.board[6] == self.human):
            return -1
        #CHECKS FOR A DRAW BY SEEING IF THERE ARE ANY NUMBERS REMAINING
        e=0
        for i in self.board:
            if i.isdigit():
                continue
            else:
                e+=1
                if e==len(self.board):
                    return 0
        return None
                
        
    
NoughtsAndCrosses()
