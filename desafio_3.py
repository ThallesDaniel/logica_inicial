import tkinter as tk
import unicodedata
import csv
import os

def remover_acentos(txt: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', txt)
        if unicodedata.category(c) != 'Mn'
    )

def contar_buracos(texto):
    buracos = {
        'A': 1, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1,
        'a': 1, 'd': 1, 'o': 1, 'p': 1, 'q': 1, 'e': 1, 'g': 1,
        'B': 2, 'b': 2
    }
    texto = remover_acentos(texto)
    return sum(buracos.get(char, 0) for char in texto)

def atualizar_contagem(event=None):
    texto = entrada.get()
    resultado.set(f"Buracos: {contar_buracos(texto)}")

def salvar_resultado():
    texto = entrada.get()
    qtd_buracos = contar_buracos(texto)

    formato = formato_var.get()

    if formato == "CSV":
        arquivo = "Saida.csv"
        existe = os.path.isfile(arquivo)

        with open(arquivo, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not existe:
                writer.writerow(["Texto", "Quantidade de Buracos"])
            writer.writerow([texto, qtd_buracos])

    else: 
        arquivo = "Saida.txt"
        existe = os.path.isfile(arquivo)

        with open(arquivo, mode="a", encoding="utf-8") as f:
            if not existe:
                f.write("Texto | Quantidade de Buracos\n")
                f.write("-" * 40 + "\n")
            f.write(f"{texto} | {qtd_buracos}\n")

    resultado.set(f"Buracos: {qtd_buracos} (salvo em {arquivo})")

root = tk.Tk()
root.title("Contador de Buracos")

resultado = tk.StringVar()

tk.Label(root, text="Digite o texto:").pack()
entrada = tk.Entry(root, width=50)
entrada.pack()
entrada.bind("<KeyRelease>", atualizar_contagem)

tk.Label(root, textvariable=resultado, font=("Arial", 14)).pack()

formato_var = tk.StringVar(value="CSV") 
tk.Label(root, text="Escolha o formato de saída:").pack()
tk.Radiobutton(root, text="CSV", variable=formato_var, value="CSV").pack(anchor="w")
tk.Radiobutton(root, text="TXT", variable=formato_var, value="TXT").pack(anchor="w")

tk.Button(root, text="Salvar Resultado", command=salvar_resultado).pack(pady=10)

root.mainloop()