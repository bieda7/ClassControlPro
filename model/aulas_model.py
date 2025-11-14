from model.conexao import conectar

    # Cadastro de aulas no DB
def inserirAulas(titulo, descricao, data_aula):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("INSERT INTO aulas (titulo, descricao, data_aula) VALUES (%s, %s, %s)",
                   (titulo, descricao, data_aula)
    )
    conexao.commit()
    conexao.close()

    # Lista Aulas referentes a cada turma
    
def listarAulas():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM aulas ORDER BY id_aula DESC")
    aulas = cursor.fetchall()  # ✅ deve ser fetchall, não fetchone
    conexao.close()
    return aulas

def atualizarAulas(id_aula, novos_dados):
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

        # Adiciona o id_aula no final da lista de valores
        valores.append(id_aula)
        # Monta a query corretamente
        cursor.execute(f"UPDATE aulas SET {', '.join(campos)} WHERE id_aula = %s", valores)
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

def salvarArquivoAulas(id_aula, nome_arquivo, caminho_arquivo):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        "INSERT INTO arquivo_aula (id_aula, nome_arquivo, caminho_arquivo) VALUE (%s, %s, %s)",
       (id_aula, nome_arquivo, caminho_arquivo)
    )
    cursor.commit()
    cursor.close()

def deletarAulas(id_aula):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM aulas WHERE id_aula = %s", (id_aula,))
    conexao.commit()
    conexao.close()
