import tkinter as tk
import unicodedata

# Função para remover acentos
def remover_acentos(txt: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', txt)
        if unicodedata.category(c) != 'Mn'
    )

# Função que conta os buracos nas letras
def contar_buracos(texto: str) -> int:
    buracos = {
        'A': 1, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1,
        'a': 1, 'd': 1, 'o': 1, 'p': 1, 'q': 1, 'e': 1, 'g': 1,
        'B': 2, 'b': 2
    }
    texto = remover_acentos(texto)  # normaliza antes de contar
    return sum(buracos.get(letra, 0) for letra in texto)

# Atualiza o contador a cada tecla digitada
def atualizar_contagem(event=None):
    texto = entrada.get()
    resultado.set(f"Buracos: {contar_buracos(texto)}")

# Interface Tkinter
root = tk.Tk()
root.title("Contador de Buracos")

resultado = tk.StringVar()

tk.Label(root, text="Digite o texto:").pack()
entrada = tk.Entry(root, width=50)
entrada.pack()
entrada.bind("<KeyRelease>", atualizar_contagem)

tk.Label(root, textvariable=resultado, font=("Arial", 14)).pack()

root.mainloop()
