import math
import random

class Player:
    def __init__(self, letter):
        # letter is X or O as per the game
        self.letter = letter
        
        # A players' next move in the game
    def get_move(self, game):
            pass
        
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        # pass
        square = random.choice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        # pass
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # Here we are now going to check if the value entered is correct or not
            # as if the entered value is not an integer then the value entered is not correct
            # and it will be invalid and also it will check if that specific spot is available or not
            # which can also reuslt in an invalid if it's not avaiable
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # It's good if its successful!
            except ValueError:
                print('Invalid square, buddy! Lets try again.')
                
        return val
    
    
class GeniusComputerPlayer(Player):
        def __init__(self, letter):
            super().__init__(letter)
            
        def get_move(self, game):
            if len(game.available_moves()) == 9:
                square = random.choice(game.available_moves()) # Random choice
            else:
                # Based on the Minimax Algorithm we will get the square
                square = self.minimax(game, self.letter)['position']
            return square
        
        def minimax(self, state, player):
            max_player = self. letter # This is us
            other_player = 'O' if player == 'X' else 'X' # Other players' choice
            
            # Lets check if the previous move wins the match or not
            if state.current_winner == other_player:
                # we will keep track of the score for the minimax algo track
                return {'position': None, 
                        'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else - 1 * (state.num_empty_squares() +1 )
                        }
                
            elif not state.empty_squares(): # without empty squares
                return {'postion': None, 'score': 0}
            
            if player == max_player:
                best = {'position': None, 'score': -math.inf} # Maximizing the score
            else:
                best = {'position': None, 'score': math.inf} # Minimizing the score
                
            for possible_move in state.avaiable_moves():
                # Step 1:Perform a move, try that spot
                state.make_move(possible_move, player)
                # Step 2: Recurse and simulating after this move using minimax
                sim_score = self. minimax(state, other_player) # Here we will alternate the players
                
                # Step 3: Undoing the move
                state.board[possible_move] = ' '
                state.current_winner = None
                sim_score['position'] = possible_move # Just to not make it meesed up
                
                # Step 4: Updating dictionary with score
                if player == max_player: # Trying to maximize the player
                    if sim_score['score'] > best['score']:
                        best = sim_score # Replacing the best
                else: # Minimizing the other player
                        if sim_score['score'] < best['score']:
                            best = sim_score # Replacing the best
                
            return best