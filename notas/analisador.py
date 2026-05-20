import csv


with  open('Pasta1.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados =list(map(list, leitor))
    print(dados)
