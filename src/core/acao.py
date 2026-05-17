from datetime import datetime;

class Acao:
    def __init__(self, tipo, paciente):
        self.tipo = tipo
        self.paciente = paciente
        self.timestamp = datetime.now().strftime("%H:%M:%S")   
        self.proximo = None

    def __str__(self):
        return f"[{self.timestamp}] {self.tipo} - {self.paciente.nome}"

    def __repr__(self):
        return self.__str__()


