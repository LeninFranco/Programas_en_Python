from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Game:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.resizable(0,0)
        self.clicked = True
        self.count = 0
        self.b1 = Button(self.window, text=" ", width=12, height=6, command=lambda: self.ActionButton(self.b1))
        self.b2 = Button(self.window, text=" ", width=12, height=6, command=lambda: self.ActionButton(self.b2))
        self.b3 = Button(self.window, text=" ", width=12, height=6, command=lambda: self.ActionButton(self.b3))
        self.b4 = Button(self.window, text=" ", width=12, height=6, command=lambda: self.ActionButton(self.b4))
        self.b5 = Button(self.window, text=" ", width=12, height=6, command=lambda: self.ActionButton(self.b5))
        self.b6 = Button(self.window, text=" ", width=12, height=6, command=lambda: self.ActionButton(self.b6))
        self.b7 = Button(self.window, text=" ", width=12, height=6, command=lambda: self.ActionButton(self.b7))
        self.b8 = Button(self.window, text=" ", width=12, height=6, command=lambda: self.ActionButton(self.b8))
        self.b9 = Button(self.window, text=" ", width=12, height=6, command=lambda: self.ActionButton(self.b9))
        self.b1.grid(row=0,column=0)
        self.b2.grid(row=0,column=1)
        self.b3.grid(row=0,column=2)
        self.b4.grid(row=1,column=0)
        self.b5.grid(row=1,column=1)
        self.b6.grid(row=1,column=2)
        self.b7.grid(row=2,column=0)
        self.b8.grid(row=2,column=1)
        self.b9.grid(row=2,column=2)
        self.window.mainloop()
    def ActionButton(self,b):
        if b["text"] == " " and self.clicked == True:
            b["text"] = "X"
            self.clicked = False
            self.count += 1
            self.WinnerSection()
        elif b["text"] == " " and self.clicked == False:
            b["text"] = "O"
            self.clicked = True
            self.count += 1
            self.WinnerSection()
        else:
            messagebox.showerror("Tic-Tac-Toe","Esta casilla ya ha sido seleccionada")
    def DissableAllButtons(self):
        self.b1.config(state="disabled")
        self.b2.config(state="disabled")
        self.b3.config(state="disabled")
        self.b4.config(state="disabled")
        self.b5.config(state="disabled")
        self.b6.config(state="disabled")
        self.b7.config(state="disabled")
        self.b8.config(state="disabled")
        self.b9.config(state="disabled")
    def WinnerSection(self):
        if self.b1["text"] == "X" and self.b2["text"] == "X" and self.b3["text"] == "X":
            self.b1.config(bg="lightblue")
            self.b2.config(bg="lightblue")
            self.b3.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA X","FELICIDADES X HA GANADO")
            self.window.destroy()
        elif self.b4["text"] == "X" and self.b5["text"] == "X" and self.b6["text"] == "X":
            self.b4.config(bg="lightblue")
            self.b5.config(bg="lightblue")
            self.b6.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA X","FELICIDADES X HA GANADO")
            self.window.destroy()
        elif self.b7["text"] == "X" and self.b8["text"] == "X" and self.b9["text"] == "X":
            self.b7.config(bg="lightblue")
            self.b8.config(bg="lightblue")
            self.b9.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA X","FELICIDADES X HA GANADO")
            self.window.destroy()
        elif self.b1["text"] == "X" and self.b4["text"] == "X" and self.b7["text"] == "X":
            self.b1.config(bg="lightblue")
            self.b4.config(bg="lightblue")
            self.b7.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA X","FELICIDADES X HA GANADO")
            self.window.destroy()
        elif self.b2["text"] == "X" and self.b5["text"] == "X" and self.b8["text"] == "X":
            self.b2.config(bg="lightblue")
            self.b5.config(bg="lightblue")
            self.b8.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA X","FELICIDADES X HA GANADO")
            self.window.destroy()
        elif self.b3["text"] == "X" and self.b6["text"] == "X" and self.b9["text"] == "X":
            self.b3.config(bg="lightblue")
            self.b6.config(bg="lightblue")
            self.b9.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA X","FELICIDADES X HA GANADO")
            self.window.destroy()
        elif self.b1["text"] == "X" and self.b5["text"] == "X" and self.b9["text"] == "X":
            self.b1.config(bg="lightblue")
            self.b5.config(bg="lightblue")
            self.b9.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA X","FELICIDADES X HA GANADO")
            self.window.destroy()
        elif self.b3["text"] == "X" and self.b5["text"] == "X" and self.b7["text"] == "X":
            self.b3.config(bg="lightblue")
            self.b5.config(bg="lightblue")
            self.b7.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA X","FELICIDADES X HA GANADO")
            self.window.destroy()
        elif self.b1["text"] == "O" and self.b2["text"] == "O" and self.b3["text"] == "O":
            self.b1.config(bg="lightblue")
            self.b2.config(bg="lightblue")
            self.b3.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA O","FELICIDADES O HA GANADO")
            self.window.destroy()
        elif self.b4["text"] == "O" and self.b5["text"] == "O" and self.b6["text"] == "O":
            self.b4.config(bg="lightblue")
            self.b5.config(bg="lightblue")
            self.b6.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA O","FELICIDADES O HA GANADO")
            self.window.destroy()
        elif self.b7["text"] == "O" and self.b8["text"] == "O" and self.b9["text"] == "O":
            self.b7.config(bg="lightblue")
            self.b8.config(bg="lightblue")
            self.b9.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA O","FELICIDADES O HA GANADO")
            self.window.destroy()
        elif self.b1["text"] == "O" and self.b4["text"] == "O" and self.b7["text"] == "O":
            self.b1.config(bg="lightblue")
            self.b4.config(bg="lightblue")
            self.b7.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA O","FELICIDADES O HA GANADO")
            self.window.destroy()
        elif self.b2["text"] == "O" and self.b5["text"] == "O" and self.b8["text"] == "O":
            self.b2.config(bg="lightblue")
            self.b5.config(bg="lightblue")
            self.b8.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA O","FELICIDADES O HA GANADO")
            self.window.destroy()
        elif self.b3["text"] == "O" and self.b6["text"] == "O" and self.b9["text"] == "O":
            self.b3.config(bg="lightblue")
            self.b6.config(bg="lightblue")
            self.b9.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA O","FELICIDADES O HA GANADO")
            self.window.destroy()
        elif self.b1["text"] == "O" and self.b5["text"] == "O" and self.b9["text"] == "O":
            self.b1.config(bg="lightblue")
            self.b5.config(bg="lightblue")
            self.b9.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA O","FELICIDADES O HA GANADO")
            self.window.destroy()
        elif self.b3["text"] == "O" and self.b5["text"] == "O" and self.b7["text"] == "O":
            self.b3.config(bg="lightblue")
            self.b5.config(bg="lightblue")
            self.b7.config(bg="lightblue")
            self.DissableAllButtons()
            messagebox.showinfo("GANA O","FELICIDADES O HA GANADO")
            self.window.destroy()
        elif self.count == 9: 
            self.DissableAllButtons()
            messagebox.showinfo("EMPATE","NI MODOS NADIE GANA")
            self.window.destroy()

if __name__ == "__main__":
    Game()