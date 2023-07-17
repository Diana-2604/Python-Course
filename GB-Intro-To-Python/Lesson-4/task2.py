# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def key_value_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            hash(key)
        except TypeError:
            key = str(key)
        result[value] = key
    return result


task_result = key_value_dict(a=1, b=2, c=3, d='apple', e='orange')
print(task_result)
