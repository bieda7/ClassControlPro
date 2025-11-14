from model.conexao import conectar
from datetime import date

def inserirAtividades(titulo, descricao, data_entrega):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        "INSERT INTO atividades (titulo, descricao, data_entrega) VALUES (%s, %s, %s)",
        (titulo, descricao, data_entrega)
    )
    conexao.commit()
    conexao.close()

def listarAtividades():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM atividades ")
    atividades = cursor.fetchall()
    cursor.close()
    return atividades

def confirmarEntrega(id_atividade, id_usuario, dia_entrega, observacao, status='em andamento', nota=None):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        "INSERT INTO registrar_entrega (id_atividade, id_usuario, status, nota, data_entrega, observacao) VALUES (%s, %s, %s, %s, %s, %s)",
        (id_atividade, id_usuario, status, nota, dia_entrega, observacao)
        )
    conexao.commit()
    conexao.close()

def atualizarAtividades(id_atividade, novos_dados):
    conexao = None
    cursor = None
   
    # Atualiza os campos de uma atividade existente no banco de dados.
    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        campos = []
        valores = []

        for campo, valor in novos_dados.items():
            campos.append(f"{campo} = %s")
            valores.append(valor)

        # Adiciona o id_aluno no final da lista de valores
        valores.append(id_atividade)
        # Monta a query corretamente
        cursor.execute(f"UPDATE atividades SET {', '.join(campos)} WHERE id_atividade = %s", valores)
        conexao.commit()
        

    except Exception as e:
        print("Tipo de erro: ", type(e).__name__)
        print(f"❌ Não foi possível realizar a atualização dos dados. Erro: {e}")
        if conexao:
            conexao.rollback()
   
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def deletarAtividades(id_atividade):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("DELETE FROM atividades WHERE id_atividade = %s", (id_atividade,))
    conexao.commit()
    conexao.close()