# Arquivo: src/core/fila.py
# Essa fila vai controlar a ordem de atendimento dos pacientes.
# Ela funciona no esquema FIFO:
# o primeiro que entra é o primeiro que sai.


class NoFila:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def enqueue(self, paciente):
        # enqueue = colocar no final da fila
        novo = NoFila(paciente)

        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

        self.tamanho += 1

    def dequeue(self):
        # dequeue = remover do começo da fila
        if self.esta_vazia():
            return None

        paciente = self.inicio.dado
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        self.tamanho -= 1
        return paciente

    def remover_por_id(self, id_paciente):
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.dado.id_paciente == id_paciente:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                
                if atual.proximo is None:
                    self.fim = anterior

                if self.inicio is None:
                    self.fim = None

                self.tamanho -= 1
                return atual.dado

            anterior = atual
            atual = atual.proximo

        return None

    def frente(self):
        # Mostra quem é o próximo sem tirar da fila
        if self.esta_vazia():
            return None

        return self.inicio.dado

    def exibir(self):
        pacientes = []
        atual = self.inicio

        while atual is not None:
            pacientes.append(atual.dado)
            atual = atual.proximo

        return pacientes

    def quantidade(self):
        return self.tamanho