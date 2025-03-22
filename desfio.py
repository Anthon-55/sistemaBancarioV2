def exibir_menu():
    opcoes = (
        "\n=============== MENU ================",
        "[d]\tDepositar",
        "[s]\tSacar",
        "[e]\tExtrato",
        "[nc]\tNova conta",
        "[lc]\tListar contas",
        "[nu]\tNovo usuário",
        "[q]\tSair",
        "=> "
    )
    return input("\n".join(opcoes))

def realizar_deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\nValor informado inválido para depósito.")
    return saldo, extrato

def realizar_saque(saldo, valor, extrato, limite, saques_realizados, max_saques):
    if valor <= 0:
        print("\nValor informado inválido para saque.")
    elif valor > saldo:
        print("\nSaldo insuficiente para efetuar o saque.")
    elif valor > limite:
        print("\nO valor do saque excede o limite permitido.")
    elif saques_realizados >= max_saques:
        print("\nLimite de saques diários atingido.")
    else:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        saques_realizados += 1
        print("\n=== Saque realizado com sucesso! ===")
    return saldo, extrato, saques_realizados

def mostrar_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if extrato:
        print(extrato)
    else:
        print("Nenhuma movimentação realizada.")
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()
    if buscar_usuario(cpf, usuarios):
        print("\nUsuário com esse CPF já existe!")
        return
    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ").strip()

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })
    print("\n=== Usuário criado com sucesso! ===")

def buscar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, num_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = buscar_usuario(cpf, usuarios)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": num_conta, "usuario": usuario}
    print("\nUsuário não encontrado. Criação de conta encerrada!")
    return None

def exibir_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return
    for conta in contas:
        dados = f"""
            Agência:\t{conta['agencia']}
            Conta Corrente:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(dados))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    saques_realizados = 0
    usuarios = []
    contas = []

    while True:
        opcao = exibir_menu().lower()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor para depósito: "))
            except ValueError:
                print("Valor inválido.")
                continue
            saldo, extrato = realizar_deposito(saldo, valor, extrato)

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor para saque: "))
            except ValueError:
                print("Valor inválido.")
                continue
            saldo, extrato, saques_realizados = realizar_saque(
                saldo, valor, extrato, limite, saques_realizados, LIMITE_SAQUES
            )

        elif opcao == "e":
            mostrar_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            num_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, num_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            exibir_contas(contas)

        elif opcao == "q":
            print("\nEncerrando o sistema...")
            break

        else:
            print("\nOperação inválida. Por favor, selecione novamente.")

if __name__ == '__main__':
    main()
