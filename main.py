import json

try:
    with open("dados.json", "r") as arquivo:
        dados = json.load(arquivo)
except (FileNotFoundError, json.JSONDecodeError):
    dados = {
        "receitas": [],
        "despesas": []
    }

def adicionar_receita(dados):
    receita = {
        "descricao": input('\n(ex: salário, freelance, presente): '),
        "valor": float(input('Adicione sua receita mensal: R$ ')),
        "data": input('Digite a data: ')
    }
    dados["receitas"].append(receita)

    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
    print('\nReceita adicionada com sucesso!')


def adicionar_despesas(dados):
    print('\nDESPESA MENSAL')
    despesa = {
        "descricao": input('\n(ex: mercado, aluguel, transporte, lanche): '),
        "valor": float(input('Adicione a despesa mensal: R$ ')),
        "data": input('Digite a data: ')
    }
    dados["despesas"].append(despesa)

    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
    
    print('\nDespesa adicionada com sucesso!')


def listar_receitas(dados):
    for receita in dados["receitas"]:
        print(f"\nDescricao: {receita['descricao']}")
        print(f"Valor: {receita['valor']}")
        print(f"Data: {receita['data']}")


def listar_despesas(dados):
    for despesa in dados["despesas"]:
        print(f"\nDescricao: {despesa['descricao']}")
        print(f"Valor: {despesa['valor']}")
        print(f"Data: {despesa['data']}")


def resumo(dados):
    total_receitas = 0
    total_despesas = 0

    for r in dados["receitas"]:
        total_receitas += r["valor"]

    for d in dados["despesas"]:
        total_despesas += d["valor"]

    saldo = total_receitas - total_despesas

    print(f'Total de receitas: R$ {total_receitas}')
    print(f'Total de despesas: R$ {total_despesas}')
    print(f'Saldo: R$ {saldo}')

    if saldo >= 0:
        print('\nSituacao: Positiva')
    else:
        print('\nSitacao: Negativa')


while True:
    print('\n[1] Adicionar Receita\n[2] Adicionar Despesas\n[3] Listar Receitas\n[4] Listar Despesas\n[5] Resumo\n[6] Limpar dados\n[0] Sair\n')
    try:
        opcao = int(input('Escolha uma opcao: '))
    except ValueError:
        print('\nDigite apenas numeros!')
        continue

    if opcao == 1:
        adicionar_receita(dados)

    elif opcao == 2:
        adicionar_despesas(dados)

    elif opcao == 3:
        listar_receitas(dados)

    elif opcao == 4:
        listar_despesas(dados)

    elif opcao == 5:
        resumo(dados)
    
    elif opcao == 6:
        while True:
            apagar = input('\nTem certeza que deseja apagar tudo? [S/N] ').upper()
            
            if apagar in ['S', 'N']:
                break
            else:
                print('Digite apenas S ou N!')
                
        if apagar == 'S':
            dados = {
                "receitas": [],
                "despesas" : []
            }
            
            with open("dados.json", "w") as arquivo:
                json.dump(dados, arquivo, indent = 4)
            
            print('\nDados limpos com sucesso!')
        else:
            print('\nOperacao cancelada.')
            

    elif opcao == 0:
        break

    else:
        print('\nOpcao invalida!')

print('Programa encerrado.')
