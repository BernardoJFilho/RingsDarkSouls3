import csv
import os
import sys
from prettytable import PrettyTable

NOME_ARQUIVO = 'allRings.csv'
NOME_CORRETO = 'admin'

def buscar_elementos():
    termo_busca = input("Digite o termo que deseja buscar nos elementos da tabela (mostrado na linha 1): ").strip().lower()
    caminho_csv = obter_caminho_csv()

    try:
        with open(caminho_csv, newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv, delimiter=',')
            tabela_encontrada = PrettyTable(['Coluna 1', 'Coluna 2'])

            for linha in leitor_csv:
                if termo_busca in linha[1].strip().lower():
                    tabela_encontrada.add_row(linha)

            if len(tabela_encontrada._rows) > 0:
                print(f"Elementos encontrados para '{termo_busca}':")
                print(tabela_encontrada)
            else:
                print(f"Nenhum elemento encontrado para '{termo_busca}'.")

    except FileNotFoundError:
        print(f"Arquivo '{NOME_ARQUIVO}' não encontrado.")
    except Exception as e:
        print(f"Erro ao abrir arquivo CSV: {e}")

def obter_caminho_csv():
    if getattr(sys, 'frozen', False):
        diretorio_executavel = sys._MEIPASS
    else:
        diretorio_executavel = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(diretorio_executavel, NOME_ARQUIVO)

def renderizar_tabela(opcao):
    caminho_csv = obter_caminho_csv()

    try:
        with open(caminho_csv, newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv, delimiter=',')
            tabela = PrettyTable(['Acquired', 'Ring'])

            primeira_linha = True
            for linha in leitor_csv:
                if primeira_linha:
                    primeira_linha = False
                    continue

                if opcao == 'completa' or (opcao == 'sem x' and linha[0].strip().lower() != 'x'):
                    if len(linha[1]) > 0:
                        tabela.add_row(linha)

            print(tabela)

    except FileNotFoundError:
        print(f"Arquivo '{NOME_ARQUIVO}' não encontrado.")
    except Exception as e:
        print(f"Erro ao abrir arquivo CSV: {e}")

def marcar_desmarcar_elemento(marcar=True):
    acao = "marcar" if marcar else "desmarcar"
    mensagem_alvo = "com 'x'" if marcar else "sem 'x'"
    while True:
        nome_alvo = input(f"Digite o nome que deseja {acao} {mensagem_alvo} (mostrado na linha 1), ou 'sair' para voltar: ").strip().lower()

        if nome_alvo == 'sair':
            break

        linhas = ler_linhas_csv()
        alterado = False

        for linha in linhas:
            if linha[1].strip().lower() == nome_alvo:
                linha[0] = 'x' if marcar else ''
                print(f"Nome '{nome_alvo}' {acao}do com sucesso.")
                alterado = True
                break

        if not alterado:
            print(f"Nome '{nome_alvo}' não encontrado.")

        escrever_linhas_csv(linhas)

def ler_linhas_csv():
    with open(NOME_ARQUIVO, 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=',')
        return list(leitor_csv)

def escrever_linhas_csv(linhas):
    with open(NOME_ARQUIVO, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv, delimiter=',')
        for linha in linhas:
            escritor_csv.writerow(linha)

def menu_principal():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Pesquisar elementos")
        print("2. Mostrar tabela completa")
        print("3. Marcar elemento com 'x'")
        print("4. Desmarcar elemento")
        print("5. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            buscar_elementos()
        elif escolha == '2':
            opcao_renderizar = input("Deseja renderizar a tabela completa ou as que não têm 'x' na linha 0? "
                                     "(Digite 'completa' ou 'sem x'): ")
            renderizar_tabela(opcao_renderizar.lower())
        elif escolha == '3':
            marcar_desmarcar_elemento(marcar=True)
        elif escolha == '4':
            marcar_desmarcar_elemento(marcar=False)
        elif escolha == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, digite um número de 1 a 5.")

def main():
    usuario = input("Digite seu nome: ")

    if usuario.lower() == NOME_CORRETO:
        menu_principal()
    else:
        print("Nome incorreto. Acesso negado.")

if __name__ == "__main__":
    main()
