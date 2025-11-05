from model.conexao import conectar


def inserirUsuarios(nome, email, senha, tipo):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute( 
        "INSERT INTO usuarios (nome, email, senha, tipo) VALUES (%s, %s, %s, %s)", # Comando SQL
        (nome, email, senha, tipo)
    )
    # execute() é responsável por permitir a execução de comandos SQL dentro do código Python
    conexao.commit() # Garante a gravação do usuário no Banco de Dados
    conexao.close()

    # Lista os usuários todos os usuários cadastrados no DB

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
        cursor.execute(f"UPDATE usuários SET {', '.join(campos)} WHERE id_usuario = %s", valores)
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
    cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id_usuario))
    conexao.commit()
    conexao.close()

