def abrirArquivo():
    file = open("notas_estudantes.dat", "rt", encoding="utf-8")
    buscarInfos(file)
    file.close()


def buscarInfos(file):
    nomes = []
    notas = []
    nomesNotas = []
    for linha in file.readlines():
        data = linha.split()
        notas.append(data[1:])
        nomesNotas.append(data[0])
        if len(data[1:]) >= 5:
            nomes.append(data[0].capitalize())
    estudantesCincoNotas(nomes)
    calcularMedia(nomesNotas, notas)
    maiorNota(nomesNotas, notas)


def estudantesCincoNotas(nomes):
    print('=' * 20 + " ESTUDANTES QUE TÊM MAIS DE CINCO NOTAS " + 20 * "=")
    for nome in nomes:
        print(f'-> {nome}')


def calcularMedia(nomes, notas):
    i = 0
    print('=' * 20 + " MÉDIA DAS NOTAS DE CADA ESTUDANTE " + 20 * "=")
    for nota in notas:
        intNota = list(map(int, nota))
        media = sum(intNota) / len(intNota)
        print(f'-> Nome do Aluno: {nomes[i].capitalize()} -/- Média: {media:.2f}')
        i += 1


def maiorNota(nomes, notas):
    i = 0
    print('=' * 20 + " NOTA MAIOR DE CADA ESTUDANTE " + 20 * "=")
    for nota in notas:
        intNota = list(map(int, nota))
        maxNotas = max(intNota)
        print(f'-> Nome do Aluno: {nomes[i].capitalize()} -/- Maior nota: {maxNotas:.2f}')
        i += 1




if __name__ == "__main__":
    abrirArquivo()