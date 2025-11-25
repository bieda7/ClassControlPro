from model.conexao import conectar

# Sempre que um usuario cadastrado for do tipo "aluno", o sistema também criará um registro com as mesmas informações na tabela alunos.
# Inseri uma matricula no padrão "ALU...." para cada usuario do tipo aluno.
def inserirAlunoAutomatico(nome, email):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    # Gerar matrícula automática (exemplo simples)
    cursor.execute("SELECT COUNT(*) AS total FROM alunos")
    total = cursor.fetchone()["total"] + 1
    matricula = f"ALU{total:04d}"

    cursor.execute(
        "INSERT INTO alunos (matricula, nome, email) VALUES (%s, %s, %s)",
        (matricula, nome, email)
    )

    conexao.commit()
    conexao.close()


def inserirUsuarios(nome, email, senha, tipo):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute(
        "INSERT INTO usuarios (nome, email, senha, tipo) VALUES (%s, %s, %s, %s)",
        (nome, email, senha, tipo)
    )
    conexao.commit()

    # Criar aluno automaticamente caso o tipo seja "aluno"
    if tipo.lower() == "aluno":
        inserirAlunoAutomatico(nome, email)


def listarUsuarios():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios ")
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

    # Pesquisa usuários através do email

def atualizarUsuarios(id_usuario, novos_dados):
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
        valores.append(id_usuario)
        # Monta a query corretamente
        cursor.execute(f"UPDATE usuarios SET {', '.join(campos)} WHERE id_usuario = %s", valores)
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

def buscarUsuarioPorEmail(email):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    usuario = cursor.fetchone()
    cursor.close()
    conexao.close()
    return usuario
    
    # Deleta usuários do DB 

def deletarUsuarios(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id_usuario,))
    conexao.commit()
    conexao.close()

