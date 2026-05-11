# Arquivo: src/core/lista_encadeada.py
# Aqui fica a lista encadeada simples.
# Ela vai guardar os pacientes cadastrados.


class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.primeiro is None

    def inserir(self, paciente):
        # Cria um novo nó guardando o paciente
        novo = No(paciente)

        # Se a lista estiver vazia, o novo nó vira o primeiro
        if self.primeiro is None:
            self.primeiro = novo
            self.tamanho += 1
            return

        # Se já tiver gente na lista, percorre até o final
        atual = self.primeiro

        while atual.proximo is not None:
            atual = atual.proximo

        # Liga o último nó ao novo nó
        atual.proximo = novo
        self.tamanho += 1

    def buscar(self, id_paciente):
        atual = self.primeiro

        while atual is not None:
            if atual.dado.id == int(id_paciente):
                return atual.dado

            atual = atual.proximo

        return None

    def remover(self, id_paciente):
        if self.primeiro is None:
            return None

        id_paciente = int(id_paciente)

        # Caso o paciente esteja no primeiro nó
        if self.primeiro.dado.id == id_paciente:
            paciente_removido = self.primeiro.dado
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1
            return paciente_removido

        anterior = self.primeiro
        atual = self.primeiro.proximo

        while atual is not None:
            if atual.dado.id == id_paciente:
                paciente_removido = atual.dado
                anterior.proximo = atual.proximo
                self.tamanho -= 1
                return paciente_removido

            anterior = atual
            atual = atual.proximo

        return None

    def exibir(self):
        pacientes = []
        atual = self.primeiro

        while atual is not None:
            pacientes.append(atual.dado)
            atual = atual.proximo

        return pacientes

    def quantidade(self):
        return self.tamanho