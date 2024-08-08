import tkinter as tk
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x500")
        self.window.configure(background="#ADD8E6")  # light blue background
        self.player_turn = 1
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.buttons = [] 
        self.result_label = tk.Label(self.window, text="", font=("Helvetica", 24), fg="blue", bg="#ADD8E6")
        self.result_label.pack(pady=20)
        self.player_mode_label = tk.Label(self.window, text="Select player mode:", font=("Helvetica", 14), fg="black", bg="#ADD8E6")
        self.player_mode_label.pack(pady=10)
        self.single_player_button = tk.Button(self.window, text="Single Player", command=self.single_player_mode, font=("Helvetica", 12), fg="white", bg="#00698f")
        self.single_player_button.pack(pady=5)
        self.double_player_button = tk.Button(self.window, text="Double Player", command=self.double_player_mode, font=("Helvetica", 12), fg="white", bg="#00698f")
        self.double_player_button.pack(pady=5) 
        self.window.mainloop()

    def single_player_mode(self):
        self.player_mode_label.pack_forget()
        self.single_player_button.pack_forget()
        self.double_player_button.pack_forget()
        self.create_board()
        self.timer = 30
        self.timer_label = tk.Label(self.window, text=f"Time left: {self.timer}", font=("Helvetica", 18), fg="black", bg="#ADD8E6")
        self.timer_label.pack(pady=10)
        self.timer_start()
        self.computer_player = True

    def double_player_mode(self):
        self.player_mode_label.pack_forget()
        self.single_player_button.pack_forget()
        self.double_player_button.pack_forget()
        self.create_board()
        self.timer = 30
        self.timer_label = tk.Label(self.window, text=f"Time left: {self.timer}", font=("Helvetica", 18), fg="black", bg="#ADD8E6")
        self.timer_label.pack(pady=10)
        self.timer_start()
        self.computer_player = False

    def create_board(self):
        frame = tk.Frame(self.window, bg="gray")
        frame.pack(pady=50)
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(frame, text="", command=lambda row=i, column=j: self.click(row, column), height=3, width=6, bg="white", fg="black")
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def click(self, row, column):
        if self.board[row][column] == 0:
            if self.player_turn == 1:
                self.board[row][column] = 1
                self.buttons[row][column].config(text="X", fg="blue")
                self.player_turn = 2
            else:
                self.board[row][column] = 2
                self.buttons[row][column].config(text="O", fg="red")
                self.player_turn = 1
            self.check_win()
            self.timer_reset()
            if self.computer_player and self.player_turn == 2:
                self.computer_move()

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0]
        if empty_cells:
            row, column = random.choice(empty_cells)
            self.board[row][column] = 2
            self.buttons[row][column].config(text="O", fg="red")
            self.player_turn = 1
            self.check_win()
            self.timer_reset()

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                self.game_over(self.board[i][0])
                return
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                self.game_over(self.board[0][i])
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.game_over(self.board[0][0])
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0]!= 0:
            self.game_over(self.board[0][2])
            return
        if all(all(cell!= 0 for cell in row) for row in self.board):
            self.game_over(0)

    def game_over(self, winner):
        if winner == 1:
            self.result_label.config(text="X wins!", fg="blue")
        elif winner == 2:
            self.result_label.config(text="O wins!", fg="red")
        else:
            self.result_label.config(text="It's a draw!", fg="black")
        self.disable_buttons()
        self.timer_label.pack_forget()  # remove the timer label

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def timer_start(self):
        self.timer_reset()
        self.timer_tick = self.window.after(1000, self.timer_tick_down)

    def timer_reset(self):
        self.timer = 30
        self.timer_label.config(text=f"Time left: {self.timer}", fg="black")

    def timer_tick_down(self):
        self.timer -= 1
        if self.timer <= 5:
            self.timer_label.config(text=f"Time left: {self.timer}", fg="red")
        else:
            self.timer_label.config(text=f"Time left: {self.timer}", fg="black")
        if self.timer > 0:
            self.timer_tick = self.window.after(1000, self.timer_tick_down)
        else:
            self.auto_move()

    def auto_move(self):
        if self.computer_player and self.player_turn == 2:
            self.computer_move()
        else:
            self.game_over(0)

if __name__ == "__main__":
    game = TicTacToe()