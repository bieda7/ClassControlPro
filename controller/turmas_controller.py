from model.turmas_model import inserirTurmas, listarTurmas, atualizarTurmas, deletarTurmas, listarProfessoresDaTurma
from utils.permissoes import acessos

def cadastrarTurmas(tipo_usuario, nome):
    if acessos(tipo_usuario, "turmas", "create"):
        inserirTurmas(nome)
        print("✅ Turma cadastrada com sucesso!")
    else:
        print("❌ Acesso negado: você não pode criar turmas.")

def listarTodasTurmas(usuario):
    if acessos(usuario, "turmas", "read"):
        turmas = listarTurmas()
        for turma in turmas:
            print(turma)
    else:
        print("❌ Acesso negado: você não pode visualizar turmas.")

def atualizarTurmaExistente(id_turma, novos_dados, usuario):
    if acessos(usuario, "turmas", "update"):
        atualizarTurmas(id_turma, novos_dados)
        print("✅ Turma atualizada com sucesso!")
    else:
        print("❌ Acesso negado: você não pode atualizar turmas.")

def exibirProfessoresDaTurma(id_turma, usuario):
    if acessos(usuario, "turmas", "read"):
        professores = listarProfessoresDaTurma(id_turma)
        if professores:
            print(f"👨‍🏫 Professores da Turma {id_turma}:")
            for p in professores:
                print(f"- {p['nome']} ({p['email']})")
        else:
            print("⚠️ Nenhum professor associado a esta turma.")
    else:
        print("❌ Acesso negado: você não pode visualizar professores desta turma.")

def excluirTurmas(id_turma, usuario):
    if acessos(usuario, "turmas", "delete"):
        deletarTurmas(id_turma)
        print("🗑️ Turma excluída com sucesso!")
    else:
        print("❌ Acesso negado: você não pode excluir turmas.")

