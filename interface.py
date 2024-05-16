import PySimpleGUI as sg
import os
import sqlite3

diretorio_corrente = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(diretorio_corrente, 'database.db')

conexao = sqlite3.connect(db_path)
query = ('''CREATE TABLE IF NOT EXISTS SUPLEMENTO (LOTE CHAR(10), PRODUTO TEXT, FORNECEDOR TEXT)''')
conexao.execute(query)
conexao.close()

dados=[]
Titulos = ['Lote', 'Produtos', 'Fornecedor']

layout = [
            [sg.Text(Titulos[0]), sg.Input(size=5, key=Titulos[0])],
            [sg.Text(Titulos[0]), sg.Input(size=20, key=Titulos[1])],
            [sg.Text(Titulos[0]), sg.Combo(['Fornecedor 1', 'Fornecedor 2', 'Fornecedor 3'], key=Titulos[2])],
            [sg.Button('Adicionar'), sg.Button('Editar'), sg.Button('Salvar', disabled=True), sg.Button('Excluir'), sg.Exit('Sair')],
            [sg.Table(dados, Titulos, key='tabela')]
]

window = sg.Window('Sistema de gerencia de suplementos', layout)

while True:

    event, values = window.read()
    print(values)

    if event == 'Adicionar':
        dados.append([values[Titulos[0]], values[Titulos[1]], values[Titulos[2]]])
        window['tabela'].update(values=dados)
        for i in range(3): # Limpa as caixas de texto
            window[Titulos[i]].update(values='')

        ### Inclusos ###
        conexao = sqlite3.connect(db_path)
        conexao.execute("INSERT INTO SUPLEMENTO (LOTE, PRODUTO, FORNECEDOR) VALUES (?,?,?)", ([values[Titulos[0]], values]))
        conexao.commit()
        conexao.close()
        