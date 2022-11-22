import unittest
from covid19 import *

class TestaSaudacoes(unittest.TestCase):

    def setUp(self):
        self.covid19_bot = ChatBot("Robô de atendimento da covid-19",
                read_only=True,
                statement_comparison_function=comparar_mensagens,
                response_selection_method=selecionar_resposta,
                logic_adapters=[
                    {
                        "import_path": "chatterbot.logic.BestMatch",
                    }
            ])

    def testar_oi(self):
        resposta = self.covid19_bot.get_response("ola")
        self.assertIn("Olá, sou o robô tira-dúvidas da COVID-19. Qual sua dúvida?", resposta.text)

    def testar_saudacoes(self):
        print("----------------TESTANDO SAUDAÇÕES-----------------")
        saudacoes = ["bom dia", "boa tarde", "boa noite"]
        for saudacao in saudacoes:
            print(f"testando: {saudacao}")
            resposta = self.covid19_bot.get_response(saudacao)
            self.assertIn(saudacao + ", sou o robô tira-dúvidas da COVID-19. Qual sua dúvida?", resposta.text)

    def testar_pergunta_um(self):
        resposta = self.covid19_bot.get_response("quanto tempo o coronavirus permanece ativo em diferentes superfícies?")
        self.assertIn("Atualizado em 29/04/2022: O novo coronavírus pode permanecer no ar por cerca de 40 minutos a até 2 horas e meia. Nas superfícies, sua sobrevivência irá depender do tipo de material. Quando estamos doentes e falamos, tossimos ou espirramos, liberamos gotas muito pequenas de saliva ou de secreção do nariz cheias de vírus.", resposta.text)

    def testar_pergunta_dois(self):
        resposta = self.covid19_bot.get_response("como deve ser feita a limpeza de superfícies para evitar o coronavírus?")
        self.assertIn("Atualizada em 29/04/2022: A limpeza de superfícies pode ser feita com água e sabão (qualquer sabão de uso comum, como detergentes), álcool a 70% ou hipoclorito (água sanitária) a 0,1%. Tome cuidado ao usar água sanitária, pois ela é tóxica e pode prejudicar o trato respiratório (órgãos que usamos para respirar).", resposta.text)

    def testar_pergunta_tres(self):
        resposta = self.covid19_bot.get_response("o que é período de incubação e qual o período de incubação do novo coronavírus?")
        self.assertIn("Atualizado em 03/05/2022: É o intervalo entre a data do primeiro contato com o vírus até o início dos sintomas da doença. No caso do novo coronavírus, o período de incubação varia de 2 a 14 dias. Isso quer dizer que a pessoa pode já estar com o vírus, mas desenvolver sintomas só depois de 2 a 14 dias.", resposta.text)

    def testar_pergunta_quatro(self):
        resposta = self.covid19_bot.get_response("Quem deve continuar usando máscara?")
        self.assertIn("Devem continuar usando máscara: Pessoas com baixa imunidade (imunossuprimidas); pessoas com doenças crônicas como doenças cardiovasculares (do coração), diabetes, hipertensão arterial (pressão alta), obesidade; idosos, pessoas não vacinadas ou que não tomaram todas as doses da vacina; profissionais de saúde e outros trabalhadores expostos a grande circulação de pessoas durante o dia de trabalho.", resposta.text)

    def testar_pergunta_cinco(self):
        resposta = self.covid19_bot.get_response("Devo ficar isolado por quanto tempo se o meu teste PCR deu positivo?")
        self.assertIn("Resposta atualizada em 28/04/2022: Se você testou positivo deve ficar isolado por 10 dias após o início dos sintomas ou do resultado do teste RT-PCR. Esse período de isolamento irá garantir que você não seja mais capaz de infectar outras pessoas.", resposta.text)

    def testar_pergunta_seis(self):
        resposta = self.covid19_bot.get_response("Como posso fortalecer minha imunidade para me proteger do novo coronavírus?")
        self.assertIn("Atualizado em 29/04/2022: Mantenha uma alimentação saudável, pratique exercícios físicos, não fume, não use drogas e não consuma bebidas alcoólicas. Faça o que lhe dá prazer, mas evite comportamentos que possam lhe colocar em risco e locais com muita gente (aglomeração).", resposta.text)

    def testar_pergunta_sete(self):
        resposta = self.covid19_bot.get_response("Limpar a casa com água sanitária, misturada com água e algum detergente e desinfetante, mata o coronavírus?")
        self.assertIn("Revalidada em 02/05/2022: O uso de um produto de limpeza é suficiente. Cuidado com a mistura de vários produtos diferentes, pois podem ocorrer reações químicas e liberação de substâncias tóxicas. Para orientações gerais sobre os cuidados de higiene e limpeza em casas com casos suspeitos ou confirmados de Covid-19.", resposta.text)


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TestaSaudacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)