from Tarefa import Tarefa
from Questao import Questao

class Tentativa (Tarefa):
    def __init__(self, nota: float) -> None:
        self.set_nota(nota) 

    def set_nota(self, nota: float) -> None:
        self.nota = nota

    