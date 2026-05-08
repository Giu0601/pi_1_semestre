from Tarefa import Tarefa
from Tentativa import Tentativa
from Questao import Questao

class Professor:
    def __init__(self, nome: str, sobrenome: str, username: str) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.username = username

    def criaTarefa(self) -> Tarefa:

        # Proximas linhas somente para poder testar depois alinhar com o banco e front
        prazo = input("Digite o prazo (dd-mm-yyyy)")
        questoes = [Questao(), Questao(), Questao()]
        
        tarefa1 = Tarefa(prazo, questoes)

        return tarefa1


    def atribuir_nota(self, nota: float, tentativa: Tentativa):
        tentativa.nota = nota

    def corrige_tarefa(self, tentativa: Tentativa):
        nota = float(input("Digite a nota"))
        self.atribuir_nota(nota, tentativa)