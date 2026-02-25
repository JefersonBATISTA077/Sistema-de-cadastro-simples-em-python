class Pessoa:
    def __init__(self):
        self.nome = None
        self.idade = None

    def buscaDados(self):

        while True:
            self.nome = input('Digite o nome: ').strip()

            if self.nome == '':
                print('Você precisa digitar o nome!')
                continue
            break

        while True:
            try:
                self.idade = int(input('Digite a idade: '))

                if self.idade <= 0 :
                    print('A idade deve ser maior que zero!')
                    continue
                break

            except ValueError:
                print('Digite somente numeros em idade!')

while True:
    try:
        quantidade = int(input('Quantas pessoas deseja cadastrar? '))
        if quantidade <= 0:
            print('Dígite um número maior que zero.')
            continue
        break
    except ValueError:
        print('Digite apenas números!')

pessoas = []

for i in range(quantidade):
    print(f'\nCadastro da pessoa {i + 1}')
    pessoa = Pessoa()
    pessoa.buscaDados()
    pessoas.append(pessoa)

print('\nPessoas cadastradas:')
for pessoa in pessoas:
    print(f'Nome: {pessoa.nome} | Idade: {pessoa.idade}')

fim = input('\nPressione Enter para finalizar o programa...')
