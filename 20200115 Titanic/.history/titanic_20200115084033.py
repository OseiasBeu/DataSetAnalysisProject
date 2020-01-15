#leitura de um arquivo
titanic_csv = open('2- Dados preparados/titanic.csv','r')
linhas =titanic_csv.readlines()

print(linhas[0])
print(linhas[1])


#Utilizamos o método split para separar as colunas por virgula

print(type(linhas[0]))
colunas = linhas[0].split(',')

print(colunas[2]) #Lista de strings


#Cada coluna será a chave e os valors uma lista 
#EX.: Name: [name1,name2,name3,name4 ...]

