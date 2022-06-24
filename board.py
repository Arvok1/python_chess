from piece import Piece

class Board():

    def __init__(self, match):
        self.match = match
        self.create_housings() 
        self.eaten_pieces = []
 
    def create_housings(self):
        linhas = range(8)
        colunas = range(8)
        matriz = [[0 for x in range(8)] for y in range(8)] 
        for linha in linhas:
            for coluna in colunas:
                matriz[linha][coluna] = (Piece(self,matriz[linha][coluna],None,"void", killable=True))
            
        self.housings = matriz 

    def still_board(self, what_position):
        if (what_position[0] > -1 
        and what_position[1] > -1 
        and what_position[0] < 8
        and what_position[1] < 8): 
            return True 
        else:
            return False 

    def check_king_killable(self):
        for i in range(8):
            for j in range(8):
                if self.housings[i][j].type == "king" and self.housings[i][j].color == self.match.actual_player.color:
                    if self.housings[i][j].killable == True:
                        return True 
                    else:
                        return False         

    def print_board(self):

        board = "    H    G    F    E    D    C    B    A    \n"
        
        for i in range(8):
            correct_line = str(i+1)
            board += correct_line
            board += " "
            for j in range(8):
                self.housings[i][j].update_index()
                board += "|"
                if self.housings[i][j].type != "void":
                    board += str(self.housings[i][j])
                else:
                    board += " ** "
            board += "|"
            board += "\n"
        print(board)
                