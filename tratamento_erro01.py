def erro():

    try:
         f = open('Nomes.txt')
         s = f.readline()
         i = int(s.strip())
    except FileExistsError:
        print("Arquivo 'Nomes.txt não encobtrado")
    except IOError:
        print("Erro na abertura do arquivo!")
    except ValueError:
        print("Formato inválido encontrado no arquivo")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise

def dividir(numerador, denominador):
    if denominador == 0:
        raise ValueError("Decisão por zero não é permitida!")
    return numerador / denominador

try:
    resultado = dividir(10, 0)
    print("Resultado:", resultado)
except ValueError as erro:
    print("Ocorreu um ero:", erro)

class MeuErro(Exception):
    pass

def dividir(numerador, denominador):
    if denominador == 0:
        raise MeuErro("Decisão por zero não é permitida!")
        return numerador / denominador
try:
    resultado = dividir(10, 0)
    print("Resultado:", resultado)
except MeuErro as erro:
    print("Ocorreu um erro personalizado:", erro)




dividir()
erro()