import os

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = self.validar_nota(nota)

    def validar_nota(self, nota):
        try:
            nota = float(nota)
            if 0 <= nota <= 10:
                return nota
            else:
                raise ValueError("A nota deve estar entre 0 e 10.")
        except ValueError as e:
            print(f"Erro ao atribuir nota: {e}")
            return None

class RegistroNotas:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def salvar_nota(self, aluno):
        if aluno.nota is not None:
            with open(self.arquivo, "a") as f:
                f.write(f"{aluno.nome},{aluno.nota}\n")
            print(f"Nota de {aluno.nome} salva com sucesso.")
        else:
            print(f"Não foi possível salvar a nota de {aluno.nome}.")

    def listar_notas(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r") as f:
                linhas = f.readlines()
                if linhas:
                    print("Registro de notas:")
                    for linha in linhas:
                        nome, nota = linha.strip().split(",")
                        print(f"{nome}: {nota}")
                else:
                    print("Nenhuma nota registrada.")
        else:
            print("Arquivo de registro ainda não foi criado.")


registro = RegistroNotas("notas.txt")

aluno1 = Aluno("Maria", 8.5)
aluno2 = Aluno("Carlos", 12)  # Erro proposital
aluno3 = Aluno("Ana", "7.2")

registro.salvar_nota(aluno1)
registro.salvar_nota(aluno2)
registro.salvar_nota(aluno3)

registro.listar_notas()
