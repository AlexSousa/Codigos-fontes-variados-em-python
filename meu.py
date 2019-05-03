import sqlite3
from time import sleep

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()


def criar_tabela():  # Criaçao da tabela
    cursor.execute('CREATE TABLE IF NOT EXISTS Cadastro(produto TEXT, codigo Integer, preco REAL, qt INTEGER)')


def ent_dados():  # Preencher o banco de dados
    while True:
        print('Adicionar produto\n')
        produto = str(input('Produto: '))
        codigo = int(input('Código: '))
        preco = float(input('Preço: R$ '))
        qt = int(input('Quantidade: '))

        cursor.execute('INSERT INTO Cadastro(produto, codigo, preco, qt) VALUES(?, ?, ?, ?)',
                       (produto, codigo, preco, qt))
        conexao.commit()
        sleep(0.5)

        sair = ' '
        while sair not in 'SN':
            sair = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]

        if sair == 'N':
            break


def ler_db():  # Abrir o estoque
    total = 0
    print('	Estoque\n')
    sleep(0.5)
    cursor.execute('SELECT * FROM Cadastro')
    dados = cursor.fetchall()

    i = 0

    print('  Produto | Código | Preço  |  Quantidade | Valor\n')
    for linha in dados:
        i += 1
        print('{} - {} | {} | R$ {:.2f} | {} Unidade(s) | R$ {:.2f}'.format(i, linha[0], linha[1], linha[2], linha[3],
                                                                            linha[2] * linha[3]))
        print('')

    for i in dados:
        total += (i[2] * i[3])

    print('Valor total do estoque: R$ {:.2f}'.format(total))


def modifcar():  # Mudar dados
    print('	Modificar produto')
    msg = int(input('1 - Ver estoque | 2 - Não ver estoque: '))
    if msg == 1:
        ler_db()
    else:
        pass

    while True:

        print('''
1 - Nome do produto
2 - Preço do produto
3 - Quntidade
4 - Sair
		''')
        op = int(input('Opção: '))

        if op == 1:
            prod = str(input('Novo produto: '))
            n_prod = int(input('Código do produto a ser modificado: '))

            cursor.execute('UPDATE Cadastro SET produto = ? WHERE codigo = ?', (prod, n_prod))
            conexao.commit()
            ler_db()

        if op == 2:
            prod = str(input('Novo preço: '))
            n_prod = int(input('Código do produto a ser modificado: '))

            cursor.execute('UPDATE Cadastro SET preco = ? WHERE codigo = ?', (prod, n_prod))
            conexao.commit()
            ler_db()

        if op == 3:
            prod = str(input('Nova quantidade: '))
            n_prod = int(input('Código do produto a ser modificado: '))

            cursor.execute('UPDATE Cadastro SET qt = ? WHERE codigo = ?', (prod, n_prod))
            conexao.commit()
            ler_db()

        if op == 4:
            break


def deletar():  # Excluir um ou todos os dados
    print('	Excluir produto')
    print('')

    msg = int(input('1 - Ver estoque | 2 - Não ver estoque: '))
    if msg == 1:
        ler_db()
    else:
        pass

    op = int(input('0 - Sair | 1 - Um produto | 2 - Todos os produtos: '))
    print('')
    if op == 1:
        prod = int(input('Código do produto a ser deletado: '))

        cursor.execute('DELETE FROM Cadastro WHERE codigo = ?', (prod,))
        conexao.commit()

        ler_db()

    if op == 2:
        aviso = str(input('Tem certeza? [S/N]: ')).upper().strip()[0]
        if aviso == 'S':
            cursor.execute('DELETE FROM Cadastro')
            conexao.commit()

            msg = int(input('1 - Ver estoque | 2 - Não ver estoque: '))
            if msg == 1:
                ler_db()
            else:
                pass
        else:
            while aviso not in "SN":
                aviso = str(input('Tem certeza? [S/N]: ')).upper().strip()[0]

                if aviso == "S":
                    cursor.execute('DELETE FROM Cadastro')
                    conexao.commit()
                    break


# Menu
while True:
    print('''	Menu
1 - Adicionar produto
2 - Ver estoque
3 - Modificar produto
4 - Excluir produto
5 - Sair
	''')
    try:
        op = int(input('Opção: '))

        if op == 1:
            criar_tabela()
            ent_dados()

        if op == 2:
            ler_db()

        if op == 3:
            modifcar()

        if op == 4:
            deletar()

        if op == 5:
            break
    except ValueError:
        pass

cursor.close()
conexao.close()
