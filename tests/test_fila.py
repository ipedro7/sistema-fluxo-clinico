# Arquivo: tests/test_fila.py
import sys
from pathlib import Path

CAMINHO_SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.append(str(CAMINHO_SRC))

from core.paciente import Paciente
from core.fila import Fila


def test_enqueue_dequeue():
    fila = Fila()
    paciente = Paciente(1, "Ana", 32)

    fila.enqueue(paciente)

    assert fila.dequeue() == paciente


def test_dequeue_fila_vazia():
    fila = Fila()

    assert fila.dequeue() is None


def test_fila_fifo_multiplos_pacientes():
    fila = Fila()

    p1 = Paciente(1, "Ana", 32)
    p2 = Paciente(2, "Carlos", 45)
    p3 = Paciente(3, "Mariana", 28)

    fila.enqueue(p1)
    fila.enqueue(p2)
    fila.enqueue(p3)

    assert fila.dequeue() == p1
    assert fila.dequeue() == p2
    assert fila.dequeue() == p3


def test_frente_nao_remove():
    fila = Fila()

    p1 = Paciente(1, "Ana", 32)
    fila.enqueue(p1)

    assert fila.frente() == p1
    assert fila.quantidade() == 1