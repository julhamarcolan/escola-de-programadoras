"""
Autor: juliamarcolan@usp.br
Este código faz parte do tópico "Manipulação de Diretórios e Arquivos" da Escola de Programadoras do Instituto Angelim.

Função: Cria uma nova pasta no diretório atual com o nome especificado.

"""
import os

#definindo o nome da pasta 
nome_da_pasta = "exemplo"

#creando a pasta 
os.mkdir(nome_da_pasta)