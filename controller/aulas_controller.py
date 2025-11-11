from model.aulas_model import inserirAulas, listarAulasPorTurma, salvarArquivoAulas, atualizarAulas, deletarAulas

def cadastrarAulas(titulo, descricao, id_turma, data_aula):
       inserirAulas(titulo, descricao, id_turma, data_aula)
       return f" ✅ Aula cadastrada com sucesso!"

def listarTodasAulas():
        aulas = listarAulasPorTurma
        return aulas

def editarAulas(id_aula, novos_dados):
        atualizarAulas(id_aula, novos_dados)
        return f" ✅ Aula atualizada com sucesso!"

def deletarAulasExistentes(id_aula):
        deletarAulas(id_aula)
        return f"✅ Aula deletada com sucesso!"


