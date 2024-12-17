# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        #analisando as linhas
        for i in range(0,3):
            soma = 0
            for c in range(0,3):
                soma += self.matriz[i][c]
            
            if soma == 3:
                return Tabuleiro.JOGADOR_0
            elif soma == 12:
                return Tabuleiro.JOGADOR_X
            
        #analisando as colunas
        for i in range(0,3):
            soma = 0
            for c in range(0,3):
                soma += self.matriz[c][i]
        
            if soma == 3:
                return Tabuleiro.JOGADOR_0
            elif soma == 12:
                return Tabuleiro.JOGADOR_X
            
        #analisando as diagonais
        soma_diag1 = self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2]
        soma_diag2 = self.matriz[0][2] + self.matriz[1][1] + self.matriz[2][0]

        if soma_diag1 == 3 or soma_diag2 == 3:
            return Tabuleiro.JOGADOR_0
        elif soma_diag1 == 12 or soma_diag2 == 12:
            return Tabuleiro.JOGADOR_X
        
        return Tabuleiro.DESCONHECIDO
    
 
    
  