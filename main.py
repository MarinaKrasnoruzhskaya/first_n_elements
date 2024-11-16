from src.utils import get_n_elements


def main():

    while True:
        n = int(input('Введите n= '))

        if n > 0:
            print(f"Первые {n} элемента(ов) последовательности: {get_n_elements(n)}")
        else:
            print("n должен быть положительным числом")

        choice = input("Продолжить? (y/n): ")

        if choice.lower() != "y":
            break


if "__main__" == __name__:
    main()
