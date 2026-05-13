# Arquivo: src/core/ordenacao.py
# Aqui ficam os algoritmos de ordenação.
# A ideia é ordenar pacientes por id, nome ou idade.

def pegar_valor(item, campo=None):
    # Se não tiver campo, compara o próprio item.
    # Isso serve para listas simples, tipo [6, 7, 6, 7].
    if campo is None:
        return item

    # Se for paciente, pega o campo escolhido.
    if campo == "id":
        return item.id

    if campo == "nome":
        return item.nome.lower()

    if campo == "idade":
        return item.idade

    return item


def selection_sort(dados, campo=None):
    # Selection Sort:
    # procura o menor elemento e troca com a posição atual.
    # Complexidade: O(n²)

    lista = dados[:]
    tamanho = len(lista)

    for i in range(tamanho):
        menor = i

        for j in range(i + 1, tamanho):
            if pegar_valor(lista[j], campo) < pegar_valor(lista[menor], campo):
                menor = j

        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]

    return lista


def insertion_sort(dados, campo=None):
    # Insertion Sort:
    # pega um item e coloca ele na posição certa
    # dentro da parte que já está ordenada.
    # Melhor caso: O(n)
    # Pior caso: O(n²)

    lista = dados[:]

    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        while j >= 0 and pegar_valor(lista[j], campo) > pegar_valor(atual, campo):
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = atual

    return lista


def quick_sort(dados, campo=None):
    # Quick Sort:
    # escolhe um pivô, separa os menores e maiores,
    # e ordena cada lado.
    # Caso médio: O(n log n)
    # Pior caso: O(n²)

    lista = dados[:]

    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2]

    menores = []
    iguais = []
    maiores = []

    for item in lista:
        if pegar_valor(item, campo) < pegar_valor(pivo, campo):
            menores.append(item)
        elif pegar_valor(item, campo) > pegar_valor(pivo, campo):
            maiores.append(item)
        else:
            iguais.append(item)

    return quick_sort(menores, campo) + iguais + quick_sort(maiores, campo)
