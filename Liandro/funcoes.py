from time import sleep
from confg import matricInt, linha, cabeçalho

def AdicionarAluno(alunos):
    cabeçalho('\033[32mNOVO CADASTRO\033[m')
    nome = str(input('Digite o nome do aluno: '))
    matricula = matricInt('Digite a matrícula do aluno: ')
    alunos[matricula]= nome
    print(f'Novo registro de {nome} adicionado.👍')

def RemoverAluno(alunos):
    cabeçalho('\033[32mREMOVER ALUNO\033[m')
    matricula = matricInt('Digite a matrícula do aluno(a) que será exluido(a): ')
    if matricula in alunos:
        resp = str(input(f'Você tem certeza que deseja excluir o registro do aluno {alunos[matricula]}?[S/N]')).upper().strip()[0]
        if resp in 'S':
            alunos.pop(matricula)
            print('Processando...')
            sleep(1.5)
            print('Registro excluido😩')
        elif resp in 'N':
            print('Registro não será excluído')
        else:
            print('Resposta inválida')
    else:
        print("Aluno não encontrado!")

def AtualizarAluno(alunos):
    cabeçalho('\033[32mATUALIZAR ALUNO\033[m')
    matricula = matricInt('Digite a matrícula do aluno: ')
    if matricula in alunos.keys():
        print(matricula, " - ", alunos[matricula])
        while True:
            resp = str(input('Deseja alterar o nome do aluno? [S/N]: ')).upper().strip()[0]
            if resp in 'S':
                novo_nome = str(input('Digite o novo nome do aluno: '))
                alunos[matricula] = novo_nome
                print(f'Nome do aluno atualizado para: {novo_nome}')
                break
            elif resp in 'N':
                break
            else:
                print('Opção inválida!')
    else:
        print('Matrícula não encontrada.')

def VerAlunos(alunos):
    cabeçalho('\033[32mVER ALUNOS\033[m')
    if len(alunos)==0:
        print("Não há dados para ser exibidos!!")
    else:
        for matricula, nome in alunos.items():
            print(f'Matrícula: {matricula} - Nome: {nome}')
