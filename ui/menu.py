#from app import *

def exibir_menu():
    print("-------- O que você deseja fazer? -------")
    print("1 - Criar agenda")
    print("2 - Listar agendas")
    print("3 - Criar um day hour")
    print("4 - Editar um day hour") #Falta concertos
    print("5 - Deletar algo") #Falta colocar o que será deletado

def create_agenda_ui():
    return AgendaUseCases.create_agenda()
    print("Agenda com valores padrões criada com sucesso!")

def get_agendas_ui():
    print("Essa é uma lista com as suas agendas")
    return AgendaUseCases.get_all_agendas()

def create_day_hour_ui():
    print ("Insira o ID, Agenda ID, Dia e Hora de Começo e fim:")
    atributos = input()
    valores = atributos.split(",")
    AgendaUseCases.insert_agenda_day_hour(valores[0], valores[1], valores[2], valores[3])
    print ("Seu Day Hour foi criado com sucesso!!")

def update_day_hour_ui(): #Não tem função de Update #EDITAR DE ACORDO COM A FUNÇÃO CRIADA
    print ("Insira os atributos que a função tem")
    atributos = input()
    valores = atributos.split(",")
    AgendaUseCases.insert_agenda_day_hour(valores[0], valores[1], valores[2], valores[3]) #preencha até a quantidade de atributos
    print ("Seu Day Hour foi atualizado com sucesso!!")

def delete_ui(): #Não tem função de deletar #Tem que criar uma que receberá o id
    atributo = input("Insira o ID: ")
    AgendaUseCases.delete(id)
    print("Deletado com sucesso")

def menu():
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        opcoes = {"1": create_agenda_ui, "2": get_agendas_ui, "3": create_day_hour_ui, "4" : update_day_hour_ui, "5" : delete_ui}
        if escolha in opcoes:
            opcoes[escolha]()
        else:
            print("Opção inválida")