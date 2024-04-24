print('------------------------------------')
print('           Recebedor 9K      v1.1.5 ')
print('------------------------------------')

while True:
    nomeCl = input('Digite o nome do cliente: ')
    valorCl = input('Digite o valor a ser recebido: ')
    data = input('Digite a data do recebimento(dd/mm/aaaa): ')
    nomeRc = input('Digite o nome de quem vai receber: ')
    obs = input('Digite as observações necessárias ou aperte enter para deixar em branco: ')

    print('Cliente:',nomeCl,'Valor:', valorCl,'Data', data,'Quem vai receber:', nomeRc, 'Observações:', obs)
    confirmacao = input('Essas informações estão corretas? Responda com "Sim" ou "Não" ')

    if confirmacao == 'Sim':
        print('|--------------------------------------------------------------------------|')
        print('|                                                   |                      |')
        print('| Nome da empresa                                   |                      |')
        print('| rua                                               |     RECEBIMENTO      |')
        print('| bairro                                            |                      |')
        print('| cidade, cep e estado                              |                      |')
        print('|                                                   |                      |')
        print('|--------------------------------------------------------------------------|')
        print('| 						     		           |')
        print('| Recebemos de', nomeCl, 'a importância de R$', valorCl, '                           |')
        print('| 						     		           |')
        print('| Data do recibo: ', data, '                                             |')
        print('| Recebido por:', nomeRc, '                                                    |')
        print('| 						     		           |')
        print('| 						     		           |')
        print('| Observações:', obs, '                                                    |')
        print('| 						     		           |')
        print('| 						     		           |')
        print('| 						     		           |')
        print('|                     ----------------------------------------             |')
        print('|                                nome da empresa                           |')
        print('|--------------------------------------------------------------------------|')

        fechar = input('Deseja imprimir outro recibo? Responda com "Sim" ou "Não" ')

        if fechar == 'Sim':
            continue

        elif fechar == 'SIM':
            continue

        elif fechar == 'sim':
            continue

        elif fechar == 'Não':
            break

        elif fechar == 'NÃO':
            break

        elif fechar == 'não':
            break

        elif fechar == 'nao':
            break

        elif fechar == 'NAO':
            break

        elif fechar == 'Nao':
            break

        else:
            print('Erro ao processar confirmação')
            continue

    elif confirmacao == 'SIM':
        print('|--------------------------------------------------------------------------|')
        print('|                                                   |                      |')
        print('| Nome da empresa                                   |                      |')
        print('| rua                                               |     RECEBIMENTO      |')
        print('| bairro                                            |                      |')
        print('| cidade, cep e estado                              |                      |')
        print('|                                                   |                      |')
        print('|--------------------------------------------------------------------------|')
        print('| 						     		           |')
        print('| Recebemos de', nomeCl, 'a importância de R$', valorCl, '                           |')
        print('| 						     		           |')
        print('| Data do recibo: ', data, '                                             |')
        print('| Recebido por:', nomeRc, '                                                    |')
        print('| 						     		           |')
        print('| 						     		           |')
        print('| Observações:', obs, '                                                    |')
        print('| 						     		           |')
        print('| 						     		           |')
        print('| 						     		           |')
        print('|                     ----------------------------------------             |')
        print('|                                nome da empresa                           |')
        print('|--------------------------------------------------------------------------|')

        fechar = input('Deseja imprimir outro recibo? Responda com "Sim" ou "Não" ')

        if fechar == 'Sim':
            continue

        elif fechar == 'SIM':
            continue

        elif fechar == 'sim':
            continue

        elif fechar == 'Não':
            break

        elif fechar == 'NÃO':
            break

        elif fechar == 'não':
            break

        elif fechar == 'nao':
            break

        elif fechar == 'NAO':
            break

        elif fechar == 'Nao':
            break

        else:
            print('Erro ao processar confirmação')
            continue

    elif confirmacao == 'sim':
        print('|--------------------------------------------------------------------------|')
        print('|                                                   |                      |')
        print('| Nome da empresa                                   |                      |')
        print('| rua                                               |     RECEBIMENTO      |')
        print('| bairro                                            |                      |')
        print('| cidade, cep e estado                              |                      |')
        print('|                                                   |                      |')
        print('|--------------------------------------------------------------------------|')
        print('| 						     		           |')
        print('| Recebemos de', nomeCl, 'a importância de R$', valorCl, '                           |')
        print('| 						     		           |')
        print('| Data do recibo: ', data, '                                             |')
        print('| Recebido por:', nomeRc, '                                                    |')
        print('| 						     		           |')
        print('| 						     		           |')
        print('| Observações:', obs, '                                                    |')
        print('| 						     		           |')
        print('| 						     		           |')
        print('| 						     		           |')
        print('|                     ----------------------------------------             |')
        print('|                                nome da empresa                           |')
        print('|--------------------------------------------------------------------------|')

        fechar = input('Deseja imprimir outro recibo? Responda com "Sim" ou "Não" ')

        if fechar == 'Sim':
            continue

        elif fechar == 'SIM':
            continue

        elif fechar == 'sim':
            continue

        elif fechar == 'Não':
            break

        elif fechar == 'NÃO':
            break

        elif fechar == 'não':
            break

        elif fechar == 'nao':
            break

        elif fechar == 'NAO':
            break

        elif fechar == 'Nao':
            break

        else:
            print('Erro ao processar confirmação')
            continue

    elif confirmacao == 'Não':
        continue

    elif confirmacao == 'não':
        continue

    elif confirmacao == 'nao':
        continue

    elif confirmacao == 'Nao':
        continue

    elif confirmacao == 'NAO':
        continue

    else:
        print('Erro ao processar confirmação')
        continue
