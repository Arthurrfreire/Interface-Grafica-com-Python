import PySimpleGUI as sg

dados=[]
Titulos = ['Lote', 'Produtos', 'Fornecedor']

layout = [
            [sg.Text(Titulos[0]), sg.Input(size=5, key=Titulos[0])],
            [sg.Text(Titulos[0]), sg.Input(size=20, key=Titulos[1])],
            [sg.Text(Titulos[0]), sg.Combo(['Fornecedor 1', 'Fornecedor 2', 'Fornecedor 3'], key=Titulos[2])],
            



]