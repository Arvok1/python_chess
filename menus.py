from match import Match 
from functions import manyfunctions



class Menu():

    def menu_inicial(self):
        manyfunctions.clear_screen()
        manyfunctions.line_break()
        print("1 - Jogar nova partida")
        print("2 - Carregar partida Salva")
        print("3 - Ver estatísticas")
        print("4 - Sair do menu")
        manyfunctions.line_break()
        selection = int(input("Qual a opção desejada?\n"))
        if selection == 1:
            match = Match()
            match.while_on_match()
        elif selection == 2:
            pass 
        elif selection == 3:
            pass 
        elif selection == 4:
            pass 
        

menus = Menu()
