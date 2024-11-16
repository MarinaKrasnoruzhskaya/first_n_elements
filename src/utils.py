def get_n_elements(n: int) -> str:
    """ Функция создает список из n элементов последовательности 122333444455555…
    и возвращает строку из этих элементов"""

    n_elements = []
    i = 1
    elements_to_add = n

    while elements_to_add > 0:
        if i < elements_to_add:
            n_elements.extend([str(i)] * i)
        else:
            n_elements.extend([str(i)] * elements_to_add)
        elements_to_add -= i
        i += 1

    return "".join(n_elements)
