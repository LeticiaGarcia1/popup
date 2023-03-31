import tkinter
from tkinter import messagebox


root = tkinter.Tk()
root.withdraw()

count = 0

msg_box = messagebox.showwarning("Meu Amô", "VOCÊ FOI HACKEADO")

if msg_box == 'ok':
    msg_box = messagebox.showwarning("PERA AI!", "PARA SER DESHAKEADO PRECISO QUE ME RESPONDA UMA PERGUNTA...")

if msg_box == 'ok':
    msg_box = messagebox.askquestion("DIZ AI", "O QUE ACHA DE COMER JAPA HOJE?")

while msg_box == 'no':
    count += 1
    msg_box = messagebox.askquestion("DIZ AI", "O QUE ACHA DE COMER JAPA HOJE?")
    if (count == 5):
        msg_box = messagebox.showerror("VOU CHORAR!", "VOCÊ NÃO ME AMA MESMO!") 
        break

if msg_box == 'yes':
    msg_box = messagebox.showinfo("BOA!", "SABIA QUE ME AMAVA HAHA!")           