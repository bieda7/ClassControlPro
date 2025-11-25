from model.conexao import conectar
from datetime import date, datetime

def totalTurmas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM turmas")
    resultado = cursor.fetchone()[0]
    conexao.close()
    return resultado

def totalUsuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    resultado = cursor.fetchone()[0]
    conexao.close()
    return resultado

def totalAulas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM aulas")
    resultado = cursor.fetchone()[0]
    conexao.close()
    return resultado

def totalAtividades():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM atividades")
    resultado = cursor.fetchone()[0]
    conexao.close()
    return resultado

def totalAtividadesPorStatus():
    """
    Retorna a quantidade de atividades por status:
    Pendente, Em andamento, Em atraso
    """
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT data_criacao, data_entrega FROM atividades")
    atividades = cursor.fetchall()

    hoje = date.today()
    totais = {
        "Pendente": 0,
        "Em andamento": 0,
        "Em atraso": 0
    }

    for atividade in atividades:
        data_criacao = atividade['data_criacao']
        data_entrega = atividade['data_entrega']

        # Converte strings para date, se necessário
        if isinstance(data_criacao, str):
            data_criacao = datetime.strptime(data_criacao, "%Y-%m-%d").date()
        if isinstance(data_entrega, str):
            data_entrega = datetime.strptime(data_entrega, "%Y-%m-%d").date()

        # Lógica de status dinâmica
        if hoje < data_criacao:
            status = "Pendente"
        elif data_criacao <= hoje <= data_entrega:
            status = "Em andamento"
        else:
            status = "Em atraso"

        totais[status] += 1

    

    conexao.close()
    return totais