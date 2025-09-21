"""
Escreva um programa em sua linguagem de preferência (console).

O programa deve apresentar como saída a quantidade de buracos nas letras.
Verifique o tratamento das letras (acentuação, maiúsculas, minúsculas).
"""
import unicodedata

def remover_acentos(txt: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', txt)
        if unicodedata.category(c) != 'Mn'
    )

def contar_buracos(texto: str) -> int:
    """
    Conta o número de buracos nas letras de um texto.
    Letras com 1 buraco: A, D, O, P, Q, R, a, d, o, p, q, e, g
    Letras com 2 buracos: B, b
    """
    buracos = {
        'A': 1, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1,
        'a': 1, 'd': 1, 'o': 1, 'p': 1, 'q': 1, 'e': 1, 'g': 1,
        'B': 2, 'b': 2
    }
    
    texto = remover_acentos(texto)
    total = 0
    for letra in texto:
        total += buracos.get(letra, 0)
    return total


if __name__ == "__main__":
    texto = input("Digite um texto: ")
    print(f"O texto possui {contar_buracos(texto)} buracos.")
