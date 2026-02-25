# Sistema-de-cadastro-simples-em-python

Sistema de Cadastro de Pessoas Simples em Python
Resumo

Este trabalho apresenta o desenvolvimento de um sistema simples de cadastro de pessoas utilizando a linguagem Python e os princípios da Programação Orientada a Objetos (POO). O sistema permite o cadastro de múltiplos indivíduos, realizando a validação dos dados de entrada e armazenando as informações em memória durante a execução do programa.

1. Introdução

A Programação Orientada a Objetos é um paradigma amplamente utilizado no desenvolvimento de software moderno, pois permite maior organização, reutilização e manutenção do código. Neste contexto, o presente projeto tem como objetivo aplicar conceitos fundamentais da POO, como classes, objetos, atributos e métodos, por meio da implementação de um sistema de cadastro de pessoas.

2. Objetivos
2.1 Objetivo Geral

Desenvolver um sistema de cadastro de pessoas em Python, utilizando Programação Orientada a Objetos.

2.2 Objetivos Específicos

Criar uma classe que represente uma pessoa

Solicitar dados ao usuário via terminal

Validar entradas de nome e idade

Armazenar os dados em uma estrutura de dados adequada

Exibir os registros cadastrados ao final da execução

3. Metodologia

O sistema foi desenvolvido em Python, utilizando estruturas de repetição, tratamento de exceções e Programação Orientada a Objetos. Os dados são coletados por meio de entradas do usuário no terminal e armazenados em uma lista, que funciona como um banco de dados em memória.

4. Estrutura do Sistema
4.1 Classe Pessoa

A classe Pessoa representa o modelo de uma pessoa dentro do sistema.

Atributos:

nome (str): armazena o nome da pessoa

idade (int): armazena a idade da pessoa

Métodos:

__init__(): inicializa os atributos da classe

buscaDados(): solicita e valida os dados do usuário

4.2 Validação dos Dados

O sistema realiza as seguintes validações:

O nome não pode ser vazio

A idade deve ser um número inteiro positivo

Entradas inválidas são tratadas por meio de exceções (try/except)

5. Funcionamento do Sistema

O fluxo de execução do programa ocorre conforme as etapas abaixo:

O usuário informa a quantidade de pessoas a serem cadastradas

Para cada pessoa:

Um objeto da classe Pessoa é criado

O método buscaDados() é executado

Os dados são armazenados em uma lista

Após o cadastro de todas as pessoas, o sistema exibe os registros cadastrados

6. Tecnologias Utilizadas

Linguagem de Programação: Python 3

Paradigma: Programação Orientada a Objetos

Ambiente de Execução: Terminal/Console

7. Resultados

O sistema atende aos objetivos propostos, permitindo o cadastro de múltiplas pessoas com validação adequada dos dados. A utilização de Programação Orientada a Objetos torna o código organizado, reutilizável e de fácil manutenção.

8. Considerações Finais

Este projeto possibilitou a aplicação prática dos conceitos fundamentais de Programação Orientada a Objetos em Python. O sistema pode ser expandido futuramente para incluir funcionalidades adicionais, como persistência de dados em arquivos, edição e remoção de registros, e criação de um menu interativo.

9. Trabalhos Futuros

Implementação de CRUD completo

Armazenamento em arquivos ou banco de dados

Criação de interface gráfica ou menu interativo

Separação do código em módulos
