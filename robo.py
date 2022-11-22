from chatterbot import ChatBot

def executar_robo():
    robo = ChatBot("Robô de atendimento da covid-19")
    while True:
        mensagem = input("Digite alguma coisa... \n")
        resposta = robo.get_response(mensagem.lower())
        if resposta.confidence >= 0.6:
            print(">>", resposta.text)
        else:
            print("Infelizmente, ainda não sei responder isso")
            print("Pergunte outra coisa")

if __name__ == "__main__":
    executar_robo()
