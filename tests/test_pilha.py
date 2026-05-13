import sys
from pathlib import Path

CAMINHO_SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.append(str(CAMINHO_SRC))

from core.pilha import Pilha


def test_push_peek():
    pilha = Pilha()

    pilha.push("Paciente Ana cadastrado")

    assert pilha.peek() == "Paciente Ana cadastrado"


def test_pop_pilha_vazia():
    pilha = Pilha()

    assert pilha.pop() is None


def test_pilha_lifo_multiplas_acoes():
    pilha = Pilha()

    pilha.push("Ação 1")
    pilha.push("Ação 2")
    pilha.push("Ação 3")

    assert pilha.pop() == "Ação 3"
    assert pilha.pop() == "Ação 2"
    assert pilha.pop() == "Ação 1"


def test_peek_nao_remove():
    pilha = Pilha()

    pilha.push("Ação teste")

    assert pilha.peek() == "Ação teste"
    assert pilha.quantidade() == 1