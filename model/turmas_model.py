from model.conexao import conectar

    # Cadastra turmas no DB
def inserirTurmas(nome):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("INSERT INTO turmas (nome) VALUES (%s)", (nome,))
    conexao.commit()
    conexao.close()

    # Lista as turmas cadastradas no DB

def listarTurmas():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT id_turma, nome FROM turmas")
    turmas = cursor.fetchall()
    conexao.close()
    return turmas

    # Associa professores a turmas

def associarProfessor(id_turma, id_professor):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    # Evita duplicidade
    cursor.execute("""
        SELECT * FROM turmas_Professores
        WHERE id_turma = %s AND id_professor = %s
    """, (id_turma, id_professor))

    if cursor.fetchone():
        print("⚠️ Este professor já está associado a esta turma.")
        conexao.close()
        return

    cursor.execute(
        "INSERT INTO turmas_Professores (id_turma, id_professor) VALUES (%s, %s)",
        (id_turma, id_professor)
    )
    conexao.commit()
    conexao.close()
    print("✅ Professor associado à turma com sucesso!")

def atualizarTurmas(id_turma, dados):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        campos = []
        valores = []

        for campo, valor in dados.items():
            campos.append(f"{campo} = %s")
            valores.append(valor)

        # Adiciona o id_aluno no final da lista de valores
        valores.append(id_turma)
        # Monta a query corretamente
        cursor.execute(f"UPDATE turmas SET {', '.join(campos)} WHERE id_turma = %s", valores)
        conexao.commit()
        return True

    except Exception as e:
        print("Tipo de erro: ", type(e).__name__)
        print(f"❌ Não foi possível realizar a atualização dos dados. Erro: {e}")
        if conexao:
            conexao.rollback()
        return False
    
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def listarProfessoresDaTurma(id_turma):
    # Retorna todos os professores associados a uma turma específica.
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT u.id_usuario, u.nome, u.email FROM turmas_professores tp JOIN usuarios u ON tp.id_professor = u.id_usuario WHERE tp.id_turma = %s"(id_turma,))
    professores = cursor.fetchall()
    conexao.close()
    return professores

def deletarTurmas(id_turma):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("DELETE FROM turmas WHERE id_turma = %s", (id_turma,))
    conexao.commit()
    conexao.close()
