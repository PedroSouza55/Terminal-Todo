from pathlib import Path
import json

arquivo_tarefas = Path("tarefas.json")
if arquivo_tarefas.is_file():
    with open("tarefas.json", "r", encoding="utf-8") as arquivo:
        tarefas = json.load(arquivo)
else:
    tarefas = []
escolha = ""
def listar_tarefas(tarefas):
    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"{numero} - {tarefa}")
def validar_input(tarefa_input):
    if not tarefa_input.isdigit():
        print("Número invalido, tente novamente.")
    else:
        numero_tarefa = int(tarefa_input)
        if 1 <= numero_tarefa <= len(tarefas):
            return numero_tarefa
        else:
            print("Número fora do intervalo válido.")
while escolha != "5":
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Editar tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")
    escolha = input()
    if escolha == "1":
        tarefa = input("Digite o nome da tarefa: ")
        tarefas.append(tarefa)
    elif escolha == "2":
        for tarefa in tarefas:
            print(tarefa)
    elif escolha == "3":
        if not tarefas:
            print("A lista de tarefas está vazia.")
        else:
            listar_tarefas(tarefas)
            tarefa_input_edicao = input("Digite o número da tarefa a ser editada: ")
            numero_tarefa_edicao = validar_input(tarefa_input_edicao)
            if numero_tarefa_edicao:
                tarefa_editada = input("Digite a tarefa editada: ")
                tarefas[numero_tarefa_edicao - 1] = tarefa_editada
                print(f'Tarefa atualizada.')
    elif escolha == "4":
        if not tarefas:
            print("A lista de tarefas está vazia.")
        else:
            listar_tarefas(tarefas)
            tarefa_input_remocao = input("Digite o número da tarefa a ser removida: ")
            numero_tarefa_remocao = validar_input(tarefa_input_remocao)
            if numero_tarefa_remocao:
                tarefa_removida = tarefas.pop(numero_tarefa_remocao - 1)
                print(f'Tarefa "{tarefa_removida}" removida')
    elif escolha == "5":
        with open("tarefas.json", "w", encoding="utf-8") as arquivo:
            json.dump(tarefas, arquivo, ensure_ascii=False)
    else:
        print("Escolha inválida.")
