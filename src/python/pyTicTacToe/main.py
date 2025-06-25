from pathlib import Path
import tkinter as tk
from eval_move import eval_move
from outcome_convention import Outcome


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        path = Path(__file__).parent / 'assets'
        self.assets = { 'empty': tk.PhotoImage(file=path/'empty.png'),
                        'o': tk.PhotoImage(file=path/'o.png'),
                        'x': tk.PhotoImage(file=path/'x.png')}

        self.board = None
        self.buttons = None
        self.popup = None
        self.reset()

        self.window.title('Tic-Tac-Toe')
        self.window.resizable(False, False)
        self.window.mainloop()

    def reset(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.create_board()
        if self.popup is not None:
            self.popup.destroy()
            self.popup = None

    def popup_message(self, message, bg=None):
        self.window.update_idletasks()

        w, h = 320, 120
        x = (self.window.winfo_x()) + (self.window.winfo_width() // 2) - (w // 2) + 6
        y = (self.window.winfo_y()) + (self.window.winfo_height() // 2) - (h // 2) + 6

        self.popup = tk.Toplevel()
        self.popup.overrideredirect(True)
        self.popup.geometry(f"{w}x{h}+{x}+{y}")
        if bg is None:
            bg2 = '#7F7F7F'
        else:
            bg2 = bg
        bg3 = '#777777'
        fg = '#F1F1F1'
        font = 'Comic Sans MS'
        self.popup.config(bg=bg2)
        label = tk.Label(self.popup, text=message, font=(font, 22), bg=bg2, foreground=fg)
        label.pack(pady=10)
        tk.Button(self.popup, text="jogar novamente", font=(font, 16), command=self.reset, bg=bg3, activebackground=bg3, foreground=fg, relief='flat').pack()
        self.popup.grab_set()



    def create_board(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.window,
                                                   image=self.assets['empty'],
                                                   width=128, height=128,
                                                   relief='sunken', cursor='hand2',
                                                   activebackground='#1F1F1F', bg='#1F1F1F',
                                                   command=lambda r=row, c=col: self.make_move(r, c))
                self.buttons[row][col].grid(row=row, column=col)


    def redraw(self):
        for r in range(3):
            for c in range(3):
                match self.board[r][c]:
                    case 0: self.buttons[r][c].config(image=self.assets['empty'])
                    case 1: self.buttons[r][c].config(image=self.assets['o'])
                    case -1: self.buttons[r][c].config(image=self.assets['x'])
                    case _: raise ValueError(f"Os estados válidos do tabuleiro são 0, 1 e -1. Foi encontrado '{self.board[r][c]}' na posição [{r}][{c}].")



    def make_move(self, r, c):
        result = enum_eval_move(self.board, r, c)
        self.redraw()
        match result:
            case Outcome.X_WINS:
                self.popup_message("Jogador 𝒪 ganhou!")
            case Outcome.O_WINS:
                self.popup_message("Jogador ✘ ganhou!")
            case Outcome.DRAW:
                self.popup_message("Empate!")
            case Outcome.INVALID_MOVE:
                self.window.bell()
            case Outcome.INVALID_STATE:
                self.window.destroy()
                raise ValueError("Estado inválido do tabuleiro")
            case Outcome.CONTINUE: pass

def enum_eval_move(board, r, c):
    result = eval_move(board, r, c)
    if isinstance(result, int):
        match result:
            case -4: return Outcome.INVALID_MOVE
            case -2: return Outcome.INVALID_STATE
            case 0: return Outcome.CONTINUE
            case 1: return Outcome.X_WINS
            case 2: return Outcome.O_WINS
            case 3: return Outcome.DRAW
    return result

if __name__ == '__main__':
    TicTacToe()