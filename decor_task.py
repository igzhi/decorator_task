from datetime import datetime

def make_trace(old_function):
    def new_function(*args, **kwargs):
        some = old_function(*args, **kwargs)
        time = datetime.now()
        arguments = args*2
        with open('file_for_task1.log', 'a') as file:
            file.write(f'Имя функции: {old_function.__name__}. \nУдвоенное колличество аргументов: {arguments}. \nДата и время вызова: {time}\n\n')
        return some
    return new_function

@make_trace
def summator(x, y):
   return x + y

three = summator(1, 2)
five = summator(2, 3)

result = summator(three, five)

# print('result: ', result)
# print('result type: ', type(result))

