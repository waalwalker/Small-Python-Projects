import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        # Creating the board first
        self.board = self.make_new_board()
        
        self.dig = set()
        
    def make_new_board(self):
        # Generate a new Board for the game
        board = [[None for _ in  range(self.dim_size)] for _ in range(self.dim_size)]
        
        # Generating and planting bombs in the game
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            
            if board[row][col] == '*':
                # this will verify if the bomb is already planted or not
                continue
            
            board[row][col] = '*' # Planting a bomb in the board
            bombs_planted =+ 1
        
        return board
                
    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # If there is already a bomb then it will continue the process
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)
            
    def get_num_neighboring_bombs(self, row, col):
        # Here we will iterate through all the positions and count total no. of bombs
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
                    
        return num_neighboring_bombs
                          
    
    def dig(self, row, col):
        self.dug.add((row, col))
            
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                    if (r, c) in self.dug:
                        continue
                    self.dig(r, c)
        
        return True
    
    
    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dim_size:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
             
def play(dim_size=10, num_bombs=10):
    board = Board(dim_size, num_bombs)
    
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row, col:"))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid Location for the input. Please Try again.")
            continue
        
        safe = board.dig(row, col)
        if not safe:
            break
        
    if safe:
        print("CONGRATS YOU won!!!!")
    else:
        print("GAME OVER, YOU LoSe!!!")
        
        
if __name__ == '__main__':
    play()