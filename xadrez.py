# xadrez.py

# Representação simples de peças
# p: peão, t: torre, c: cavalo, b: bispo, q: rainha, k: rei
# letras minúsculas: pretas | maiúsculas: brancas

tabuleiro = [
    ["t", "c", "b", "q", "k", "b", "c", "t"],
    ["p"] * 8,
    [" "] * 8,
    [" "] * 8,
    [" "] * 8,
    [" "] * 8,
    ["P"] * 8,
    ["T", "C", "B", "Q", "K", "B", "C", "T"],
]

def mostrar_tabuleiro():
    print("  a b c d e f g h")
    for i, linha in enumerate(tabuleiro):
        print(8 - i, " ".join(linha), 8 - i)
    print("  a b c d e f g h")

def mover_peca(origem, destino):
    colunas = "abcdefgh"
    try:
        col_o, lin_o = colunas.index(origem[0]), 8 - int(origem[1])
        col_d, lin_d = colunas.index(destino[0]), 8 - int(destino[1])
        peca = tabuleiro[lin_o][col_o]
        if peca == " ":
            print("Nenhuma peça na posição de origem.")
            return
        tabuleiro[lin_d][col_d] = peca
        tabuleiro[lin_o][col_o] = " "
        print(f"Movido {peca} de {origem} para {destino}")
    except (IndexError, ValueError):
        print("Movimento inválido.")

def main():
    while True:
        mostrar_tabuleiro()
        origem = input("Digite a posição de origem (ex: e2): ")
        destino = input("Digite a posição de destino (ex: e4): ")
        if origem.lower() == "sair" or destino.lower() == "sair":
            break
        mover_peca(origem, destino)

if __name__ == "__main__":
    main()
