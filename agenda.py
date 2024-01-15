from time import sleep
agenda = {}



def teleInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO: por favor, digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[0;31mERRO:Operação canelada pelo usuário=\033[m')
            return 0
        else:
            return n
        


def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    sleep(2)
    cabeçalho('          \033[30;42mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = teleInt('\033[36mSua opção: \033[m')
    return opc



def inluirConta(nome='desconhecido', telefone=0):
    try:        
        agenda[nome]=telefone
        
    except:
        print('Houve um ERRO ao inserir os dados!')
    else:
        print(f'Novo registro de {nome} adicionado.👍')
            

def alterarContato(nome, telefone):
    while True:
        if nome in agenda.keys():
            print(nome, " - ", agenda[nome])
            telefone = teleInt('digite novo contato')
            agenda[nome] = telefone
            print(f'O novo contato de {nome} é {telefone}')
            break
        elif nome not in agenda:
            try:
                resp = str(input('Contato não encontrado, deseja cadastrá-lo? [S/N]')).upper().strip()[0]
            except (KeyboardInterrupt):
                print(f'\033[0;31mERRO:Operação canelada pelo usuário=\033[m')
                return 0
            if resp in 'S':
                telefone = teleInt('digite novo contato')
                agenda[nome] = telefone 
                return inluirConta(nome, agenda[nome] ) 
            if resp in 'N':
                print('Usuário desistiu do cadastrado😩')  
                break
            if resp not in 'SN':
                print('Opção inválida')
            
                
                        
def consultarContatos():
    if len(agenda)==0:
        print("Agenda vazia!!")
    else:
        for i in agenda.items():
            print(i)
    

def consultarContato(nome):
    while True:
        if nome in agenda:
            print(nome, " - ", agenda[nome])
            break
        elif nome not in agenda:
            try:
                resp = str(input('Contato não encontrado, deseja cadastrá-lo? [S/N]')).upper().strip()[0]
            except (KeyboardInterrupt):
                print(f'\033[0;31mERRO:Operação canelada pelo usuário=\033[m')
                return 0
            if resp in 'S':
                telefone = teleInt('digite novo contato')
                agenda[nome] = telefone 
                return inluirConta(nome, agenda[nome] )
            if resp in 'N':
                print('Usuário desistiu do cadastrado😩')
                break  
            if resp not in 'SN':
                print('Opção inválida')
        
    
def excluirContato(nome):
    if nome in agenda:
        resp = str(input(f'você tem certeza que deseja excluir o contato {nome} da agenda?[S/N]')).upper().strip()[0]
        if resp in 'S':
            agenda.pop(nome)
            print('Processando...')
            sleep(1.5)
            print('Contato excluido😩')
        elif resp in 'N':
            print('Contato permanecerar na agenda')
        else:
            print('Resposta inválida')
    else:
        print("Contato não encontrado!")


def limparContatos():
    resp = str(input(f'você tem certeza que deseja excluir todos os contatos da agenda? [S/N]')).upper().strip()[0]
    if resp == 'S':
        agenda.clear()
        if len(agenda)==0:
            print("Contatos apagados!!")
    elif resp == 'N':
        print('Contatos preservados')
    else:
        print('ERRO: Digite um opção válida')
    

while True:
    resposta = menu(['Adicionar contato', 'Alterar contato', 'Mostrar todos os contatos', 'Buscar contato', 'Excluir contato', 'Limpar agenda', 'Sair do sistema']) 

    match resposta:
        case 1:
            cabeçalho('\033[32mNOVO CADASTRO\033[m')
            nome = str(input('digite seu nome '))
            telefone = teleInt('digite um contato ')
            inluirConta(nome, telefone)
        case 2:
            cabeçalho('\033[32mALTERAR CONTATO\033[m')
            nome = str(input('Nome: '))
            telefone = teleInt
            alterarContato(nome, telefone) 
        case 3:
            cabeçalho('\033[32mCONSULTAR CONTATOS\033[m')
            consultarContatos()
        case 4:
            cabeçalho('\033[32mCONSULTAR CONTATO\033[m')
            nome = input("Informe o nome: ")
            consultarContato(nome)
        case 5:
            cabeçalho('\033[32mEXCLUIR CONTATO\033[m')
            nome = input("Informe o nome do contato a ser excluido: ")
            excluirContato(nome)
        case 6:
            cabeçalho('\033[32mLIMPAR CONTATOS\033[m')
            limparContatos()
        case 7:
            cabeçalho('\033[32;44mSaindo do sistema... Até logo!\033[m')
            break
        case _:
            print('\033[0;30;41mERRO! Digite uma opção válida!\033[m')
    sleep(2)



    



