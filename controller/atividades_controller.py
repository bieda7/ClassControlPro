from model.atividades_model import inserirAtividades, listarAtividades, confirmarEntrega, atualizarAtividades, deletarAtividades


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
def registrarEntrega(id_atividade, id_usuario, status, nota=None, dia_entrega=None, observacao=None):
    confirmarEntrega(id_atividade, id_usuario, status, nota, dia_entrega, observacao)
    return "✅ Entrega de atividade registrada com sucesso!"




