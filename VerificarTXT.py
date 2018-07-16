import os

def verificar(path, numLinhas):
    contador = 0
    ocorrencias = 0
    for p, _, files in os.walk(os.path.abspath(path)):
        for file in files:
            caminho = os.path.join(p, file)
            contador += 1
            linhas = contarLinhas(caminho)
            if linhas > numLinhas:
                ocorrencias += 1
                print("Ocorrência em: " + caminho)

    print("Total de verificações: " + str(contador))
    print("Total de ocorrências: " + str(ocorrencias))


def contarLinhas(arquivo):
    with open(arquivo, 'r') as file:
        total = len(file.readlines())
        file.close
        return(total)

pasta = input("Caminho da pasta que deseja verificar: ")
numLinhas = int(input("Número máximo de linhas que o arquivo deve ter: "))

verificar(pasta, numLinhas)