from model.alunos_model import inserirAlunos, listarAlunos, atualizarAlunos, deletarAlunos
from utils.permissoes import acessos

def cadastrarAlunos(tipo_usuario, nome, email, matricula, id_turma):
    if acessos(tipo_usuario, "alunos", "create"):
        inserirAlunos(nome, email, matricula, id_turma)
        print("✅ Aluno cadastrado com sucesso!")
    else:
        print("❌ Acesso negado: você não pode criar alunos.")

def listarTodosAlunos(usuario):
    if acessos(usuario, "alunos", "read"):
        alunos = listarAlunos()
        for aluno in alunos:
            print(aluno)
    else:
        print("❌ Acesso negado: você não pode visualizar alunos.")

def atualizarAlunoExistente(id_aluno, novos_dados, usuario):
    if acessos(usuario, "alunos", "update"):
        atualizarAlunos(id_aluno, novos_dados)
        print("✅ Aluno atualizado com sucesso!")
    else:
        print("❌ Acesso negado: você não pode atualizar alunos.")

def excluirAlunos(id_aluno, usuario):
    if acessos(usuario, "alunos", "delete"):
        deletarAlunos(id_aluno)
        print("🗑️ Aluno excluído com sucesso!")
    else:
        print("❌ Acesso negado: você não pode excluir alunos.")
