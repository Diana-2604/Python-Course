# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы
# с разными расширениями. Расширения и количество файлов
# функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

from task1 import create_files


def file_generate(**kwargs) -> None:
    for extension, count in kwargs.items():
        create_files(extension=extension, count=count)


if __name__ == '__main__':
    file_generate(bin=2, jpg=1)
