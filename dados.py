import sqlite3
conn = sqlite3.connect('bancodedados.db')
cursor = conn.cursor()


def carregarDadosAlunos():
    global conn
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alunos')
    listaAlunos = cursor.fetchall()

    cursor.close()
    return listaAlunos

def carregarDadosProfessores():
    global conn
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM professores')
    listaProfessores = cursor.fetchall()

    cursor.close()
    return listaProfessores

def carregarDadosDisciplinas():
    global conn
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM disciplinas')
    listaDisciplinas = cursor.fetchall()

    cursor.close()
    return listaDisciplinas

def carregarDadosNotas():
    global conn
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM notas')
    listaNotas = cursor.fetchall()
    print(listaNotas)
    cursor.close()
    return listaNotas
