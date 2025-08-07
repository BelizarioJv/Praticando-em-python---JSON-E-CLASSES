import functions

doList = []

while True:
    print("-"*15)
    print("TO DO LIST")
    print("-"*15)
    print("1-ADICIONAR TAREFA")
    print("2-RETIRAR TAREFA")
    print("3-REFAZER TAREFA")
    print("4-VER LISTA DE TAREFAS")
    print("4-SAIR DO PROGRAMA")

    whichOperation = int(input("Qual operacao deseja realizar? : (1,2,3,4)"))
    match whichOperation:   
        case 1 :
            functions.addTask(doList)
        case 2:
            oldList, removingTask=functions.removeTask(doList)
        case 3:
            oldList = functions.redoTask(removingTask,oldList)
        case 4 :
            print(doList)
        case 5:
            print("Saindo do programa.....")
            break
        case _ :
            print("Dgito invalido")