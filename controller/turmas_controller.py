from model.turmas_model import inserirTurmas, listarTurmas, atualizarTurmas, deletarTurmas, listarProfessoresDaTurma
from utils.permissoes import acessos

# === Cadastrar Turmas ===
def cadastrarTurmas(nome):
    inserirTurmas(nome)
    return "✅ Turma cadastrada com sucesso!"

# === Listar Todas as Turmas ===
def listarTodasTurmas():
    turmas = listarTurmas()
    return turmas  # retorna lista de turmas mesmo que vazia

# === Editar Turmas ===
def editarTurmas(id_turma, dados):
    atualizarTurmas(id_turma, dados)
    return "✅ Turma atualizada com sucesso!"

# === Exibir Professores de uma Turma ===
def exibirProfessoresDaTurma(id_turma):
    professores = listarProfessoresDaTurma(id_turma)
    return professores  # retorna lista de professores

# === Excluir Turmas ===
def excluirTurmas(id_turma):
    deletarTurmas(id_turma)
    return "🗑️ Turma excluída com sucesso!"

def contarTurmas():
    turmas = listarTodasTurmas()
    return len(turmas)