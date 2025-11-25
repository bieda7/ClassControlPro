from model.relatorios_model import totalTurmas, totalUsuarios, totalAulas, totalAtividades, totalAtividadesPorStatus
from report.pdf.relatorios import gerar_relatorio_admin, gerar_relatorio_professor, gerar_relatorio_aluno
from model.alunos_model import buscarAlunoPorEmail
from tkinter import messagebox

def gerarRelatorioAdmin(usuario):
    t_turmas = totalTurmas()
    t_usuarios = totalUsuarios()

    caminho = gerar_relatorio_admin(usuario, t_turmas, t_usuarios)
    return caminho

def gerarRelatorioProf(usuario):
    t_aulas = totalAulas()
    t_atividades = totalAtividades()
    t_atividades_por_status = totalAtividadesPorStatus()

    caminho = gerar_relatorio_professor(usuario, t_aulas, t_atividades, t_atividades_por_status)
    return caminho

    
def gerarRelatorioAluno(usuario):
    # Puxa o total de atividades por status (pendente, concluída, atrasada...)
    total_atividades_status = totalAtividadesPorStatus()

    # Gera o relatório, agora com a assinatura correta da função
    caminho = gerar_relatorio_aluno(usuario, total_atividades_status)

    return caminho

from model.relatorios_model import (
    totalUsuarios,
    totalTurmas,
    totalAtividades,
    totalAulas)

def obter_totais_dashboard():
    return {
        "usuarios": totalUsuarios(),
        "turmas": totalTurmas(),
        "atividades": totalAtividades(),
        "aulas": totalAulas()
    }



