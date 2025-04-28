import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        
        self.score_frame = tk.Frame(self.master)
        self.score_frame.pack()
        
        self.player1_score = 0
        self.player2_score = 0
        
        self.score_label = tk.Label(self.score_frame, text=f"Player 1: {self.player1_score}  Player 2: {self.player2_score}")
        self.score_label.pack()
        
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack()
        
        # Buttons vor reset_game initialisieren
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.button_frame, text='', font='Arial 20', width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)
        
        # reset_game nach Button-Initialisierung aufrufen
        self.reset_game()
        
        self.reset_button = tk.Button(self.master, text='Reset Game', command=self.reset_game)
        self.reset_button.pack()
        
        self.play_button = tk.Button(self.master, text='Play Against AI', command=self.play_against_ai)
        self.play_button.pack()

    def reset_game(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        for row in self.buttons:
            for button in row:
                button.config(text='', state=tk.NORMAL)

    def make_move(self, row, col):
        if self.board[row][col] == '' and not self.game_over:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                self.game_over = True
                self.update_score()
            elif all(cell != '' for row in self.board for cell in row):
                self.game_over = True
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for row in self.board:
            if row.count(row[0]) == 3 and row[0] != '':
                messagebox.showinfo("Game Over", f"Player {row[0]} wins!")
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                messagebox.showinfo("Game Over", f"Player {self.board[0][col]} wins!")
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            messagebox.showinfo("Game Over", f"Player {self.board[0][0]} wins!")
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            messagebox.showinfo("Game Over", f"Player {self.board[0][2]} wins!")
            return True
        return False

    def update_score(self):
        if self.current_player == 'X':
            self.player1_score += 2
        else:
            self.player2_score += 2
        self.score_label.config(text=f"Player 1: {self.player1_score}  Player 2: {self.player2_score}")

    def play_against_ai(self):
        self.reset_game()
        self.current_player = 'X'
        while not self.game_over:
            if self.current_player == 'O':
                self.ai_move()
                self.current_player = 'X'

    def ai_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == '']
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
