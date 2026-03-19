aluno1 = {"nome": "Jéssica", "idade": 22, "notas": [6, 4.5, 4]}
aluno2 = {"nome": "Caique", "idade": 22, "notas": [4.5, 9.5, 9]}
aluno3 = {"nome": "Geovanna", "idade": 24, "notas": [8, 6, 10]}

alunos = [aluno1, aluno2, aluno3]

for aluno in alunos:
    media = sum(aluno["notas"]) / 3
    print(f'{aluno["nome"]} - {media}')
