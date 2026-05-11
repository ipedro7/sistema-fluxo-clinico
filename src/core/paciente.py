# Arquivo: src/core/paciente.py
# Essa classe representa um paciente do sistema.
# Eu deixei simples mesmo: id, nome e idade.


class Paciente:
    def __init__(self, id, nome, idade):
        self.id = int(id)
        self.nome = nome
        self.idade = int(idade)

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Idade: {self.idade}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, outro):
        if not isinstance(outro, Paciente):
            return False

        return self.id == outro.id