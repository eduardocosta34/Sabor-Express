import os

restaurantes = [
    {'nome':'Pizzaria Souza', 'categoria':'Italiana', 'ativo':False},
    {'nome':'Café Mania','categoria':'Brasileira', 'ativo':True},
    {'nome':'SushiLandia', 'categoria':'Japonesa', 'ativo':True}
]

def exibir_nome_do_programa(): 
    ''' Função para exibir o nome do Sistema '''
    print('𝕤𝕒𝕓𝕠𝕣 𝕖𝕩𝕡𝕣𝕖𝕤𝕤\n')

def exibir_opcoes():
    ''' Função para exibir as opções '''
    print ('1. Cadastrar restaurante')
    print ('2. Listar restaurantes')
    print ('3. Ativar restaurante')
    print ('4. Sair\n')

def finalizar_app():
    ''' Função para finalizar o sistema '''
    exibir_subtitulo('Finalizando APP')

def voltar_ao_menu():
    ''' função para poder voltar ao menu principal '''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    exibir_subtitulo('Opção invalida!')
    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    linhas = '*' * (len(texto))
    print(linhas)
    print(texto)
    print(linhas)
    print()

def cadastrar_restaurante():
    ''' Função para cadastrar novo restaurante '''
    exibir_subtitulo('Cadastro de novos restaurantes: ')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input('Digite o nome da categoria do restaurante {nome_restaurante}: ')

    dados_restaurante = {
        'nome': nome_restaurante,
        'categoria': categoria,
        'ativo': False
    }

    restaurantes.append(dados_restaurante)

    print(f'o restaurante {nome_restaurante} foi cadastrado com sucesso!!')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Restaurantes cadastrados: ')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for item in restaurantes:
        nome_restaurante = item['nome']
        categoria_restaurante = item['categoria']
        ativo_restaurante = 'ativado' if item['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')

    voltar_ao_menu()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante: ')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ATIVADO' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi DESATIVADO'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))
        print(f'você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
