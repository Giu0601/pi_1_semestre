from Questao import Questao

class Tarefa:
    def __init__(self, prazo: str, questao: Questao) -> None:
        self.prazo = prazo
        self.questao = questao

    def adicionar_questao(self, questao: Questao):
        pass

    def exibir_questionario(self):
        pass