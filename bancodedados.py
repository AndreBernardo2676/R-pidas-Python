import os 
import sqlite3
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo

class BancoDeDados:
    def __init__(self, nome_banco="banco_sqllite"):
        self.nome_banco = os.path.join(os.path.dirname(__file__), nome_banco)
        self.com = None

    def conectar(self):
        try:
            self.com = sqlite3.connect(self.nome_banco)
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco: {e}")

    def criar_tabelas(self):
         self.criar_tabelas_pessoa()
         self.criar_tabelas_marca()
         self.criar_tabelas_veiculo()

    def criar_tabelas_pessoa(self):
        if self.com:

            try:
                cursor = self.com.cursos()
                cursor.execute(
                    """CREATE TABLE IF NOT EXEISTS Pessoa(
                    cpf INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    nascimento DATE,
                    oculos BOOLEAN
                    )"""
                )
                self.com.commit()
            except sqlite3.Error as e:
                 print(f"Erro ao criar a tabela Pessoa : {e}")

    def criar_tabelas_marca(self):
            if self.com:

                try:
                    cursor = self.com.cursos()
                    cursor.execute(
                        """CREATE TABLE IF NOT EXEISTS Pessoa(
                        id INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        sigla TEXT
                        )"""
                    )
                    self.com.commit()
                except sqlite3.Error as e:
                    print(f"Erro ao criar a tabela Marca : {e}")

    def criar_tabelas_veiculo(self):
            if self.com:
                try:
                    cursor = self.com.cursos()
                    cursor.execute(
                        """CREATE TABLE IF NOT EXEISTS Veiculo(
                        narca TEXT PRIMARY KEY,
                        cor TEXT NOT NULL,
                        cpf _proprietario IM+NTEGER,
                        id _marca INTAGER,
                        FOREIGN KEY(cpf_proprietario) REFERENCES pessoa(cpf),
                        FOREIGN KEY(id_marca) REFERENCES Marca(id))"""
                    )
                    self.com.commit()
                except sqlite3.Error as e:
                    print(f"Erro ao criar a tabela Veiculo: {e}")



                       
                    