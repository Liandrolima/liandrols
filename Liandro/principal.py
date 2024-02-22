from time import sleep
from menu import menu
from funcoes import AdicionarAluno, AtualizarAluno, VerAlunos, RemoverAluno

alunos = {}

while True:
    resposta = menu(['Adicionar Aluno', 'Remover Aluno', 'Atualizar Aluno', 'Ver Alunos', 'Sair do sistema']) 

    match resposta:
        case 1:
            AdicionarAluno(alunos)
        case 2:
            RemoverAluno(alunos)
        case 3:
            AtualizarAluno(alunos)
        case 4:
            VerAlunos(alunos)
        case 5:
            print('\033[32;44mSaindo do sistema... Até logo!\033[m')
            break
        case _:
            print('\033[0;30;41mERRO! Digite uma opção válida!\033[m')
    sleep(2)   
