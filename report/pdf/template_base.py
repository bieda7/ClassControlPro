from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader

LOGO_PATH = "view\components\logotipo-classcontrolpro.png"  # coloque seu caminho real

def criar_template(caminho, usuario):
    pdf = canvas.Canvas(caminho, pagesize=A4)
    largura, altura = A4

    y = altura - 80

    # LOGO
    try:
        logo = ImageReader(LOGO_PATH)
        pdf.drawImage(logo, 40, altura - 120, width=80, height=80, preserveAspectRatio=True, mask="auto")
    except:
        pass  # caso não tenha logo

    # Nome do sistema
    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawCentredString(largura / 2, y, "ClassControlPro")

    # Mensagem padrão
    y -= 30
    pdf.setFont("Helvetica", 12)
    pdf.drawCentredString(largura / 2, y, "Relatório gerado automaticamente pelo sistema.")

    # Nome do usuário
    nome_user = usuario.get("nome", "Usuário")
    y -= 30
    pdf.setFont("Helvetica", 12)
    pdf.drawString(40, y, f"Gerado por: {nome_user}")

    # Data
    from datetime import datetime
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    pdf.drawString(350, y, f"Data: {data}")

    # Linha divisória
    y -= 20
    pdf.line(40, y, largura - 40, y)

    # Retorna o PDF + posição atual do Y para continuar escrevendo
    return pdf, y
