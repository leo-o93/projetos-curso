tasks = []

def show_menu():
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")

def add_task():
    task = input("Digite a nova tarefa: ")
    tasks.append(task)
    print("Tarefa adicionada com sucesso!")

def list_tasks():
    if not tasks:
        print("Nenhuma tarefa adicionada ainda.")
    else:
        print("\nTarefas:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task():
    list_tasks()
    try:
        task_num = int(input("Digite o número da tarefa a ser removida: "))
        removed = tasks.pop(task_num - 1)
        print(f"Tarefa '{removed}' removida com sucesso!")
    except (IndexError, ValueError):
        print("Número inválido. Tente novamente.")

while True:
    show_menu()
    choice = input("Escolha uma opção: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
