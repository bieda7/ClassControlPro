from model.alunos_model import inserirAlunos, listarAlunos, atualizarAlunos, deletarAlunos


def cadastrarAlunos(matricula, nome, email, id_turma):
    inserirAlunos(matricula, nome, email, id_turma)
    return "✅ Aluno cadastrado com sucesso!"

def editarAluno(id_aluno, novos_dados):
    atualizarAlunos(id_aluno, novos_dados)
    return "✅ Aluno atualizado com sucesso!"

def excluirAlunos(id_aluno):
    deletarAlunos(id_aluno)
    return "🗑️ Aluno excluído com sucesso!"

def listarTodosAlunos():
        alunos = listarAlunos()
        return alunos