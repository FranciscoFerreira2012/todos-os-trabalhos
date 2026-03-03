import tkinter as tk
from tkinter import messagebox

def ClicaBotao(index):
    global jogadorAtual, board, buttons
    # Verifica sea posição no board está vazia
    if board[index] == '':
        # Atualiza  board com o jogador atual
        board[index] = jogadorAtual
        # Atualiza o texto do butão
        buttons[index].config(text=jogadorAtual)
        # Verifica se há um vencedor
        if VerificaVencedor():
            messagebox.showinfo('Fim de Jogo', f'Jogador {jogadorAtual} venceu!')
            Reset()
        # Verifica se há um empate
        elif '' not in board:
            messagebox.showinfo('Fim de Jogo', 'Empate!')
            Reset()
        # Verifica se há um empate
        elif '' not in board:
            messagebox.showinfo('Fim de Jogo', 'Empate')
            Reset()
        else:
            # Alterna o jogador atual
            if jogadorAtual == 'X':
                jogadorAtual = 'O'
            else:
                jogadorAtual = 'X'

# Função  que verifica se há um vencedor
def VerificaVencedor():
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Colunas
        [0, 4, 8], [2, 4, 6]             # Diagonais
    ]
    for comb in combinacoes:
        # Verifica se todos os três elementos da combinação são iguais e não vazio
        if board[comb[0]] == board[comb[1]] == board[comb[2]] != '':
            return True
    return False

def Reset():
    global jogadorAtual, board
    jogadorAtual = 'X'
    # Limpar a lista de lógica
    board = ['' for _ in range(9)]
    # Limpar o texto dos botões visuais
    for button in buttons:
        button.config(text='')

if __name__ == '__main__':
    janela = tk.Tk()  # Cria a janela principal do Tkkinter
    janela.title('Jogo do Galo') # Define o título da janela

    jogadorAtual= 'X'  # Define o jogador inicial como 'X'
    board = ['' for _ in range(9)]  # Inicializa o board vazio
    buttons = []  # Lista para armazenar os butões

    # Cria a grade de botões 3x3
    for i in range(9):
        button = tk.Button(janela, text=' ', font=('normal', 40), width=5, height=2, command=lambda i=i: ClicaBotao(i))

        # Matemática simples para grelha 3x3:
        # Linha: 0, 0, 0 | 1, 1, 1 | 2, 2, 2
        linha = i // 3
        # Coluna 0, 1, 2 | 0, 1, 2 | 0, 1, 2
        coluna = i % 3

        button.grid(row=linha, column=coluna)
        buttons.append(button)
    
    janela.mainloop()  # Inicia o loo principal do Tkinter