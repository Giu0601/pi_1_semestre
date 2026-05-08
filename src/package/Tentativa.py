from Tarefa import Tarefa
from Aluno import Aluno
from Questao import Questao

class Tentativa (Tarefa):
    def __init__(self, nota: float, aluno: Aluno) -> None:
        self._nota = nota 
        self._aluno = aluno


    @property
    def nota(self) -> float:
        return self._nota
    
    @nota.setter
    def nota(self, nota: float) -> None:
        
        if nota is not float:
            try:
                    nota = float(nota)
            except ValueError:
                    raise ValueError(f'Valor Inválido "{nota}" não é do tipo float')
    
        self._nota = nota