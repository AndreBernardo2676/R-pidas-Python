import os

caminho = os.path.join(os.getcwd(), 'manipulacaodearquivos', 'arquivo.txt')
arquivo = open(caminho)


#arquivo = open('arquivo.txt')

print('nome do arqivo:', arquivo.name)
print('tamanho do arquivo (embytes):', arquivo.tell())
print('modo de arquivo:', arquivo.mode)
print('arquivo está fechado?', arquivo.closed)

arquivo.close()

print('arquivo está fechado?', arquivo.closed)


arquivo= open('G:\Andre\Git\RapidasPython\manipulacaodearquivos\arquivo.txt','w')
arquivo.write('André')
arquivo.close()

arquivo= open('G:\Andre\Git\RapidasPython\manipulacaodearquivos\arquivo.txt')
print(arquivo.readline())
arquivo.close()



def exemplo01():
    arquivo = open("arquivo.txt", 'w')
    arquivo.write('André')
    arquivo.writelines(['\nAna', '\nJoão', '\nCarlos', '\nRui'])
    arquivo.close()

def exemplo02():
    arquivo = open("arquivo.txt", 'r')
    print(arquivo.readline)
    arquivo.close()

def exemplo03():
    caminho_arquivo= 'arquivo.txt'
    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write("Essa é a primeira linha. \n")
        arquivo.write("Essa é a segunda linha. \n")

        linhas = ["Essa é a primeira linha em uma lista.", "Essa é a segunda linha em uma lista."]
        arquivo.writelines(linhas)

exemplo01()
exemplo02()
exemplo03()

caminho_arquivo= 'arquivo.txt'
arquivo = open(caminho_arquivo, 'r')

linha1 = arquivo.readline()
print(f'Linha 1: {linha1}')
linha2 = arquivo.readline()
print(f'Linha 2: {linha2}')

arquivo.close()



arquivo = open(caminho_arquivo, 'r')
linha= arquivo.readline()
for i, linha in enumerate(linha, start=1):
    print(f'linha{i}: {linha}')


# Cria um arquivo de exemplo e escreve um conteúdo nele
with open("exemplo.txt", "w", encoding="utf-8") as f:
    f.write("Exemplo de um dos métodos zteek() e tell() em Python.")

# Abre arquivo para leitura e demonstra o uso de streek() e tell()
with open("exemplo.txt", "r", encoding="utf-8") as f:
    print("Posição inicial do cursos:", f.tell())

    # Lê os primeiros 10 caracteres.
    conteudo = f.read(10)
    print("Conteúdo lido:", conteudo)
    print("Posição do cursor após 10 caracteres", f.tell())

    # Volta para o inicio do arquivo
    f.seek(0, 0) # whence=0: início do arquivo
    print("Posição do cursor após seek(0, 0):", f.tell())


