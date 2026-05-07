from Aluno import Aluno
from Professor import Professor

class Turma:
    def __init__(self, curso: str, cod_turma: str, cod_sub_turma: str, professor: Professor, *alunos: Aluno):
        self.curso = curso
        self.cod_turma = cod_turma
        self.cod_sub_turma = cod_sub_turma
        self.professor = professor
        self.alunos = alunos