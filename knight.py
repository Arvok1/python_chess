from piece import Piece 

class Knight(Piece):

    def __init__(self, board, initial_housing, color, type):
        super().__init__(board=board, initial_housing=initial_housing, color=color, type=type)
    
    def calculate_possible_moves(self):
        possible_moves = []

        for i in range(-2, 3):
            
            for j in range(-2, 3):

                if (i**2) + (j**2) == 5:

                    if self.board.still_board((self.current_line + i, self.current_column + j)):

                        if self.board.housings[self.current_line + i][self.current_column + j].color == self.color: 
                           break 
                        
                        else:

                            if self.board.housings[self.current_line + i][self.current_column + j] != self.color:
                                
                                self.board.housings[self.current_line + i][self.current_column + j].killable = True 
                                possible_moves.append(self.board.housings[self.current_line+i][self.current_column+j])

                                if self.board.housings[self.current_line + i][self.current_column + j].color != None:
                                    
                                    self.board.housings[self.current_line + i][self.current_column + j].killable = True 
                                    possible_moves.append(self.board.housings[self.current_line + i][self.current_column + j])
                                    break
        return possible_moves