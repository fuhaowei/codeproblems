# basically it's just implement connect 4 the boardgame but with a twist
# so there's an infinite board, -inf <= x <= inf, and 0 <= y <= inf
# 2 players take turns
# basically implement move(player, column)
# which inserts a piece into the bottom of that column, and pushes all the other pieces upwards
# then move should return a player, if they won, or nothing if game is still going 
# at game start ur given integer k 
# a player wins if they get k pieces in a row horizontally or vertically 
# if a player makes a move that would give both players k in a row,
# then the player making the move wins

"""
basically it's just implement connect 4 the boardgame but with a twist
so there's an infinite board, -inf <= x <= inf, and 0 <= y <= inf
2 players take turns
basically implement move(player, column)
which inserts a piece into the bottom of that column, and pushes all the other pieces upwards
then move should return a player, if they won, or nothing if game is still going 
at game start ur given integer k 
a player wins if they get k pieces in a row horizontally or vertically 
if a player makes a move that would give both players k in a row,
then the player making the move wins
"""

def move(player : str, col : int) -> str | None: 
    pass


class GameState:
    def __init__(self, k : int):
        self.board = defaultdict(list)  # stores [col][row]
        self.k = k

    # return the player that won or None if game is still going
    # win is k-in-a-row, horizontally or vertically
    def is_vertical_win(col):
        column = self.board[col]
        player = column[-1]  # bottom piece
        if len(column) < self.k:
            return False

        for row in range(1, self.k):
            if column[~row] != player:
                return False
        return True

    # returns True if there's a horizontal win
    # stemming from (row,col)
    def is_horizontal_win(row, col):
        count = 1
        player = self.board[col][row]
        for offset in range(1, self.k):
            left_col  = col - offset
            right_col = col + offset
            if getPieceAt(row, left_col) == player:
                count += 1
            if getPieceAt(row, right_col) == player:
                count += 1
        return count >= self.k
            
    def getPieceAt(row, col):
        column = self.board[col]
        if row >= len(column):
            return None
        return column[~row]
    
    def move(self, player, col):
        column = self.board[col]
        column.append(player)

        # check for vertical win
        if is_vertical_win(col):
            return player
            
        # check for horizontal win
        other_player_won = None
        for row in range(len(column)):
            p = self.board[col][row]
            if is_horizontal_win(row, col): 
                if p == player:
                    return player
                else:
                    other_player_won = p

        return other_player_won
        
    
'''
Sample Errors:
    1. start count = 0
    2. don't refactor getPieceAt 
    3. 
'''
''' 