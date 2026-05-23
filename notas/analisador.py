import csv

with open('Pasta1.csv', 'r') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=';')
    dados = list(leitor)
alunos = list(map(
    lambda x: {
        'nome': x['nome'],
        'extra': int(x['extra']),
        'notas': list(map(float, [x['nota1'], x['nota2'], x['nota3'], x['nota4']]))
    }, 
    dados))

#print(alunos)

MediaAlunos = list(map(lambda x: {
    'nome': x['nome'],
    'media': min(sum(x['notas']) / len(x['notas'])+ 1 if x['extra'] == 1 else sum(x['notas']) / len(x['notas']),10)
},alunos))

aprovados = list(filter(lambda x: x['media'] >=7, MediaAlunos))
reprovados = list(filter(lambda x: x['media'] <7, MediaAlunos))

print(aprovados)
print(reprovados)

print(MediaAlunos)
