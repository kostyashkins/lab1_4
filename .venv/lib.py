def count_common_elements(*lists):
    """
    Функция для подсчета количества одинаковых элементов в N списках.
    :param lists: Произвольное количество списков.
    :return: Количество одинаковых элементов.
    """
    if not lists:
        return 0

    # Находим пересечение всех списков
    common_elements = set(lists[0])
    for lst in lists[1:]:
        common_elements.intersection_update(lst)

    return len(common_elements)


# Пример использования
if __name__ == "__main__":
    list1 = [1, 2, 3, 4]
    list2 = [2, 3, 4, 5]
    list3 = [3, 4, 5, 6]

    common_count = count_common_elements(list1, list2, list3)
    print(f"Количество одинаковых элементов: {common_count}")