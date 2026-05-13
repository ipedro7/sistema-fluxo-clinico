import sys
from pathlib import Path

CAMINHO_SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.append(str(CAMINHO_SRC))

from core.ordenacao import selection_sort, insertion_sort, quick_sort
from core.paciente import Paciente


def test_selection_sort_basico():
    dados = [5, 3, 1, 4, 2]

    resultado = selection_sort(dados)

    assert resultado == [1, 2, 3, 4, 5]


def test_insertion_sort_basico():
    dados = [8, 4, 6, 2, 1]

    resultado = insertion_sort(dados)

    assert resultado == [1, 2, 4, 6, 8]


def test_quick_sort_basico():
    dados = [10, 7, 8, 9, 1, 5]

    resultado = quick_sort(dados)

    assert resultado == [1, 5, 7, 8, 9, 10]


def test_lista_vazia():
    dados = []

    assert selection_sort(dados) == []
    assert insertion_sort(dados) == []
    assert quick_sort(dados) == []


def test_ordenar_pacientes_por_id():
    pacientes = [
        Paciente(3, "Mariana", 28),
        Paciente(1, "Ana", 32),
        Paciente(2, "Carlos", 45),
    ]

    resultado = selection_sort(pacientes, "id")

    assert resultado[0].id == 1
    assert resultado[1].id == 2
    assert resultado[2].id == 3


def test_ordenar_pacientes_por_idade():
    pacientes = [
        Paciente(1, "Ana", 32),
        Paciente(2, "Carlos", 45),
        Paciente(3, "Mariana", 28),
    ]

    resultado = insertion_sort(pacientes, "idade")

    assert resultado[0].nome == "Mariana"
    assert resultado[1].nome == "Ana"
    assert resultado[2].nome == "Carlos"