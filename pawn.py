from piece import Piece 

class Pawn(Piece):

    def __init__(self, board, initial_housing, color, type):
        super().__init__(board=board, initial_housing=initial_housing, color=color, type=type)

    def calculate_possible_moves(self):
        possible_moves = []
        #o if abaixo permite uma maior modularização do código de movimento
        #será substituido por um setter de atributo
        if self.color == 'black':
            pawn_initial_movement = 2
            pawn_kill_square = 1
            initial_range = (1,pawn_initial_movement)
            
        elif self.color == 'white':
            pawn_initial_movement = -2
            pawn_kill_square = -1
            initial_range = (pawn_initial_movement, -1)
        
        elif self.color == None:
            raise ValueError('This piece is not selectable')

        
        if self.movements == 0:# movimento inicial(poderia ser substituido por uma lógica de movimentos feitos)
           
            if self.board.housings[self.current_line + pawn_initial_movement][self.current_column].type == "void" and self.board.housings[self.current_line + pawn_kill_square][self.current_column].type == "void":
                
                for i in initial_range:
                    if self.board.housings[self.current_line+i][self.current_column].color == self.color: 
                                break
                    possible_moves.append(self.board.housings[self.current_line+i][self.current_column]) 

        else:
            kill_squares = [[self.current_line+pawn_kill_square, self.current_column+i] for i in range(-1,1)]

            for positions in kill_squares:
                if self.board.still_board(positions):
                        if self.board.housings[positions[0]][positions[1]].color != self.color:
                                self.board.housings[positions[0]][positions[1]].killable = True
                                possible_moves.append(self.board.housings[positions[0]][positions[1]])
                                if self.board.housings[positions[0]][positions[1]].color != None:
                                    self.board.housings[positions[0]][positions[1]].killable = True 
                                    possible_moves.append(self.board.housings[positions[0]][positions[1]])
                                    break 
                            #o código abaixo proibe que a peça passe por cima de seus aliados, entretanto, como o movimento dos peões está com problemas, não permite testar os cálculos da função
                        if self.board.housings[positions[0]][positions[1]].color == self.color: 
                                break 

        return possible_moves