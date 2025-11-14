import customtkinter as ctk
from tkinter import messagebox

from controller.usuarios_controller import cadastrarUsuarios, editarUsuarios, excluirUsuarios, listarTodosUsuarios
from controller.turmas_controller import cadastrarTurmas, editarTurmas, excluirTurmas
from controller.aulas_controller import cadastrarAulas, editarAulas, deletarAulasExistentes
from controller.atividades_controller import cadastrarAtividades, editarAtividades, excluirAtividades, registrarEntrega

from datetime import datetime

import customtkinter as ctk
from tkinter import messagebox

from view.ui_config import COLORS, get_fonts



# -----------------------------
# ===== FORMULÁRIOS DE USUÁRIOS
# -----------------------------

def form_cadastrar_usuario(parent, callback_atualizar):
    """
    Formulário para cadastrar novo usuário
    """
    janela = ctk.CTkToplevel(parent)
    janela.title("Cadastrar Usuário")
    janela.geometry("400x300")

    ctk.CTkLabel(janela, text="Cadastrar Usuário", font=("Arial", 16, "bold")).pack(pady=10)

    nome_entry = ctk.CTkEntry(janela, placeholder_text="Nome")
    nome_entry.pack(pady=5)

    email_entry = ctk.CTkEntry(janela, placeholder_text="E-mail")
    email_entry.pack(pady=5)

    senha_entry = ctk.CTkEntry(janela, placeholder_text="Senha")
    senha_entry.pack(pady=5)

    tipo_entry = ctk.CTkEntry(janela, placeholder_text="Tipo (admin, professor, aluno)")
    tipo_entry.pack(pady=5)

    def salvar():
        msg = cadastrarUsuarios(
            nome=nome_entry.get(),
            email=email_entry.get(),
            senha=senha_entry.get(),
            tipo=tipo_entry.get()
        )
        messagebox.showinfo("Resultado", msg)
        janela.destroy()
        callback_atualizar()

    ctk.CTkButton(janela, text="Cadastrar", command=salvar).pack(pady=10)


def form_editar_usuario(parent, usuario, callback_atualizar):
    
    # Formulário para editar usuário existente
    
    janela = ctk.CTkToplevel(parent)
    janela.title("Editar Usuário")
    janela.geometry("400x300")

    ctk.CTkLabel(janela, text="Editar Usuário", font=("Arial", 16, "bold")).pack(pady=10)

    
    nome_entry = ctk.CTkEntry(janela, placeholder_text="Nome")
    nome_entry.insert(0, usuario["nome"])
    nome_entry.pack(pady=5)

    email_entry = ctk.CTkEntry(janela, placeholder_text="E-mail")
    email_entry.insert(0, usuario["email"])
    email_entry.pack(pady=5)

    tipo_entry = ctk.CTkEntry(janela, placeholder_text="Tipo")
    tipo_entry.insert(0, usuario["tipo"])
    tipo_entry.pack(pady=5)

    def salvar():
        msg = editarUsuarios(
            id_usuario=usuario["id_usuario"],
            nome=nome_entry.get(),
            email=email_entry.get(),
            tipo=tipo_entry.get()
        )
        messagebox.showinfo("Resultado", msg)
        janela.destroy()
        callback_atualizar()

    ctk.CTkButton(janela, text="Salvar Alterações", command=salvar).pack(pady=10)


def form_excluir_usuario(id_usuario, callback_atualizar):
   
   # Excluir usuário com confirmação
   
    resposta = messagebox.askyesno("Confirmação", "Deseja realmente excluir este usuário?")
    if resposta:
        msg = excluirUsuarios(id_usuario)
        messagebox.showinfo("Resultado", msg)
        callback_atualizar()


# -----------------------------
# ===== FORMULÁRIOS DE TURMAS
# -----------------------------

def form_cadastrar_turma(parent, callback_atualizar):
    
    # Formulário para cadastrar nova turma
    
    janela = ctk.CTkToplevel(parent)
    janela.title("Cadastrar Turma")
    janela.geometry("400x250")

    ctk.CTkLabel(janela, text="Cadastrar Turma", font=("Arial", 16, "bold")).pack(pady=10)

    nome_entry = ctk.CTkEntry(janela, placeholder_text="Nome da Turma")
    nome_entry.pack(pady=5)

    def salvar():
        msg = cadastrarTurmas(nome_entry.get())
        messagebox.showinfo("Resultado", msg)
        janela.destroy()
        callback_atualizar()

    ctk.CTkButton(janela, text="Cadastrar", command=salvar).pack(pady=10)


def form_editar_turma(parent, turma, callback_atualizar):
    # Formulário para editar turma existente
    janela = ctk.CTkToplevel(parent)
    janela.title("Editar Turma")
    janela.geometry("500x400")

    ctk.CTkLabel(janela, text="Editar Turma", font=("Arial", 16, "bold")).pack(pady=10)

    nome_entry = ctk.CTkEntry(janela, placeholder_text="Nome da Turma")
    nome_entry.insert(0, turma["nome"])
    nome_entry.pack(pady=5)

    def salvar():
        msg = editarTurmas(
            id_turma=turma["id_turma"],
            dados={
                "nome": nome_entry.get(),
            }
        )
        messagebox.showinfo("Resultado", msg)
        janela.destroy()
        callback_atualizar()

    ctk.CTkButton(janela, text="Salvar Alterações", command=salvar).pack(pady=10)


def form_excluir_turma(id_turma,callback_atualizar):
    
    # Excluir turma com confirmação
    
    resposta = messagebox.askyesno("Confirmação", "Deseja realmente excluir esta turma?")
    if resposta:
        msg = excluirTurmas(id_turma)
        messagebox.showinfo("Resultado", msg)
        callback_atualizar()

# ------------------------------
# ======= FORMULÁRIOS DE AULAS
# ------------------------------

def form_cadastrar_aula(parent, callback_atualizar):
    """
    Formulário para cadastrar nova aula
    """
    janela = ctk.CTkToplevel(parent)
    janela.title("Nova Aula")
    janela.geometry("500x450")
    janela.configure(fg_color="white")
    janela.resizable(False, False)

    ctk.CTkLabel(janela, text="Criar Nova Aula", font=("Arial", 16, "bold")).pack(pady=10)

    titulo_entry = ctk.CTkEntry(janela, placeholder_text="Título da Aula", width=400)
    titulo_entry.pack(pady=10)

    descricao_entry = ctk.CTkEntry(janela, placeholder_text="Descrição da Aula", width=400)
    descricao_entry.pack(pady=10)

    data_entry = ctk.CTkEntry(janela, placeholder_text="Data (AAAA-MM-DD)", width=400)
    data_entry.pack(pady=10)

    def salvar():
        msg = cadastrarAulas(
            titulo_entry.get(),
            descricao_entry.get(),
            data_entry.get()
        )
        messagebox.showinfo("Sucesso", msg)
        janela.destroy()
        callback_atualizar()  # 🔁 Atualiza lista de aulas no dashboard

    ctk.CTkButton(janela, text="💾 Salvar Aula", fg_color=COLORS["accent"], command=salvar).pack(pady=30)


def form_editar_aula(parent, aula, callback_atualizar):
    """
    Formulário para editar aula existente
    """
    janela = ctk.CTkToplevel(parent)
    janela.title("Editar Aula")
    janela.geometry("500x450")
    janela.configure(fg_color="white")
    janela.resizable(False, False)

    ctk.CTkLabel(janela, text="Editar Aula", font=("Arial", 16, "bold")).pack(pady=10)

    titulo_entry = ctk.CTkEntry(janela, placeholder_text="Título", width=400)
    titulo_entry.insert(0, aula["titulo"])
    titulo_entry.pack(pady=10)

    descricao_entry = ctk.CTkEntry(janela, placeholder_text="Descrição", width=400)
    descricao_entry.insert(0, aula["descricao"])
    descricao_entry.pack(pady=10)

    data_entry = ctk.CTkEntry(janela, placeholder_text="Data (AAAA-MM-DD)", width=400)
    data_entry.insert(0, aula["data_aula"])
    data_entry.pack(pady=10)

    def salvar():
        novos_dados = {
            "titulo": titulo_entry.get(),
            "descricao": descricao_entry.get(),
            "data_aula": data_entry.get()
        }
        msg = editarAulas(aula["id_aula"], novos_dados)
        messagebox.showinfo("Sucesso", msg)
        janela.destroy()
        callback_atualizar()

    ctk.CTkButton(janela, text="✏️ Atualizar Aula", fg_color=COLORS["accent"], command=salvar).pack(pady=30)
# ---------------------
# ======== FORMULÁRIOS ATIVIDADES
# --------------------

def form_cadastrar_atividade(master, callback_atualizar):
    janela = ctk.CTkToplevel(master)
    janela.title("Nova Atividade")
    janela.geometry("500x480")
    janela.configure(fg_color=COLORS["card_bg"])
    janela.resizable(False, False)

    fonts = get_fonts()

    ctk.CTkLabel(
        janela,
        text="📘 Criar Nova Atividade",
        font=fonts["title"],
        text_color=COLORS["accent"]
    ).pack(pady=(25, 20))

    titulo = ctk.CTkEntry(janela, placeholder_text="Título da Atividade", width=400)
    titulo.pack(pady=10)

    descricao = ctk.CTkEntry(janela, placeholder_text="Descrição", width=400)
    descricao.pack(pady=10)

    data_entrega = ctk.CTkEntry(janela, placeholder_text="Data de Entrega (AAAA-MM-DD)", width=400)
    data_entrega.pack(pady=10)

    def salvar():
        if not titulo.get() or not descricao.get() or not data_entrega.get():
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos antes de salvar.")
            return

        try:
            msg = cadastrarAtividades(titulo.get(), descricao.get(), data_entrega.get())
            messagebox.showinfo("✅ Sucesso", msg)
            janela.destroy()
            callback_atualizar()  # Atualiza a lista de atividades no dashboard
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao salvar a atividade:\n{e}")

    ctk.CTkButton(
        janela,
        text="💾 Salvar Atividade",
        fg_color=COLORS["accent"],
        hover_color=COLORS["accent_hover"],
        text_color=COLORS["text_light"],
        font=fonts["button"],
        command=salvar,
        width=200,
        height=40,
        corner_radius=10
    ).pack(pady=30)


# === Formulário: Editar atividade existente ===
def form_editar_atividade(master, atividade, callback_atualizar):

    janela = ctk.CTkToplevel(master)
    janela.title("Editar Atividade")
    janela.geometry("500x480")
    janela.configure(fg_color=COLORS["card_bg"])
    janela.resizable(False, False)

    fonts = get_fonts()

    ctk.CTkLabel(
        janela,
        text="✏️ Editar Atividade",
        font=fonts["title"],
        text_color=COLORS["accent"]
    ).pack(pady=(25, 20))

    titulo = ctk.CTkEntry(janela, placeholder_text="Título", width=400)
    titulo.insert(0, atividade["titulo"])
    titulo.pack(pady=10)

    descricao = ctk.CTkEntry(janela, placeholder_text="Descrição", width=400)
    descricao.insert(0, atividade["descricao"])
    descricao.pack(pady=10)

    data_entrega = ctk.CTkEntry(janela, placeholder_text="Data de Entrega (AAAA-MM-DD)", width=400)
    data_entrega.insert(0, atividade["data_entrega"])
    data_entrega.pack(pady=10)

    def salvar():
        novos_dados = {
            "titulo": titulo.get(),
            "descricao": descricao.get(),
            "data_entrega": data_entrega.get()
        }

        try:
            msg = editarAtividades(atividade["id_atividade"], novos_dados)
            messagebox.showinfo("✅ Sucesso", msg)
            janela.destroy()
            callback_atualizar()  # Atualiza a lista no dashboard
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao atualizar a atividade:\n{e}")

    ctk.CTkButton(
        janela,
        text="💾 Salvar Alterações",
        fg_color=COLORS["accent_hover"],
        hover_color=COLORS["accent"],
        text_color=COLORS["text_light"],
        font=fonts["button"],
        command=salvar,
        width=200,
        height=40,
        corner_radius=10
    ).pack(pady=30)

def form_entregar_atividade(usuario, id_atividade):
    """Exibe o formulário para o aluno enviar a resposta de uma atividade."""

    # === Janela principal ===
    janela = ctk.CTkToplevel()
    janela.title("📤 Enviar Atividade")
    janela.geometry("500x400")
    janela.resizable(False, False)
    janela.configure(fg_color=COLORS["bg"])

    # === Fontes ===
    FONTS = get_fonts()
    title_font = FONTS["title"]
    text_font = FONTS["text"]
    button_font = FONTS["button"]

    # === Cabeçalho ===
    header = ctk.CTkFrame(janela, fg_color=COLORS["accent"], corner_radius=12)
    header.pack(fill="x", pady=(15, 10), padx=15)
    ctk.CTkLabel(
        header,
        text="📘 Enviar Resposta da Atividade",
        font=title_font,
        text_color="white"
    ).pack(pady=10)

    # === Corpo ===
    corpo = ctk.CTkFrame(janela, fg_color="white", corner_radius=12)
    corpo.pack(fill="both", expand=True, padx=15, pady=(5, 15))

    ctk.CTkLabel(
        corpo,
        text="💬 Sua Resposta:",
        font=text_font,
        text_color=COLORS["text_dark"],
        anchor="w"
    ).pack(anchor="w", pady=(15, 5), padx=15)

    # Campo de texto para resposta
    resposta_entry = ctk.CTkTextbox(
        corpo,
        height=180,
        font=("Arial", 13),
        fg_color="#F9FAFB",
        border_width=1,
        border_color="#D1D5DB",
        corner_radius=8
    )
    resposta_entry.pack(fill="both", expand=True, padx=15, pady=(0, 10))

    # === Função interna de envio ===
    def enviar():
        resposta = resposta_entry.get("1.0", "end").strip()
        if not resposta:
            messagebox.showwarning("Aviso", "Digite uma resposta antes de enviar.")
            return

        try:
            msg = registrarEntrega(
                id_atividade=id_atividade,
                id_usuario=usuario["id_usuario"],  # ✅ Correção principal
                status="Entregue",
                nota=None,
                dia_entrega=datetime.now().strftime("%Y-%m-%d"),
                observacao=resposta
            )
            messagebox.showinfo("✅ Sucesso", msg)
            janela.destroy()
        except Exception as e:
            messagebox.showerror("❌ Erro", f"Erro ao enviar atividade:\n{e}")

    # === Botão de envio ===
    ctk.CTkButton(
        corpo,
        text="📤 Enviar Atividade",
        font=button_font,
        fg_color=COLORS["accent"],
        hover_color=COLORS["accent_hover"],
        text_color="white",
        corner_radius=10,
        height=40,
        command=enviar
    ).pack(pady=(10, 20))

    janela.grab_set()  # bloqueia interação com janelas atrás