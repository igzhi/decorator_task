from datetime import datetime

def parametrized_decor(parameter):
    def decor(foo):
        def new_foo(*args, **kwars):
            time = datetime.now()
            result = foo(*args, **kwars)
            arguments = sum(arg*2 for arg in args)
            with open(f'{parameter}.log', 'a') as file:
                file.write(f'Имя функции: {foo.__name__} \nДата и время вызова: {time}\nРезультат функции до обработки: {result}\nРезультат функции ПОСЛЕ обработки:{arguments}\n')
            return result
        return new_foo
    return decor

@parametrized_decor(parameter='путь_к_логам')
def foo(x, y):
    return x + y

foo(2, 5)