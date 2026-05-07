from Tentativa import Tentativa
from Tarefa import Tarefa
from Casa import Casa

class Aluno:
    def __init__(self, nome: str, sobrenome: str, username: str, casa: Casa):
        self.nome = nome
        self.sobrenome = sobrenome
        self.username = username

    def realizar_tentativa(self, tarefa: Tarefa):
        self.entregar_tentativa

    def entregar_tentativa(self) -> Tentativa:
        tentativa1 = Tentativa()

        return tentativa1
    





