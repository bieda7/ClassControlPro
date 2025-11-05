from model.aulas_model import inserirAulas, listarAulasPorTurma, salvarArquivoAulas, atualizarAulas, deletarAulas
from utils.permissoes import acessos

def cadastrarAulas(tipo_usuario, titulo, descricao, id_turma, data_aula):
    if acessos(tipo_usuario, "aulas", "create"):
       inserirAulas(titulo, descricao, id_turma, data_aula)
       print(f" ✅ Aula cadastrada com sucesso!")
    else:
        print(f"❌ Você não possui permissão para cadastrar aulas!")

def listarTodasAulas(usuario):
    if acessos(usuario, "aulas", "read"):
        aulas = listarAulasPorTurma
        for aula in aulas:
            print(aula)
    else: 
        print("❌ Você não pode listar as aulas!")

def atualizarAulasExistentes(usuario, id_aula, novos_dados):
    if acessos(usuario, "aula", "update"):
        atualizarAulas(id_aula, novos_dados)
        print("✅ Aula atualizada com sucesso!")
    else:
        print("❌ Acesso negado: você não pode atualizar aulas.")

def deletarAulasExistentes(usuario, id_aula):
    if acessos(usuario, "aula", "delete"):
        deletarAulas(id_aula)
        print("✅ Aula deletada com sucesso!")
    else: 
        print("❌ Você não pode deletar aulas!")

