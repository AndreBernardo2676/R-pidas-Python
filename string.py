import re

class Exemplo:

    @staticmethod
    def exemplo_uso_de_string_01() -> None:
        texto = "Nossa aula Manipulando String."
        print(texto[0:20:2])  

    @staticmethod
    def exemplo_uso_de_string_02() -> None:
        texto = "Nossa aula Manipulando String."
        print(f"step: 1 -> " + str(len(texto)))  
        print(f"step: 2 -> " + str(texto.count("a")))  
        print(f"step: 3 -> " + str(texto.count("a", 5, 30))) 

    @staticmethod
    def exemplo_uso_de_string_03() -> None:
        texto = "Nossa aula Manipulando String."

        print("case: 1 if Find -> " + str(texto.find("aula")))
        print("case: 1 if Null -> " + str(texto.find("Python")))

        print("case: 2 if Find -> " + str('String' in texto))
        print("case: 2 if Null -> " + str('André' in texto))

    @staticmethod
    def exemplo_uso_de_string_04() -> None:
        texto = "Nossa aula Manipulando String."

        novo_txt = texto.replace("Manipulando", "trabalhando com")
        print("novo-texto:", novo_txt)

        print(texto.startswith("Nossa"))
        print(texto.startswith("aula"))

        print(texto.endswith("aula"))
        print(texto.endswith("."))

    @staticmethod
    def exemplo_uso_de_string_05() -> None:
        texto = "Nossa aula Manipulando String."

        print(texto.lower())
        print(texto.upper())
        print(texto.capitalize())
        print(texto.title())
        print(texto.swapcase())

    @staticmethod
    def exemplo_uso_de_string_06() -> None:
        texto = "Nossa aula Manipulando String."
        nome = " João "  # Corrigindo erro de variável não definida
        print(f'olá, {nome}!')
        print(f'olá, {nome.strip()}!')

        print(f'!{nome.rstrip()}!')
        print(f'!{nome.lstrip()}!')

    @staticmethod
    def exemplo_uso_de_string_07() -> None:
        texto = "Nossa aula Manipulando String."
        print(texto.split())
        print(texto.split('Nossa'))

    @staticmethod
    def exemplo_uso_de_string_08() -> None:
        texto = "Nossa aula Manipulando String."
        print(''.join(texto))
        print(texto.split())
        print(''.join(texto.split()))

    @staticmethod
    def exemplo_get_coxinhas(*pedidos):
        return [f'{pedido} coxinhas' for pedido in pedidos]

    @staticmethod
    def exemplo_get_joelho(*pedidos):
        for pedido in pedidos:
            yield f'{pedido} joelho(s)'

    @staticmethod
    def exemplo_regex_01():
        texto = "O número de telefone de André é (132) 456-7890."
        padrao = r'\(\d{3}\) \d{3}-\d{4}'

        resultado = re.search(padrao, texto)
        if resultado:
            numero_telefone = resultado.group()
            print("Número de telefone encontrado:", numero_telefone)
        else:
            print("Número de telefone não encontrado.")

    @staticmethod
    def exemplo_regex_02():
        texto = "Meu e-mail é exemplo@gmail.com, entre em contato."
        padrao = r'\b\w+@\w+\.\w+\b'  # Correção na regex

        novo_texto = re.sub(padrao, "[email oculto]", texto)
        print(novo_texto)


if __name__ == "__main__":
    Test = Exemplo  # Correção do nome da classe

    '''
    Test.exemplo_uso_de_string_01()
    Test.exemplo_uso_de_string_02()
    Test.exemplo_uso_de_string_03()
    Test.exemplo_uso_de_string_04()
    Test.exemplo_uso_de_string_05()
    Test.exemplo_uso_de_string_06()
    Test.exemplo_uso_de_string_07()
    Test.exemplo_uso_de_string_08()
    '''

    '''
    salgados_return = Test.exemplo_get_coxinhas(4, 6, 8)
    print("Usando return:")
    print(salgados_return)

    print("\nUsando yield:")
    for salgado in Test.exemplo_get_joelho(4, 6, 8):
        print(salgado)
    '''

    Test.exemplo_regex_02()
