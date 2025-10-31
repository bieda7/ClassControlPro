from model.conexao import conectar

def inserirAtividades(titulo, descricao, data_entrega, id_aula):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        "INSERT INTO atividades (titulo, descricao, data_entrega, id_aula) VALUES (%s, %s, %s, %s)"
        (titulo, descricao, data_entrega, id_aula)
    )
    cursor.commit()
    cursor.close()

def listarAtividadePorAula(id_aula):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT id_atividade, titulo, descricao ,data_estrega FROM  aulas WHERE id_aula = %s", (id_aula,))
    atividades = cursor.fetchall()
    cursor.close()
    return atividades

def registrarEntrega(id_atividade, id_aluno, status='em andamento', nota=None):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        "INSERT INTO atividades_alunos (id_atividade, id_aluno, status, nota) VALUES (%s, %s, %s, %s)"
        (id_atividade, id_aluno, status, nota)
        )
    cursor.commit()
    cursor.close()

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