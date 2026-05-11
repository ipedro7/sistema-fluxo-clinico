# Arquivo: src/core/pilha.py
# Essa pilha vai guardar o histórico de ações recentes.
# Ela funciona no esquema LIFO:
# a última ação feita é a primeira que aparece no topo.


class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def push(self, acao):
        # push = empilhar uma nova ação
        self.itens.append(acao)

    def pop(self):
        # pop = remover a última ação
        if self.esta_vazia():
            return None

        return self.itens.pop()

    def peek(self):
        # peek = ver a última ação sem remover
        if self.esta_vazia():
            return None

        return self.itens[-1]

    def exibir(self):
        # Mostra do mais recente para o mais antigo
        return list(reversed(self.itens))

    def quantidade(self):
        return len(self.itens)