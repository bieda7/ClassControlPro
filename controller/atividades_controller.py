from model.atividades_model import inserirAtividades, listarAtividadePorAula, confirmarEntrega, atualizarAtividades, deletarAtividades
from utils.permissoes import acessos

# Cadastra atividades
def cadastrarAtividades(tipo_usuario, titulo, descricao, data_entrega, id_aula):
    if acessos(tipo_usuario, "atividades", "create"):
       inserirAtividades(titulo, descricao, data_entrega, id_aula)
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
                return True
        else:
            print("Nenhuma atividade encontrada para esta aula.")
            return False
    else:
        print("❌ Acesso negado: você não tem permissão para visualizar atividades.")
        return False
    
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
        return True
    else:
        print("❌ Acesso negado: você não pode excluir atividades.")
        return False
    
def registrarEntrega(tipo_usuario, id_atividade, id_aluno, status, nota, dia_entrega, observacao):
    if acessos(tipo_usuario, 'atividades', 'grade'):
        confirmarEntrega(id_atividade, id_aluno, status, nota, dia_entrega, observacao)
        print("✅ Entrega de atividade registrada com sucesso!")
        return True    
    else:
       print("❌ Você não pode registrar entregas de atividades!")
       return False


