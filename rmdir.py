"""
Autor: juliamarcolan@usp.br
Este código faz parte do tópico "Manipulação de Diretórios e Arquivos" da Escola de Programadoras do Instituto Angelim.

Função: Deleta uma nova pasta no diretório atual com o nome especificado utilizando a biblioteca os. 

"""
import os

#definindo o nome da pasta 
nome_da_pasta = "exemplo"

#creando a pasta 
os.rmdir(nome_da_pasta)