# Arquivo: src/ui/main.py
# Esse é o menu principal do sistema.
# A interface vai ser no terminal mesmo.

import sys
from pathlib import Path

# Essa parte ajuda o Python a encontrar a pasta src
CAMINHO_SRC = Path(__file__).resolve().parents[1]
sys.path.append(str(CAMINHO_SRC))

from service.sistema_clinico_service import SistemaClinicoService


def mostrar_linha():
    print("-" * 45)


def pausar():
    input("\nAperte ENTER para continuar...")


def mostrar_pacientes(pacientes):
    if len(pacientes) == 0:
        print("Nenhum paciente para mostrar.")
        return

    for paciente in pacientes:
        print(paciente)

menu = """
    |=============================================|
    |    SISTEMA DE GESTÃO DE FLUXO CLÍNICO       |
    |=============================================|
    |                                             |
    |   [1] Cadastrar paciente                    |
    |   [2] Listar pacientes cadastrados          |
    |   [3] Buscar paciente por ID                |
    |   [4] Remover paciente do cadastro          |
    |   [5] Adicionar paciente à fila             |
    |   [6] Ver próximo paciente da fila          |
    |   [7] Chamar próximo paciente               |
    |   [8] Ver fila atual                        |
    |   [9] Ver histórico de ações                |
    |   [10] Desfazer ultima ação                 |
    |   [11] Carregar pacientes do arquivo        |
    |   [12] Ordenar pacientes para relatório     |
    |   [13] Dashboard de desempenho              |
    |   [0] Sair                                  |
    |                                             |
    |=============================================|
"""

def tela_cadastrar(service):
    print("\n=== Cadastro de Paciente ===")

    try:
        id_paciente = int(input("Informe o ID do paciente: "))
        nome = input("Informe o nome do paciente: ")
        idade = int(input("Informe a idade do paciente: "))

        confirmar = input("Confirmar cadastro? [s/n]: ").lower()

        if confirmar != "s":
            print("Cadastro cancelado.")
            return

        sucesso, mensagem = service.cadastrar_paciente(id_paciente, nome, idade)
        print(mensagem)

    except ValueError:
        print("ERRO: ID e idade precisam ser números.")


def tela_listar(service):
    print("\n=== Pacientes Cadastrados ===")
    pacientes = service.listar_pacientes()
    mostrar_pacientes(pacientes)


def tela_buscar(service):
    print("\n=== Buscar Paciente ===")

    try:
        id_paciente = int(input("Informe o ID do paciente: "))
        paciente = service.buscar_paciente(id_paciente)

        if paciente is None:
            print("Paciente não encontrado.")
        else:
            print("Paciente encontrado:")
            print(paciente)

    except ValueError:
        print("ERRO: o ID precisa ser um número.")


def tela_remover(service):
    print("\n=== Remover Paciente ===")

    try:
        id_paciente = int(input("Informe o ID do paciente que deseja remover: "))

        confirmar = input("Confirmar remoção? [s/n]: ").lower()

        if confirmar != "s":
            print("Remoção cancelada.")
            return

        sucesso, mensagem = service.remover_paciente(id_paciente)
        print(mensagem)

    except ValueError:
        print("ERRO: o ID precisa ser um número.")


def tela_adicionar_fila(service):
    print("\n=== Adicionar Paciente à Fila ===")

    try:
        id_paciente = int(input("Informe o ID do paciente: "))

        sucesso, mensagem = service.adicionar_paciente_na_fila(id_paciente)
        print(mensagem)

        print("\nEstado atual da fila:")
        mostrar_pacientes(service.ver_fila())

    except ValueError:
        print("ERRO: o ID precisa ser um número.")


def tela_ver_proximo(service):
    print("\n=== Próximo Paciente da Fila ===")

    paciente = service.ver_proximo_paciente()

    if paciente is None:
        print("A fila está vazia.")
    else:
        print("Próximo paciente:")
        print(paciente)


def tela_chamar_proximo(service):
    print("\n=== Chamar Próximo Paciente ===")

    sucesso, mensagem = service.chamar_proximo_paciente()
    print(mensagem)

    print("\nEstado atual da fila:")
    mostrar_pacientes(service.ver_fila())


def tela_ver_fila(service):
    print("\n=== Fila Atual ===")
    fila = service.ver_fila()
    mostrar_pacientes(fila)


def tela_historico(service):
    print("\n=== Histórico de Ações ===")

    historico = service.ver_historico()

    if len(historico) == 0:
        print("Histórico vazio.")
        return

    for indice, acao in enumerate(historico, start=1):
        print(acao)


def tela_remover_ultima_acao(service):
    print("\n=== Remover Última Ação do Histórico ===")

    sucesso, mensagem = service.remover_ultima_acao_do_historico()
    print(mensagem)


def tela_carregar_arquivo(service):
    print("\n=== Carregar Pacientes de Arquivo ===")
    print("Arquivo esperado: data/pacientes.txt")

    confirmar = input("Deseja carregar os pacientes deste arquivo? [s/n]: ").lower()

    if confirmar != "s":
        print("Carregamento cancelado.")
        return

    sucesso, quantidade, erros = service.carregar_pacientes_do_arquivo("data/pacientes.txt")

    if sucesso:
        print(f"{quantidade} pacientes carregados com sucesso.")
    else:
        print("Não foi possível carregar o arquivo.")

    if len(erros) > 0:
        print("\nAvisos/erros encontrados:")
        for erro in erros:
            print(f"- {erro}")


def tela_ordenar(service):
    print("\n=== Ordenar Pacientes ===")
    print("Escolha o campo:")
    print("[1] ID")
    print("[2] Nome")
    print("[3] Idade")

    opcao_campo = input("Campo: ")

    if opcao_campo == "1":
        campo = "id"
    elif opcao_campo == "2":
        campo = "nome"
    elif opcao_campo == "3":
        campo = "idade"
    else:
        print("Campo inválido.")
        return

    print("\nEscolha o algoritmo:")
    print("[1] Selection Sort")
    print("[2] Insertion Sort")
    print("[3] Quick Sort")
    print("[4] Bubble Sort - parte do Wendel")
    print("[5] Merge Sort - parte do Wendel")

    opcao_algoritmo = input("Algoritmo: ")

    if opcao_algoritmo == "1":
        algoritmo = "selection"
    elif opcao_algoritmo == "2":
        algoritmo = "insertion"
    elif opcao_algoritmo == "3":
        algoritmo = "quick"
    elif opcao_algoritmo == "4":
        algoritmo = "bubble"
    elif opcao_algoritmo == "5":
        algoritmo = "merge"
    else:
        print("Algoritmo inválido.")
        return

    sucesso, mensagem, pacientes_ordenados = service.ordenar_pacientes(campo, algoritmo)

    print(mensagem)

    if sucesso:
        print("\nResultado da ordenação:")
        mostrar_pacientes(pacientes_ordenados)


def tela_dashboard(service):
    print("\n=== Dashboard de Desempenho ===")

    dados = service.dashboard()

    print(f"Pacientes cadastrados: {dados['pacientes']}")
    print(f"Pacientes aguardando na fila: {dados['fila']}")
    print(f"Ações no histórico: {dados['historico']}")
    print(f"Status da fila: {dados['status_fila']}")
    print(f"Status do histórico: {dados['status_historico']}")


def main():
    service = SistemaClinicoService()

    while True:
        print(menu)
        opcao = input("                 Escolha uma opção: ")

        mostrar_linha()

        match opcao:

            case "1":
                tela_cadastrar(service)
            case "2":
                tela_listar(service)
            case "3":
                tela_buscar(service)
            case "4":
                tela_remover(service)
            case "5":
                tela_adicionar_fila(service)
            case "6":
                tela_ver_proximo(service)
            case "7":
                tela_chamar_proximo(service)
            case "8":
                tela_ver_fila(service)
            case "9":
                tela_historico(service)
            case "10":
                tela_remover_ultima_acao(service)
            case "11":
                tela_carregar_arquivo(service)
            case "12":
                tela_ordenar(service)
            case "13":
                tela_dashboard(service)
            case "0":
                print("Programa encerrado com sucesso.")
                break
            case _:
                print("Opção inválida. Tente novamente.")

        pausar()


if __name__ == "__main__":
    main()