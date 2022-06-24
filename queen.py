from piece import Piece 
from bishop import Bishop
from rook import Rook 

class Queen(Piece):

    def __init__(self, board, initial_housing, color, type):
        super().__init__(board=board, initial_housing=initial_housing, color=color, type=type)

    def calculate_possible_moves(self):
        
        possible_moves = []

        possible_moves.append(Bishop.calculate_possible_moves(self))
        possible_moves.append(Rook.calculate_possible_moves(self))

        return possible_moves