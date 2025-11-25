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

def registrar_entrega(id_atividade, id_aluno, resposta=None, arquivo_url=None):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        query = """
            INSERT INTO registrar_entrega
            (id_atividade, id_aluno, resposta, arquivo_url, status, data_envio)
            VALUES (%s, %s, %s, %s, 'enviado', NOW())
            ON DUPLICATE KEY UPDATE
                resposta = VALUES(resposta),
                arquivo_url = VALUES(arquivo_url),
                status = 'enviado',
                data_envio = NOW();
        """

        cursor.execute(query, (id_atividade, id_aluno, resposta, arquivo_url))
        conexao.commit()

        return True

    except Exception as e:
        print("Erro ao registrar entrega:", e)
        return False
    
    finally:
        cursor.close()
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

def atualizarNotaEntrega(id_atividade, id_aluno, nota, observacao=None):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        query = """
            UPDATE registrar_entrega
            SET 
                nota = %s,
                observacao = %s,
                status = 'corrigido',
                data_correcao = NOW()
            WHERE id_atividade = %s 
              AND id_aluno = %s;
        """

        cursor.execute(query, (nota, observacao, id_atividade, id_aluno))
        conexao.commit()

        return "Nota registrada com sucesso!"

    except Exception as e:
        print("Erro ao atualizar nota:", e)
        return "Erro ao salvar a nota!"

    finally:
        cursor.close()
        conexao.close()


# NOVO
def listarEntregasProfessor(id_professor):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ra.id_atividade,
            ra.id_aluno,
            a.titulo AS atividade,
            al.nome AS aluno,
            ra.resposta,
            ra.arquivo_url,
            ra.status,
            ra.nota,
            ra.observacao,
            ra.data_envio,
            ra.data_correcao
        FROM registrar_entrega ra
        JOIN atividades a ON a.id_atividade = ra.id_atividade
        JOIN alunos al ON al.id_aluno = ra.id_aluno
        ORDER BY ra.data_envio DESC;
    """)

    return cursor.fetchall()

def listarAtividadesCorrigidasAluno(id_aluno):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ra.id_atividade,
            a.titulo AS titulo,
            a.descricao,
            ra.resposta,
            ra.arquivo_url,
            ra.status,
            ra.nota,
            ra.observacao,
            ra.data_envio,
            ra.data_correcao
        FROM registrar_entrega ra
        JOIN atividades a ON a.id_atividade = ra.id_atividade
        WHERE ra.id_aluno = %s
          AND (ra.status = 'corrigida' OR ra.nota IS NOT NULL)
        ORDER BY ra.data_correcao DESC;
    """, (id_aluno,))

    return cursor.fetchall()





