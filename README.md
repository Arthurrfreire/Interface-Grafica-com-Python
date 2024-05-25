# Sistema de Gerenciamento de Suplementos

Este projeto em Python com PySimpleGUI oferece uma interface gráfica para gerenciar informações sobre suplementos, incluindo lote, produto e fornecedor. Os dados são armazenados em um banco de dados SQLite para persistência.

## Tecnologias Utilizadas
**Python:** Linguagem de programação utilizada para desenvolver a lógica do sistema e a interface gráfica.

**PySimpleGUI:** Biblioteca Python que facilita a criação de interfaces gráficas de usuário (GUI) de forma rápida e intuitiva.

**SQLite:** Sistema de gerenciamento de banco de dados relacional leve e embutido, utilizado para armazenar os dados dos suplementos.

## Funcionalidades

- **Adicionar:** Insere um novo suplemento com lote, produto e fornecedor.
- **Editar:** Modifica os dados de um suplemento existente.
- **Salvar:** Confirma as alterações feitas durante a edição.
- **Excluir:** Remove um suplemento do banco de dados.
- **Visualização em Tabela:** Exibe todos os suplementos cadastrados em uma tabela organizada.

## Pré-requisitos

- Python 3.x
- PySimpleGUI (`pip install PySimpleGUI`)
- SQLite3 (geralmente incluído com o Python)

## Como Usar

1. **Clone o Repositório:**
   ```bash
   git clone [https://github.com/Arthurrfreire/Interface-Grafica-com-Python.git](https://github.com/Arthurrfreire/Interface-Grafica-com-Python.git)
   
2. **Execute o Script:**
    ```bash
    python interface.py

## Interface Gráfica:

Preencha os campos "Lote", "Produto" e selecione o "Fornecedor".

Clique em "Adicionar" para inserir um novo suplemento.

Selecione uma linha na tabela e clique em "Editar" para modificar os dados.

Após editar, clique em "Salvar" para confirmar as alterações.

Selecione uma linha e clique em "Excluir" para remover o suplemento.

## Estrutura do Projeto
interface.py: Arquivo principal contendo o código da interface gráfica e a lógica de interação com o banco de dados.

database.db: Arquivo do banco de dados SQLite que armazena os dados dos suplementos.

## Observações
Certifique-se de que o arquivo database.db esteja no mesmo diretório do script Python.

O código inclui tratamento básico de erros, mas pode ser expandido para maior robustez.

A interface gráfica é simples e pode ser personalizada com mais recursos e estilos visuais.
