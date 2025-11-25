from model.atividades_model import inserirAtividades, listarAtividades, registrar_entrega, atualizarAtividades, deletarAtividades


# === Cadastrar Atividades ===
def cadastrarAtividades(titulo, descricao, data_entrega):
    inserirAtividades(titulo, descricao, data_entrega)
    return "✅ Atividade criada com sucesso!"

# === Listar Atividades de uma Aula ===
def listarTodasAtividades():
    atividades = listarAtividades()
    return atividades  # retorna lista de atividades, mesmo que vazia

# === Editar Atividades ===
def editarAtividades(id_atividade, novos_dados):
    atualizarAtividades(id_atividade, novos_dados)
    return "✅ Atividade atualizada com sucesso!"

# === Excluir Atividades ===
def excluirAtividades(id_atividade):
    deletarAtividades(id_atividade)
    return f"🗑️ Atividade {id_atividade} excluída com sucesso!"

# === Registrar Entrega de Atividade ===
# aluno entrega atividade
from model.atividades_model import registrar_entrega

def enviarEntregaAluno(id_atividade, id_aluno, resposta, arquivo_url):
    if not resposta and not arquivo_url:
        return "❌ Você deve enviar uma resposta ou um arquivo."

    sucesso = registrar_entrega(id_atividade, id_aluno, resposta, arquivo_url)

    if sucesso:
        return "✅ Entrega enviada com sucesso!"
    else:
        return "❌ Erro ao enviar entrega."




