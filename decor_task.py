from datetime import datetime

def make_trace(old_function):
    def new_function(*args):
        time = datetime.now()
        arguments = args*2
        with open('file_for_task.log', 'a') as file:
            file.write(f'Имя функции: {old_function.__name__}. \nАргументы умноженные на 2: {arguments}. \nДата и время вызова: {time}\n\n')
    return new_function

@make_trace
def task(a,b):
    return 'test'

task("Тест", "Тест2")
