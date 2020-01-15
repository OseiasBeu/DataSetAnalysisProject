import re

#leitura de um arquivo
titanic_csv = open('2- Dados preparados/titanic.csv','r')
linhas =titanic_csv.readlines()

# print(linhas[0])
# print(linhas[1])


#Utilizamos o método split para separar as colunas por virgula

print(type(linhas[0]))
colunas = linhas[0].split(',')

print(colunas[2]) #Lista de strings
print(colunas)

#Dados

dados = linhas[1].split(',')
print(dados)


#Cada coluna será a chave e os valors uma lista 
#EX.: Name: [name1,name2,name3,name4 ...]

print(len(colunas), len(dados))

print(colunas[0])
print(dados[0])

math = re.compile(r)