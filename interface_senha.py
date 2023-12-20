import tkinter as tk
from tkinter import messagebox
import random
import string


def gerar_senha_segura():
    comprimento = int(comprimento_entry.get())
    usar_maiusculas = maiusculas_var.get()
    usar_minusculas = minusculas_var.get()
    usar_numeros = numeros_var.get()
    usar_caracteres_especiais = caracteres_var.get()

    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_caracteres_especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    senha_gerada_label.config(text="A senha gerada é: " + senha)

    copiar.config(state=tk.NORMAL)


def copiar_senha():
    senha = senha_gerada_label.cget("text").split(": ")[1]
    janela.clipboard_clear()
    janela.clipboard_append(senha)
    janela.update()
    messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")


janela = tk.Tk()
janela.title("Gerador de Senhas Seguras")

comprimento_label = tk.Label(janela, text="Comprimento da senha:")
comprimento_label.pack()
comprimento_entry = tk.Entry(janela)
comprimento_entry.pack()

maiusculas_var = tk.IntVar()
maiusculas_check = tk.Checkbutton(janela, text="Letras maiúsculas", variable=maiusculas_var)
maiusculas_check.pack()

minusculas_var = tk.IntVar()
minusculas_check = tk.Checkbutton(janela, text="Letras minúsculas", variable=minusculas_var)
minusculas_check.pack()

numeros_var = tk.IntVar()
numeros_check = tk.Checkbutton(janela, text="Números", variable=numeros_var)
numeros_check.pack()

caracteres_var = tk.IntVar()
caracteres_check = tk.Checkbutton(janela, text="Caracteres especiais", variable=caracteres_var)
caracteres_check.pack()

gerar_button = tk.Button(janela, text="Gerar senha", command=gerar_senha_segura)
gerar_button.pack()

senha_gerada_label = tk.Label(janela, text="")
senha_gerada_label.pack()

copiar = tk.Button(janela, text="Copiar senha", state=tk.DISABLED, command=copiar_senha)
copiar.pack()

janela.mainloop()
