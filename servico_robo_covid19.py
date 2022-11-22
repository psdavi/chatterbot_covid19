from covid19 import *
from flask import Flask

VERSAO = "1.0"

covid19_bot = ChatBot("Robô de atendimento da covid-19",
    read_only=True,
    statement_comparison_function=comparar_mensagens,
    response_selection_method=selecionar_resposta,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
        }
    ])

servico_robo_covid19 = Flask(__name__)


@servico_robo_covid19.route("/versao", methods=["GET"])
def get_versao():
    return VERSAO

@servico_robo_covid19.route("/resposta/<mensagem>", methods=["GET"])
def get_resposta(mensagem):
    resposta = covid19_bot.get_response(mensagem)
    return resposta.text

if __name__ == "__main__":
    servico_robo_covid19.run()
