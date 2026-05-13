import sys
from pathlib import Path

CAMINHO_SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.append(str(CAMINHO_SRC))

from core.paciente import Paciente
from core.lista_encadeada import ListaEncadeada


def test_inserir_e_buscar_paciente():
    lista = ListaEncadeada()
    paciente = Paciente(1, "Ana", 32)

    lista.inserir(paciente)

    assert lista.buscar(1) == paciente


def test_buscar_em_lista_vazia():
    lista = ListaEncadeada()

    assert lista.buscar(99) is None


def test_buscar_com_multiplos_pacientes():
    lista = ListaEncadeada()

    lista.inserir(Paciente(1, "Ana", 32))
    lista.inserir(Paciente(2, "Carlos", 45))
    lista.inserir(Paciente(3, "Mariana", 28))

    resultado = lista.buscar(2)

    assert resultado.nome == "Carlos"


def test_remover_paciente():
    lista = ListaEncadeada()

    lista.inserir(Paciente(1, "Ana", 32))
    lista.inserir(Paciente(2, "Carlos", 45))

    removido = lista.remover(1)

    assert removido.nome == "Ana"
    assert lista.buscar(1) is None