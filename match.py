from ctypes.wintypes import CHAR
from logging import exception
from msilib.schema import File
from king import King
from board import Board 
from pawn import Pawn  
from queen import Queen
from knight import Knight
from rook import Rook
from bishop import Bishop
from player import Player
import string 
import random 
from functions import manyfunctions

class Match():


    def __init__(self):
        self.players = [Player(self, "white"), Player(self, "black")]
        self.actual_player = self.players[0]
        self.create_board() 
        self.create_pieces()
        self.movements = []
        self.match_id = self.id_generator()
        self.file = self.create_file()
        

    def create_file(self):#método para salvar a partida em um arquivo
        match_index = open("matchs.txt","a+")
        match_index.write(f"{self.match_id} \n")
        match_index.close()
        match_file = open(f'{self.match_id}',"a+")
        return match_file
        
    
    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def load_match(self):
        pass

    def create_board(self):
        self.board = Board(self) 
    

    def create_pieces(self):
        #as peças são criadas todas como apontamentos de memória no tabuleiro
        #o código de criar as peças e colocar elas no tabuleiro consegue ser reduzido a muito menos linhas, menos manuais, mas para poupar tempo fiz assim, acaba ficando mais visual também
        #peças pretas
        self.board.housings[0][3] = King(self.board, self.board.housings[0][3],"black","king")
        self.board.housings[0][4] = Queen(self.board, self.board.housings[0][4],"black","queen")
        self.board.housings[0][1] = Knight(self.board, self.board.housings[0][1],"black","knight")
        self.board.housings[0][6] = Knight(self.board, self.board.housings[0][6],"black","knight")
        self.board.housings[0][2] = Bishop(self.board, self.board.housings[0][2],"black","bishop")
        self.board.housings[0][5] = Bishop(self.board, self.board.housings[0][5],"black","bishop")
        self.board.housings[0][0] = Rook(self.board, self.board.housings[0][0],"black","rook")
        self.board.housings[0][7] = Rook(self.board, self.board.housings[0][7],"black","rook")

        #peças brancas
        self.board.housings[7][3] = King(self.board, self.board.housings[7][3],"white","king")
        self.board.housings[7][4] = Queen(self.board, self.board.housings[7][4],"white","queen")
        self.board.housings[7][1] = Knight(self.board, self.board.housings[7][1],"white","knight")
        self.board.housings[7][6] = Knight(self.board, self.board.housings[7][6],"white","knight")
        self.board.housings[7][2] = Bishop(self.board, self.board.housings[7][2],"white","bishop")
        self.board.housings[7][5] = Bishop(self.board, self.board.housings[7][5],"white","bishop")
        self.board.housings[7][0] = Rook(self.board, self.board.housings[7][0],"white","rook")
        self.board.housings[7][7] = Rook(self.board, self.board.housings[7][7],"white","rook")
       
        


        for coluna in range(8):
            self.board.housings[1][coluna] = Pawn(self.board, self.board.housings[1][coluna],"black","pawn")
            self.board.housings[6][coluna] = Pawn(self.board, self.board.housings[6][coluna],"white","pawn")


    def __ask_for_movement(self):
        columns = "ABCDEFGH"
        columns_translated = "76543210"
        played = False 
        while not played:
            house_to_play = str(input("Em que casa está a peça desejada?\n"))
            translation_table = house_to_play.maketrans(columns, columns_translated)
            reverse_translation_table = {value: key for key, value in translation_table.items()}
            translated_house = house_to_play.translate(translation_table)
            if self.board.housings[int(translated_house[1])-1][int(translated_house[0])].color == self.actual_player.color:
                print("Esses são os movimentos possíveis da peça que você escolheu:")
                possible_movements = self.board.housings[int(translated_house[1])-1][int(translated_house[0])].calculate_possible_moves()
                if possible_movements:
                    for housing in possible_movements:
                        line = housing.current_line
                        column = housing.current_column
                        column = str(column)
                        inverse_translated_column = column.translate(reverse_translation_table)
                        print(f'{inverse_translated_column}{line+1}\n')
                    house_to_movement = str(input("Para que casa deseja movimentar?"))
                    translated_movement = house_to_movement.translate(translation_table)
                    if self.board.housings[int(translated_movement[1])-1][int(translated_movement[0])] in possible_movements:
                        if not self.board.check_king_killable():
                            piece = self.board.housings[int(translated_house[1])-1][int(translated_house[0])].move(self.board.housings[int(translated_movement[1])-1][int(translated_movement[0])])
                            self.board.housings[int(translated_movement[1])-1][int(translated_movement[0])] = piece[0]
                            self.board.housings[int(translated_house[1])-1][int(translated_house[0])] = piece[1]
                            self.board.housings[int(translated_movement[1])-1][int(translated_movement[0])].update_index()
                            self.board.housings[int(translated_house[1])-1][int(translated_house[0])].update_index()
                            #piece[2].to_line = self.board.housings[int(translated_movement[1])-1][int(translated_movement[0])].current_line
                            #piece[2].to_column = self.board.housings[int(translated_movement[1])-1][int(translated_movement[0])].current_column
                            #piece[2].save_movements_text()
                            played = True 
                            print ("Movimento realizado")
                        else:
                            print( "Você precisa tirar o rei do xeque!")
                else:
                    print("Perdão, não há movimentos disponíveis")
            else:
                print("A peça escolhida não é do seu time")        


    def __change_player(self):
        if self.actual_player.color == "white":
            self.actual_player.color = "black"
            
        elif self.actual_player.color == "black":
            self.actual_player.color = "white"
            
        else:
            raise ValueError("That Player should not exist")
    
    def while_on_match(self):
        playing = True
        while playing:
            try:
                manyfunctions.clear_screen()
                self.board.print_board()
                self.__ask_for_movement()
                self.__change_player()

            except Exception as error:
                print(error.args)