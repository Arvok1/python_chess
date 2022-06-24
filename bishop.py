from piece import Piece 

class Bishop(Piece):

    def __init__(self, board, initial_housing, color, type):
        super().__init__(board=board, initial_housing=initial_housing, color=color, type=type)

    def calculate_possible_moves(self):
        possible_moves = []
        diagonals = [
                        [[self.current_line + i, self.current_column + i] for i in range(0,7)],
                        [[self.current_line + i, self.current_column - i] for i in range(1,7)],
                        [[self.current_line - i, self.current_column - i] for i in range(1,7)],
                        [[self.current_line - i, self.current_column + i] for i in range(0,7)]
        ]

        for possible_diagonal in diagonals:
            for position in possible_diagonal:
                if self.board.still_board(position):
                    if self.board.housings[position[0]][position[1]].color == self.color: 
                           break 
                    else:

                        if self.board.housings[position[0]][position[1]].color != self.color:
                            self.board.housings[position[0]][position[1]].killable = True
                            possible_moves.append(self.board.housings[position[0]][position[1]])
                            if self.board.housings[position[0]][position[1]].color != None:
                                self.board.housings[position[0]][position[1]].killable = True 
                                possible_moves.append(self.board.housings[position[0]][position[1]])
                                break 
        return possible_moves