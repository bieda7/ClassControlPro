from tkinter import filedialog
from report.pdf.template_base import criar_template
from reportlab.lib.pagesizes import A4
from model.alunos_model import buscarAlunoPorEmail
from tkinter import messagebox


def gerar_relatorio_admin(usuario, total_usuarios, total_turmas):

    caminho = filedialog.asksaveasfilename(
        title="Salvar Relatório Administrativo",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if not caminho:
        return None

    pdf, y = criar_template(caminho, usuario)

    # título do relatório
    y -= 40
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(40, y, "RELATÓRIO ADMINISTRATIVO")

    y -= 30
    pdf.setFont("Helvetica", 12)
    pdf.drawString(40, y, f"Total de usuários cadastrados: {total_usuarios}")

    y -= 20
    pdf.drawString(40, y, f"Total de turmas cadastradas: {total_turmas}")

    pdf.save()
    return caminho



def gerar_relatorio_professor(usuario, total_aulas, total_atividades, total_atividades_status):
    caminho = filedialog.asksaveasfilename(
        title="Salvar Relatório do Professor",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if not caminho:
        return None

    pdf, y = criar_template(caminho, usuario)

    # Título
    y -= 40
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(40, y, "RELATÓRIO DO PROFESSOR")
    y -= 30

    # Quantidades
    pdf.setFont("Helvetica", 12)
    pdf.drawString(40, y, f"Total de aulas cadastradas: {total_aulas}")
    y -= 20
    pdf.drawString(40, y, f"Total de atividades cadastradas: {total_atividades}")
    y -= 40

    pdf.drawString(40, y, "Atividades por status:")
    y -= 20

    for status, total in total_atividades_status.items():
        pdf.drawString(60, y, f"{status}: {total}")
        y -= 20

    pdf.save()
    return caminho



def gerar_relatorio_aluno(usuario, total_atividades_status):
    # Buscar dados do aluno pela tabela ALUNOS
    dados_aluno = buscarAlunoPorEmail(usuario["email"])

    if not dados_aluno:
        messagebox.showerror("Erro", "Não foi possível encontrar dados do aluno na tabela.")
        return None

    matricula = dados_aluno["matricula"]
    turma = dados_aluno["turma"]  # vem da LEFT JOIN

    caminho = filedialog.asksaveasfilename(
        title="Salvar Relatório do Aluno",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if not caminho:
        return None

    pdf, y = criar_template(caminho, usuario)

    # Título
    y -= 40
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(40, y, "RELATÓRIO DO ALUNO")
    y -= 30

    pdf.setFont("Helvetica", 12)

    pdf.drawString(40, y, f"Aluno: {usuario['nome']}")
    y -= 20

    pdf.drawString(40, y, f"Matrícula: {matricula}")
    y -= 20

    pdf.drawString(40, y, f"Turma: {turma}")
    y -= 40

    pdf.drawString(40, y, "Atividades por status:")
    y -= 20

    for status, total in total_atividades_status.items():
        pdf.drawString(60, y, f"{status}: {total}")
        y -= 20

    pdf.save()
    return caminho
