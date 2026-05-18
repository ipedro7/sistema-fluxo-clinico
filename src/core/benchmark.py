import time
import random

from core.paciente import Paciente
from core.ordenacao import bubble_sort, insertion_sort, selection_sort, quick_sort, merge_sort

def gerar_paciente(quantidade):
    paciente = []
    nomes = ["Andrea", "Pedro", "Wendel", "Cleber", "Verstappen", "Ryan", "Renata"]

    for i in range(quantidade):
        nome = random.choice(nomes)
        idade = random.randint(1, 100)
        paciente.append(Paciente(i, nome, idade))

    return paciente

def executar_benchmark():
    quantidades = [100, 1000, 5000]
    algoritmos = {
        "Bubble Sort: ": bubble_sort,
        "Insertion sort: ": insertion_sort,
        "Selection sort: ": selection_sort,
        "Quick sort: ": quick_sort,
        "Merge sort: ": merge_sort,
    }

    resultados = {}

    for qtd in quantidades:
        pacientes = gerar_paciente(qtd)
        resultados[qtd] = {}

        for nome_algo, funcao in algoritmos.items():
            copia = pacientes[:]

            inicio = time.perf_counter()
            funcao(copia, "id")
            fim = time.perf_counter()

            resultados[qtd][nome_algo] = fim - inicio
    return resultados

