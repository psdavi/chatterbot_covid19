from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONFIGURACOES_CONVERSAS = [
    "conversas/saudacoes.json",
    "conversas/info_basicas.json"
]

def iniciar():
    global robo
    global treinador

    robo = ChatBot("Robô de atendimento da covid-19")
    treinador = ListTrainer(robo)

def carregar_conversas():
    conversas = []

    for arquivo_configuracao in CONFIGURACOES_CONVERSAS:
        with open(arquivo_configuracao, "r") as arquivo:
            conversas_configuradas = json.load(arquivo)
            conversas.append(conversas_configuradas["conversas"])
            arquivo.close()
    return conversas

def treinar_robo(conversas):
    global treinador

    for conversa in conversas:
        for mensagens_resposta in conversa:
            mensagens = mensagens_resposta["mensagens"]
            resposta = mensagens_resposta["resposta"]

            print("Treinando o robô para responder a: ", mensagens, "com a responsta: ", resposta)
            for mensagem in mensagens:
                treinador.train([mensagem, resposta])


if __name__ == "__main__":
    iniciar()

    conversas = carregar_conversas()
    if conversas:
        treinar_robo(conversas)



