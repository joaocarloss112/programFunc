import csv

with open('Pasta1.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=';')
    dados = list(map(dict, leitor))
alunos = list(map(
    lambda x: {
        'nome': x['nome'], 
        'notas': list(map(float, [x['nota1'], x['nota2'], x['nota3'], x['nota4']]))
    }, 
    dados))

print(alunos)

MediaAlunos = list(map(lambda x: {
    'nome': x['nome'], 
    'media': sum(x['notas']) / len(x['notas'])
},alunos))

print(MediaAlunos)
