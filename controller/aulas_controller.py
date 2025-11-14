from model.aulas_model import inserirAulas, listarAulas, salvarArquivoAulas, atualizarAulas, deletarAulas

def cadastrarAulas(titulo, descricao, data_aula):
       inserirAulas(titulo, descricao, data_aula)
       return f" ✅ Aula cadastrada com sucesso!"

def listarTodasAulas():
        return listarAulas() 

def editarAulas(id_aula, novos_dados):
        atualizarAulas(id_aula, novos_dados)
        return f" ✅ Aula atualizada com sucesso!"

def deletarAulasExistentes(id_aula):
        deletarAulas(id_aula)
        return f"✅ Aula {id_aula} deletada com sucesso!"


