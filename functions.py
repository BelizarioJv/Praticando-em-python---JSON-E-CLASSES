def addTask(lista):
    print(f"Sua lista de tarefas : {lista}")
    task = input("Digite a tarefa que deseja realizar")
    lista.append(task)
    return lista 

def removeTask(lista):
    print(f"Sua lista de tarefas : {lista}")
    task = input("Digite o nome da tarefa que deseja retirar da sua lista de tarefas: ")
    if task in lista :
        lastRemoved = task
        lista.remove(task)
    else:
        print(f"A tarefa {task} nao esta em sua lista de tarefas")
    return lista , lastRemoved

def redoTask (lastRemoved,lista):
    print(lista)
    reallyDo = input(f"Deseja refazer a tarefa {lastRemoved} ? (S(sim) N(nao))").strip().upper()
    if reallyDo == "S":
        lista.append(lastRemoved)
    elif reallyDo == "N":
        pass
    else:
        print("Digito invalido")
    return lista