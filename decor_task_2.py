from datetime import datetime

def make_trace(old_function): #paht
    def new_function(path2):
        time = datetime.now()

        with open(f'{path2}', 'a') as file:
            file.write(f'Имя функции: {old_function.__name__}. \nДата и время вызова: {time}\n')
    return new_function

@make_trace
def task(path):
    return 'test'

task('TASK_2.log')
