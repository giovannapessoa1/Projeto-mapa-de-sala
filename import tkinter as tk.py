import tkinter as tk
from tkinter import simpledialog

# Função para imprimir o mapa no terminal
def imprimir_mapa(mapa):
    for linha in mapa:
        for celula in linha:
            if celula == 0:
                print(" ", end=" ")  # Espaço vazio
            elif celula == 1:
                print("■", end=" ")  # Parede
            elif celula == 2:
                print("D", end=" ")  # Porta
            elif celula == 3:
                print("I", end=" ")  # Item (cadeira)
        print()  # Nova linha após cada linha do mapa

# Função para atualizar a interface gráfica
def imprimir_mapa_gui():
    for widget in frame_mapa.winfo_children():
        widget.destroy()

    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            # Define o símbolo baseado no valor do mapa
            if mapa[i][j] == 0:
                simbolo = " "
            elif mapa[i][j] == 1:
                simbolo = "■"
            elif mapa[i][j] == 2:
                simbolo = "D"
            elif mapa[i][j] == 3:
                simbolo = "I"

            # Cria um botão para cada célula do mapa
            botao = tk.Button(frame_mapa, text=simbolo, width=4, height=2,
                              command=lambda i=i, j=j: alterar_celula_gui(i, j))
            botao.grid(row=i, column=j)

# Função para alterar a célula no gráfico
def alterar_celula_gui(linha, coluna):
    # Pergunta ao usuário o que ele quer colocar na célula
    tipo = simpledialog.askinteger("Escolher tipo", 
                                   f"O que você deseja colocar na posição ({linha}, {coluna})?\n"
                                   "1 - Parede (■)\n2 - Porta (D)\n3 - Espaço Vazio ( )\n4 - Item (I)",
                                   minvalue=1, maxvalue=4)
    if tipo:
        if tipo == 1:
            mapa[linha][coluna] = 1  # Parede
        elif tipo == 2:
            mapa[linha][coluna] = 2  # Porta
        elif tipo == 3:
            mapa[linha][coluna] = 0  # Espaço Vazio
        elif tipo == 4:
            mapa[linha][coluna] = 3  # Item (cadeira)

        imprimir_mapa_gui()  # Atualiza a tela com o mapa alterado
        atualizar_titulo()  # Atualiza o título da janela

# Função para adicionar uma cadeira (item) na célula selecionada
def adicionar_cadeira():
    linha, coluna = obter_posicao_usuario()
    if linha is not None and coluna is not None:
        mapa[linha][coluna] = 3  # Coloca uma cadeira (item) na célula
        imprimir_mapa_gui()  # Atualiza a interface gráfica
        atualizar_titulo()  # Atualiza o título da janela

# Função para remover uma cadeira (item) na célula selecionada
def remover_cadeira():
    linha, coluna = obter_posicao_usuario()
    if linha is not None and coluna is not None:
        mapa[linha][coluna] = 0  # Remove a cadeira (coloca espaço vazio)
        imprimir_mapa_gui()  # Atualiza a interface gráfica
        atualizar_titulo()  # Atualiza o título da janela

# Função para obter a posição da célula selecionada pelo usuário
def obter_posicao_usuario():
    # Pede ao usuário para escolher a linha e coluna da célula
    linha = simpledialog.askinteger("Escolher linha", "Digite o número da linha (0-4):", minvalue=0, maxvalue=4)
    if linha is None:
        return None, None  # Caso o usuário cancele ou insira um valor inválido
    coluna = simpledialog.askinteger("Escolher coluna", "Digite o número da coluna (0-4):", minvalue=0, maxvalue=4)
    if coluna is None:
        return None, None  # Caso o usuário cancele ou insira um valor inválido
    return linha, coluna

# Função para atualizar o título da janela
def atualizar_titulo():
    # Conta quantos itens (cadeiras) estão no mapa
    total_cadeiras = sum(row.count(3) for row in mapa)
    root.title(f"Editor de Mapa - {total_cadeiras} Cadeiras")

# Criando o mapa inicial (5x5)
mapa = [
    [1, 1, 1, 1, 1],  # Paredes
    [1, 0, 0, 0, 1],  # Espaço vazio
    [1, 0, 2, 0, 1],  # Porta
    [1, 0, 3, 0, 1],  # Item (cadeira)
    [1, 1, 1, 1, 1]   # Paredes
]

# Exibe o mapa inicial no console
print("Mapa Inicial:")
imprimir_mapa(mapa)

# Configuração da interface gráfica com Tkinter
root = tk.Tk()
root.title("Editor de Mapa - 1 Cadeira")  # Inicializa com o título mostrando 1 cadeira

frame_mapa = tk.Frame(root)
frame_mapa.pack(padx=10, pady=10)

# Botões para adicionar ou remover cadeiras
botao_adicionar_cadeira = tk.Button(root, text="Adicionar Cadeira", command=adicionar_cadeira)
botao_adicionar_cadeira.pack(pady=5)

botao_remover_cadeira = tk.Button(root, text="Remover Cadeira", command=remover_cadeira)
botao_remover_cadeira.pack(pady=5)

# Função de inicialização para mostrar o mapa
imprimir_mapa_gui()

# Rodar o aplicativo gráfico
root.mainloop()
