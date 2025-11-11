from model.atividades_model import inserirAtividades, listarAtividadePorAula, confirmarEntrega, atualizarAtividades, deletarAtividades


# === Cadastrar Atividades ===
def cadastrarAtividades(titulo, descricao, data_entrega, id_aula):
    inserirAtividades(titulo, descricao, data_entrega, id_aula)
    return "✅ Atividade criada com sucesso!"

# === Listar Atividades de uma Aula ===
def listarAtividadesDaAula(id_aula):
    atividades = listarAtividadePorAula(id_aula)
    return atividades  # retorna lista de atividades, mesmo que vazia

# === Editar Atividades ===
def editarAtividades(id_atividade, novos_dados):
    atualizarAtividades(id_atividade, novos_dados)
    return "✅ Atividade atualizada com sucesso!"

# === Excluir Atividades ===
def excluirAtividades(id_atividade):
    deletarAtividades(id_atividade)
    return "🗑️ Atividade excluída com sucesso!"

# === Registrar Entrega de Atividade ===
def registrarEntrega(id_atividade, id_aluno, status, nota=None, dia_entrega=None, observacao=None):
    confirmarEntrega(id_atividade, id_aluno, status, nota, dia_entrega, observacao)
    return "✅ Entrega de atividade registrada com sucesso!"




