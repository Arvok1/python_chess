class Movement():

    def __init__(self, board, piece_movimented, next_housing):
        self.board = board 
        self.piece_movimented = piece_movimented
        self.from_line = self.piece_movimented.current_line
        self.from_column = self.piece_movimented.current_column
        self.piece_eaten = next_housing
        self.to_line = 0
        self.to_column =  0

    def save_movements_text(self):
        columns = "ABCDEFGH"
        columns_translated = "76543210"
        columns_int = range(8)
        translation_table = str(columns_int).maketrans(columns_translated, columns)
        self.board.match.file.write(f'[piece:{self.piece_movimented} - from: {str(self.from_column).translate(translation_table)}{self.from_line+1} - to: {str(self.to_column).translate(translation_table)}{self.to_line+1} - eaten: {self.piece_eaten}]\n')

