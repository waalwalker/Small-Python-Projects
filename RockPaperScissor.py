import random

def play():
    user = input("What is your Choice? \n'R' for rock,'P' for paper, and 'S' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It is a tie!'
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You WONNN!!!'
    
    return 'You Lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
            return True
        

print(play())
        