from turtle import update
from movement import Movement
from functions import manyfunctions

class Piece():
    
    def __init__(self, board, initial_housing, color, type, killable=False):
        self.board = board
        self.match = self.board.match
        self.last_housing = None
        self.current_housing = initial_housing
        self.color = color
        self.eaten = False
        self.killable = killable
        self.type = type
        self.movements = 0

    def update_index(self):
        self.indexes = manyfunctions.index_2d(self.board.housings, self)
        self.current_line = self.indexes[0]
        self.current_column = self.indexes[1]

    def __str__(self):
        return (f' {self.color[0]}{self.type[0]} ')

    def move(self, next_housing):#as peças tem a o calculate_possible_moves especifico e a classe pai Piece possui o método "global" das classes: move, que possui o mesmo procedimento pra todas(diferente dos possíveis movimentos)
        valid_movements = self.calculate_possible_moves()
        if next_housing in valid_movements :
            if next_housing.killable == True:
                movement = Movement(self.board, self, next_housing)
                next_housing = self
                self.last_housing = self.current_housing
                self.current_housing = Piece(self.board,self.last_housing,None,"void", killable= True)
                self.current_housing = next_housing
                self.movements += 1
                return [self,self.last_housing, movement] 
        else:
            print("Movimento inválido")

    def calculate_possible_moves(self):
        possible_moves = []
        return possible_moves