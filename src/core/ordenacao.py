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

def bubble_sort(dados, campo=None):
    # Bubble Sort:
    # compara os itens lado a lado
    # e troca quando estão fora de ordem.
    # Complexidade: O(n²)

    lista = dados[:]
    tamanho = len(lista)

    for i in range(tamanho - 1):
        houve_troca = False

        for j in range(tamanho - 1 - i):
            if pegar_valor(lista[j], campo) > pegar_valor(lista[j + 1], campo):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                houve_troca = True

        # Se não aconteceu nenhuma troca,
        # a lista já está ordenada
        if not houve_troca:
            break

    return lista


def merge_sort(dados, campo=None):
    # Merge Sort:
    # divide a lista em partes menores,
    # ordena cada parte e depois junta tudo.
    # Complexidade: O(n log n)

    lista = dados[:]

    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    esquerda = merge_sort(lista[:meio], campo)
    direita = merge_sort(lista[meio:], campo)

    return juntar_listas(esquerda, direita, campo)


def juntar_listas(esquerda, direita, campo=None):
    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if pegar_valor(esquerda[i], campo) <= pegar_valor(direita[j], campo):
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1

    while j < len(direita):
        resultado.append(direita[j])
        j += 1

    return resultado
