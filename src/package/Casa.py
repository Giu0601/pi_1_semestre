from Tarefa import Tarefa

class Casa():
    def __init__(self, num_casa: int, nivel: int, tarefa: Tarefa):
        self.num_casa = num_casa
        self.nivel = nivel
        self.tarefa = tarefa
    
    def exibir_tarefa(self, tarefa: Tarefa):
        print(self.tarefa)

    def exibir_casa(self):
        print(f"Casa {self.num_casa} | Nível {self.nivel}")

    def avancar_casa(self):
        pass #ver se coloca a questão da nota aqui ou na seção