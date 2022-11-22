from chatterbot import ChatBot
from difflib import SequenceMatcher
#from chatterbot.comparisons import levenshtein_distance
#from chatterbot.response_selection import get_first_response

ACEITACAO = 0.70

def comparar_mensagens(mensagem, mensagem_candidata):
    confianca = 0.0

    if mensagem.text and mensagem_candidata.text:
        texto_mensagem = mensagem.text
        texto_mensagem_candidata = mensagem_candidata.text

        confianca = SequenceMatcher(
            None,
            texto_mensagem,
            texto_mensagem_candidata
        )
        confianca = round(confianca.ratio(), 2)
        if confianca < ACEITACAO:
            confianca = 0.0
        else:
            print("mensagem do usuário:", texto_mensagem, ", mensagem candidata:", mensagem_candidata, ", nível de confiança", confianca)
    return confianca

def selecionar_resposta(mensagem, lista_respostas, storage=None):
    resposta = lista_respostas[0]
    print("resposta:", resposta)
    return resposta

def executar_robo():
    covid19_bot = ChatBot("Robô de atendimento da covid-19")

    while True:
        entrada = input("digite algo...\n")
        resposta = covid19_bot.get_response(entrada)
        if resposta.confidence > 0.0:
            print(resposta.text)
        else:
            print("ainda não sei responder essa pergunta")
            print("pergunte outra coisa...\n")

if __name__ == "__main__":
    executar_robo()
