from model.conexao import conectar

     
def inserirAlunos(matricula, nome, email, id_turma):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        "INSERT INTO alunos (matricula, nome, email, id_turma) VALUES (%s, %s, %s, %s)",
        (matricula ,nome, email, id_turma)
    )
    conexao.commit()
    conexao.close()

def listarAlunos():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("""
        SELECT 
            a.id_aluno,
            a.nome,
            a.email,
            a.matricula,
            t.nome AS turma
        FROM alunos a
        LEFT JOIN turmas t ON a.id_turma = t.id_turma
    """)
    alunos = cursor.fetchall()
    conexao.close()
    return alunos

def atualizarAlunos(id_aluno, novos_dados):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        campos = []
        valores = []

        for campo, valor in novos_dados.items():
            campos.append(f"{campo} = %s")
            valores.append(valor)

        # Adiciona o id_aluno no final da lista de valores
        valores.append(id_aluno)
        # Monta a query corretamente
        cursor.execute(f"UPDATE alunos SET {', '.join(campos)} WHERE id_aluno = %s", valores)
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

def listarAlunosPorTurma(id_turma):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT id_aluno, nome, email FROM alunos WHERE id_turma = %s", (id_turma,))
    alunos = cursor.fetchall()
    conexao.close()
    return alunos

def deletarAlunos(id_aluno):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("DELETE FROM alunos WHERE id_aluno = %s", (id_aluno,))
    conexao.commit()
    conexao.close()

def buscarAlunoPorID(id_aluno):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            a.id_aluno,
            a.nome,
            a.email,
            a.matricula,
            t.nome AS turma
        FROM alunos a
        LEFT JOIN turmas t ON a.id_turma = t.id_turma
        WHERE a.id_aluno = %s
    """, (id_aluno,))

    aluno = cursor.fetchone()
    conexao.close()
    return aluno

def buscarAlunoPorEmail(email):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("""
        SELECT 
            a.id_aluno,
            a.matricula,
            a.nome,
            a.email,
            a.id_turma,
            t.nome AS turma
        FROM alunos a
        LEFT JOIN turmas t ON t.id_turma = a.id_turma
        WHERE a.email = %s
    """, (email,))
    
    aluno = cursor.fetchone()
    conexao.close()
    return aluno

def buscarMatriculaETurmaPorEmail(email):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("""
        SELECT 
            a.matricula,
            t.nome AS turma
        FROM alunos a
        LEFT JOIN turmas t ON t.id_turma = a.id_turma
        WHERE a.email = %s
    """, (email,))
    
    dados = cursor.fetchone()
    conexao.close()
    return dados

def buscarIdAlunoPorUsuario(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT a.id_aluno
        FROM alunos a
        JOIN usuarios u ON u.email = a.email
        WHERE u.id_usuario = %s
    """, (id_usuario,))

    resultado = cursor.fetchone()
    conexao.close()

    return resultado["id_aluno"] if resultado else None

def buscarAlunoPorUsuario(email):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT id_aluno, nome, id_turma
        FROM alunos
        WHERE email = %s
    """, (email,))

    return cursor.fetchone()


