import dados as bd


professores = {}
alunos = {}
disciplinas = {}
notas = {}
dados_notas = []
lista_aux = []

def iniciaDicionarios():
    global professores, alunos,disciplinas,notas
    for p in bd.carregarDadosProfessores():
        professores[p[0]] = {'nome': p[1], 'data_nascimento': p[2]}
    for a in bd.carregarDadosAlunos():
        alunos[a[0]] = {'nome': a[1], 'data_nascimento': a[2]}
    for d in bd.carregarDadosDisciplinas():
        disciplinas.update({d[0]:{d[1], d[2]}})
        disciplinas[d[0]] = {'nome_disciplina':d[1], 'matricula_professor': d[2]}
    for n in bd.carregarDadosNotas():
        notas.update({n[0]:{n[1], n[2], n[3], n[4]}})
        notas[n[0]] = {'matricula_aluno': n[0] , 'codigo_disciplinas': n[1], 'nota_01': n[2], 'nota_02': n[3], 'media': n[4]}










class Escola:
    def __init__(self):
        global alunos, professores
        iniciaDicionarios()
        print('👍👍👍')
        print(alunos, professores, disciplinas, notas)
        pass

    def cadastrar_de_professores(self, nome, matricula, data_nascimento):
        global professores
        if matricula not in professores:
            professores[matricula] = {'nome': nome, 'data_nascimento': data_nascimento}
            return print(professores)
        return print('Error ❌! Matrícula já cadastrada.')

    def cadastrar_alunos(self, nome, matricula, data_nascimento):
        global alunos
        if matricula not in alunos:
            alunos[matricula] = {'nome': nome, 'data_nascimento': data_nascimento}
            return
        return print('Error ❌! Matrícula já cadastrada.')

    def cadastrar_de_diciplinas(self, codigo_disciplina, nome_disciplina, matricula_professor):
        global professores, disciplinas
        if matricula_professor in professores:
            if codigo_disciplina not in disciplinas:
                disciplinas[codigo_disciplina] = {'nome_disciplina': nome_disciplina, 'matricula_professor': matricula_professor}
                print(disciplinas)
                return
            return print('Disciplina já cadastrada!')
        print('Error ❌! Matrícula do professor não cadastrada.')
        return

    def cadastrar_notas(self, codigo_disciplina, matricula_aluno, nota_01, nota_02):
        global alunos, disciplinas, notas, dados_notas, lista_aux
        if matricula_aluno in alunos.keys():
            lista_aux = []
            if codigo_disciplina in disciplinas:
                media = round(((nota_01 + nota_02) / 2), 2)
                if matricula_aluno not in notas.keys():
                    lista_aux.append({'matricula_aluno': matricula_aluno, 'codigo_disciplinas': codigo_disciplina,
                                      'nota_01': nota_01, 'nota_02': nota_02, 'media': media})
                    notas.update({matricula_aluno: lista_aux})
                    print(notas)
                    return print('Nota cadastrada com sucesso!!')
                for nota in notas[matricula_aluno]:
                    lista_aux.append(nota)
                lista_aux.append(
                    {'matricula_aluno': matricula_aluno, 'codigo_disciplinas': codigo_disciplina, 'nota_01': nota_01,
                     'nota_02': nota_02, 'media': media})
                notas.update({matricula_aluno: lista_aux})
            print(notas)
            return print('Disciplina não cadastrada!')
        return print('Error ❌! Matrícula não cadastrada.')

    def relatorio_notas(self, codigo_disciplina):
        global disciplinas, notas, professores, alunos
        if codigo_disciplina in disciplinas: #não faz diferença .keys() :(
            print(f"Disciplina: {disciplinas[codigo_disciplina]['nome_disciplina']}\nProfessor: {disciplinas[codigo_disciplina]['matricula_professor']}")
            for aluno in alunos.keys():
                if aluno in notas.keys():
                    for i in notas[aluno]:
                        if i['codigo_disciplinas'] == codigo_disciplina:
                            print(f"Matrícula: {aluno} - Nota 1: {i['nota_01']} Nota 2: {i['nota_02']} Média : {i['media']}")
            return
        return print('Disciplina não cadastrada!')




###class BasedeDados:
    #def __init__(self):
        #pass

