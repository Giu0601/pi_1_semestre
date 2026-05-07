from Tarefa import Tarefa

class Professor:
    def __init__(self, nome: str, sobrenome: str, username: str) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.username = username

    def criaTarefa() -> Tarefa:
        tarefa1 = Tarefa()

        return tarefa1


