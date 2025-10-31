from model.atividades_model import inserirAtividades, listarAtividadePorAula, registrarEntrega, atualizarAtividades, deletarAtividades
from utils.permissoes import acessos

# Cadastra atividades
def cadastrarAtividades(usuario, titulo, descricao, data_entrega, id_aula):
    if acessos(usuario, "atividade", "create"):
       inserirAtividades(titulo,descricao, data_entrega, id_aula)
       print("✅ Atividade criada com sucesso!")
       return True 
    else:
       print("❌ Você não possui permissão para cadastrar atividades!")
       return False
# Lista atividades relacionadas a aula especificada 
def listarAtividadesDaAula(id_aula, usuario):
    if acessos(usuario, "atividades", "read"):
        atividades = listarAtividadePorAula(id_aula)
        if atividades:
            print(f"📚 Atividades da Aula {id_aula}:")
            for a in atividades:
                print(f"- {a['titulo']} (Entrega: {a['data_entrega']})")
        else:
            print("Nenhuma atividade encontrada para esta aula.")
    else:
        print("❌ Acesso negado: você não tem permissão para visualizar atividades.")

def atualizarAtividadeExistente(id_atividade, novos_dados, usuario):
    if acessos(usuario, "atividades", "update"):
        atualizarAtividades(id_atividade, novos_dados)
        print("✅ Atividade atualizada com sucesso!")
    else:
        print("❌ Acesso negado: você não pode atualizar atividades.")

def excluirAtividades(id_atividade, usuario):
    if acessos(usuario, "atividades", "delete"):
        deletarAtividades(id_atividade)
        print("🗑️ Atividade excluída com sucesso!")
    else:
        print("❌ Acesso negado: você não pode excluir atividades.")



