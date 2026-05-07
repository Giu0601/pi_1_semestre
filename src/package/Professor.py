from Tarefa import Tarefa
from Tentativa import Tentativa

class Professor:
    def __init__(self, nome: str, sobrenome: str, username: str) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.username = username

    def criaTarefa() -> Tarefa:
        tarefa1 = Tarefa()

        return tarefa1

    def corrige_tarefa(self, tarefa: Tarefa):
        self.atribuir_nota(tarefa)

    def atribuir_nota(nota: float, tentativa: Tentativa):
        tentativa.set_nota(nota)