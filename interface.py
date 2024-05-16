import PySimpleGUI as sg

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

    