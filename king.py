from piece import Piece 

class King(Piece):

    def __init__(self, board, initial_housing, color, type):
        super().__init__(board=board, initial_housing=initial_housing, color=color, type=type)

    
    def calculate_possible_moves(self):
        possible_moves = []
        for y in range(1,3):
            for x in range(1,3):
                if self.board.still_board((self.current_line - 1 +y, self.current_column - 1 + x)):

                    if self.board.housings[self.current_line -1 + y][self.current_column - 1 + x].color == self.color: 
                           break 
                        
                    else:
                        if self.board.housings[self.current_line -1 + y][self.current_column - 1 + x].color != self.color:
                            self.board.housings[self.current_line -1 + y][self.current_column - 1 + x].killable = True
                            possible_moves.append(self.board.housings[self.current_line -1 + y][self.current_column - 1 + x])
                            if self.board.housings[self.current_line -1 + y][self.current_column - 1 + x].color != None:
                                self.board.housings[self.current_line -1 + y][self.current_column - 1 + x].killable = True 
                                possible_moves.append(self.board.housings[self.current_line -1 + y][self.current_column - 1 + x])
                                break 

        return possible_moves