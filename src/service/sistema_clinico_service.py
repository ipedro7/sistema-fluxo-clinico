# Arquivo: src/service/sistema_clinico_service.py
# Esse arquivo é a camada de serviço.
# Ele junta as estruturas e organiza as ações do sistema.

from core.paciente import Paciente
from core.lista_encadeada import ListaEncadeada
from core.fila import Fila
from core.pilha import Pilha
from core.ordenacao import (
    selection_sort,
    insertion_sort,
    quick_sort,
    bubble_sort,
    merge_sort,
)


class SistemaClinicoService:
    def __init__(self):
        self.pacientes = ListaEncadeada()
        self.fila = Fila()
        self.historico = Pilha()

    def cadastrar_paciente(self, id_paciente, nome, idade):
        if nome.strip() == "":
            return False, "ERRO: o nome não pode ficar vazio."

        paciente_existente = self.pacientes.buscar(id_paciente)

        if paciente_existente is not None:
            return False, "ERRO: já existe um paciente com esse ID."

        paciente = Paciente(id_paciente, nome, idade)
        self.pacientes.inserir(paciente)

        self.historico.push(f"Paciente {paciente.nome} cadastrado")

        return True, f"Paciente {paciente.nome} cadastrado com sucesso."

    def listar_pacientes(self):
        return self.pacientes.exibir()

    def buscar_paciente(self, id_paciente):
        return self.pacientes.buscar(id_paciente)

    def remover_paciente(self, id_paciente):
        paciente = self.pacientes.remover(id_paciente)

        if paciente is None:
            return False, "ERRO: paciente não encontrado."

        self.historico.push(f"Paciente {paciente.nome} removido do cadastro")
        return True, f"Paciente {paciente.nome} removido com sucesso."

    def adicionar_paciente_na_fila(self, id_paciente):
        paciente = self.pacientes.buscar(id_paciente)

        if paciente is None:
            return False, "ERRO: paciente não encontrado no cadastro."

        self.fila.enqueue(paciente)
        self.historico.push(f"Paciente {paciente.nome} entrou na fila")

        return True, f"Paciente {paciente.nome} adicionado à fila."

    def ver_proximo_paciente(self):
        return self.fila.frente()

    def chamar_proximo_paciente(self):
        paciente = self.fila.dequeue()

        if paciente is None:
            return False, "ERRO: fila vazia. Não há pacientes para chamar."

        self.historico.push(f"Paciente {paciente.nome} chamado para atendimento")

        return True, f"Próximo paciente chamado: {paciente.nome}."

    def ver_fila(self):
        return self.fila.exibir()

    def ver_historico(self):
        return self.historico.exibir()

    def ver_ultima_acao(self):
        return self.historico.peek()

    def remover_ultima_acao_do_historico(self):
        acao = self.historico.pop()

        if acao is None:
            return False, "ERRO: histórico vazio. Não há ação para remover."

        return True, f"Última ação removida do histórico: {acao}"

    def carregar_pacientes_do_arquivo(self, caminho):
        carregados = 0
        erros = []

        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                for numero_linha, linha in enumerate(arquivo, start=1):
                    linha = linha.strip()

                    if linha == "":
                        continue

                    partes = linha.split(";")

                    if len(partes) != 3:
                        erros.append(f"Linha {numero_linha}: formato inválido")
                        continue

                    id_paciente = partes[0]
                    nome = partes[1]
                    idade = partes[2]

                    if self.pacientes.buscar(id_paciente) is not None:
                        erros.append(f"Linha {numero_linha}: ID repetido")
                        continue

                    paciente = Paciente(id_paciente, nome, idade)
                    self.pacientes.inserir(paciente)
                    carregados += 1

            if carregados > 0:
                self.historico.push(f"{carregados} pacientes carregados do arquivo")

            return True, carregados, erros

        except FileNotFoundError:
            return False, 0, ["Arquivo não encontrado. Verifique se data/pacientes.txt existe."]

    def ordenar_pacientes(self, campo, algoritmo):
        lista = self.pacientes.exibir()

        if len(lista) == 0:
            return False, "Não há pacientes cadastrados para ordenar.", []

        try:
            if algoritmo == "selection":
                ordenados = selection_sort(lista, campo)
            elif algoritmo == "insertion":
                ordenados = insertion_sort(lista, campo)
            elif algoritmo == "quick":
                ordenados = quick_sort(lista, campo)
            elif algoritmo == "bubble":
                ordenados = bubble_sort(lista, campo)
            elif algoritmo == "merge":
                ordenados = merge_sort(lista, campo)
            else:
                return False, "Algoritmo inválido.", []

            self.historico.push(f"Relatório ordenado por {campo} usando {algoritmo}")

            return True, "Pacientes ordenados com sucesso.", ordenados

        except NotImplementedError as erro:
            return False, str(erro), []

    def dashboard(self):
        total_pacientes = self.pacientes.quantidade()
        total_fila = self.fila.quantidade()
        total_historico = self.historico.quantidade()

        if total_fila <= 5:
            status_fila = "NORMAL"
        elif total_fila <= 10:
            status_fila = "ATENÇÃO"
        else:
            status_fila = "CRÍTICO"

        if total_historico <= 10:
            status_historico = "NORMAL"
        else:
            status_historico = "ATENÇÃO"

        return {
            "pacientes": total_pacientes,
            "fila": total_fila,
            "historico": total_historico,
            "status_fila": status_fila,
            "status_historico": status_historico,
        }