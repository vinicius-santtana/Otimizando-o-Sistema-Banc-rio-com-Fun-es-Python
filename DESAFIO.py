# Otimizando-o-Sistema-Banc-rio-com-Fun-es-Python

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza a operação de saque.

    Args:
        saldo: Saldo atual da conta.
        valor: Valor a ser sacado.
        extrato: Histórico de transações.
        limite: Limite máximo por saque.
        numero_saques: Número de saques já realizados.
        limite_saques: Limite máximo de saques.

    Returns:
        Uma tupla contendo o novo saldo e o extrato atualizado.
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato, /):
    """
    Realiza a operação de depósito.

    Args:
        saldo: Saldo atual da conta.
        valor: Valor a ser depositado.
        extrato: Histórico de transações.

    Returns:
        Uma tupla contendo o novo saldo e o extrato atualizado.
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def exibir_extrato(saldo, *, extrato):
    """
    Exibe o extrato bancário.

    Args:
        saldo: Saldo atual da conta (argumento posicional).
        extrato: Histórico de transações (argumento keyword-only).
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def cadastrar_usuario(usuarios):
    """
    Cadastra um novo usuário no sistema.

    Args:
        usuarios: Lista de dicionários contendo os usuários cadastrados.
    """
    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (DD-MM-AAAA): ")
    cpf = input("Digite o CPF (apenas números): ")
    endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Erro: CPF já cadastrado.")
        return

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")


def criar_conta(contas, usuarios):
    """
    Cria uma nova conta corrente para um usuário existente.

    Args:
        contas: Lista de dicionários contendo as contas bancárias.
        usuarios: Lista de dicionários contendo os usuários cadastrados.
    """
    cpf = input("Digite o CPF do titular da conta: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if usuario:
        agencia = "0001"
        numero_conta = len(contas) + 1
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        contas.append(conta)
        print("Conta criada com sucesso!")
        print(f"Agência: {agencia}, Conta: {numero_conta}")
    else:
        print("Erro: Usuário não encontrado.")


def listar_contas(contas):
    """
    Lista todas as contas bancárias cadastradas.

    Args:
        contas: Lista de dicionários contendo as contas bancárias.
    """
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\n======== LISTA DE CONTAS ========")
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Conta: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")
        print("-------------------------------")
    print("================================")


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lc] Listar Contas
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            cadastrar_usuario(usuarios)
        elif opcao == "nc":
            criar_conta(contas, usuarios)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
