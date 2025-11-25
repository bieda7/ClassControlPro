import customtkinter as ctk
from tkinter import messagebox

from controller.usuarios_controller import cadastrarUsuarios, editarUsuarios, excluirUsuarios, listarTodosUsuarios
from controller.turmas_controller import cadastrarTurmas, editarTurmas, excluirTurmas
from controller.aulas_controller import cadastrarAulas, editarAulas, deletarAulasExistentes
from controller.atividades_controller import cadastrarAtividades, editarAtividades, excluirAtividades, enviarEntregaAluno
from controller.alunos_controller import cadastrarAlunos, editarAluno, excluirAlunos
from controller.turmas_controller import listarTodasTurmas
from model.alunos_model import buscarIdAlunoPorUsuario
from model.atividades_model import atualizarNotaEntrega

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
    janela.grab_set()         # força foco na nova janela (modal)
    janela.focus_force()      # garante foco no Windows
    janela.transient()    # associa a nova janela à janela principal
    janela.lift()             # traz para frente
    janela.attributes('-topmost', True)
    janela.after(10, lambda: janela.attributes('-topmost', False))

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
    janela.grab_set()         # força foco na nova janela (modal)
    janela.focus_force()      # garante foco no Windows
    janela.transient()    # associa a nova janela à janela principal
    janela.lift()             # traz para frente
    janela.attributes('-topmost', True)
    janela.after(10, lambda: janela.attributes('-topmost', False))

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
    janela.grab_set()         # força foco na nova janela (modal)
    janela.focus_force()      # garante foco no Windows
    janela.transient()    # associa a nova janela à janela principal
    janela.lift()             # traz para frente
    janela.attributes('-topmost', True)
    janela.after(10, lambda: janela.attributes('-topmost', False))

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
    janela.grab_set()         # força foco na nova janela (modal)
    janela.focus_force()      # garante foco no Windows
    janela.transient()    # associa a nova janela à janela principal
    janela.lift()             # traz para frente
    janela.attributes('-topmost', True)
    janela.after(10, lambda: janela.attributes('-topmost', False))

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
    janela.grab_set()         # força foco na nova janela (modal)
    janela.focus_force()      # garante foco no Windows
    janela.transient()    # associa a nova janela à janela principal
    janela.lift()             # traz para frente
    janela.attributes('-topmost', True)
    janela.after(10, lambda: janela.attributes('-topmost', False))
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
    janela.grab_set()         # força foco na nova janela (modal)
    janela.focus_force()      # garante foco no Windows
    janela.transient()    # associa a nova janela à janela principal
    janela.lift()             # traz para frente
    janela.attributes('-topmost', True)
    janela.after(10, lambda: janela.attributes('-topmost', False))
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
    janela.grab_set()         # força foco na nova janela (modal)
    janela.focus_force()      # garante foco no Windows
    janela.transient()    # associa a nova janela à janela principal
    janela.lift()             # traz para frente
    janela.attributes('-topmost', True)
    janela.after(10, lambda: janela.attributes('-topmost', False))
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

# ----------------------------------------------
# === Formulário: Editar atividade existente ===
# ----------------------------------------------
def form_editar_atividade(master, atividade, callback_atualizar):

    janela = ctk.CTkToplevel(master)
    janela.title("Editar Atividade")
    janela.geometry("500x480")
    janela.grab_set()         # força foco na nova janela (modal)
    janela.focus_force()      # garante foco no Windows
    janela.transient()    # associa a nova janela à janela principal
    janela.lift()             # traz para frente
    janela.attributes('-topmost', True)
    janela.after(10, lambda: janela.attributes('-topmost', False))
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

    janela = ctk.CTkToplevel()
    janela.title("📤 Enviar Atividade")
    janela.geometry("500x430")
    janela.grab_set()
    janela.focus_force()
    janela.transient()
    janela.lift()
    janela.attributes('-topmost', True)
    janela.after(10, lambda: janela.attributes('-topmost', False))
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

    # Campo de texto
    resposta_entry = ctk.CTkTextbox(
        corpo,
        height=150,
        font=("Arial", 13),
        fg_color="#F9FAFB",
        border_width=1,
        border_color="#D1D5DB",
        corner_radius=8
    )
    resposta_entry.pack(fill="both", expand=True, padx=15, pady=(0, 10))

    # Arquivo opcional (para implementar depois)
    arquivo_url = None

    # === Função interna de envio ===
    def enviar():
        resposta = resposta_entry.get("1.0", "end").strip()

        if not resposta:
            messagebox.showwarning("Aviso", "Digite uma resposta antes de enviar.")
            return

        try:
            # Buscar id_aluno vinculado ao usuário
            id_aluno = buscarIdAlunoPorUsuario(usuario["id_usuario"])

            if not id_aluno:
                messagebox.showerror("❌ Erro", "Não foi possível localizar o aluno vinculado a este usuário.")
                return

            # === CHAMADA CORRETA DO MODEL ===
            sucesso = enviarEntregaAluno(
                id_atividade=id_atividade,
                id_aluno=id_aluno,
                resposta=resposta,
                arquivo_url=arquivo_url
            )

            if sucesso:
                messagebox.showinfo("✅ Sucesso", "Atividade enviada com sucesso!")
                janela.destroy()
            else:
                messagebox.showerror("❌ Erro", "Erro ao registrar a entrega. Tente novamente.")

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

    janela.grab_set()


# --------------------------
# === Formulários Alunos ===
# --------------------------
def form_cadastrar_aluno(parent, callback_atualizar):
    """
    Formulário para cadastrar novo aluno
    """
    janela = ctk.CTkToplevel(parent)
    janela.title("Cadastrar Aluno")
    janela.geometry("400x300")
    janela.grab_set()         # força foco na nova janela (modal)
    janela.focus_force()      # garante foco no Windows
    janela.transient()    # associa a nova janela à janela principal
    janela.lift()             # traz para frente
    janela.attributes('-topmost', True)
    janela.after(10, lambda: janela.attributes('-topmost', False))

    ctk.CTkLabel(janela, text="Cadastrar Aluno", font=("Arial", 16, "bold")).pack(pady=10)

    nome_entry = ctk.CTkEntry(janela, placeholder_text="Nome")
    nome_entry.pack(pady=5)

    matricula_entry = ctk.CTkEntry(janela, placeholder_text="Matrícula")
    matricula_entry.pack(pady=5)

    email_entry = ctk.CTkEntry(janela, placeholder_text="Email")
    email_entry.pack(pady=5)

    idturma_entry = ctk.CTkEntry(janela, placeholder_text="Id Turma")
    idturma_entry.pack(pady=5)

    def salvar():
        msg = cadastrarAlunos(
            nome=nome_entry.get(),
            matricula=matricula_entry.get(),
            email=email_entry.get(),
            id_turma=idturma_entry.get()
        )
        messagebox.showinfo("Resultado", msg)
        janela.destroy()
        callback_atualizar()

    ctk.CTkButton(janela, text="Cadastrar", command=salvar).pack(pady=10)

def form_editar_aluno(parent, aluno, callback_atualizar):
    # Formulário para editar usuário existente
    
    janela = ctk.CTkToplevel(parent)
    janela.title("Editar Aluno")
    janela.geometry("400x460")
    janela.grab_set()         # força foco na nova janela (modal)
    janela.focus_force()      # garante foco no Windows
    janela.transient()    # associa a nova janela à janela principal
    janela.lift()             # traz para frente
    janela.attributes('-topmost', True)
    janela.after(10, lambda: janela.attributes('-topmost', False))
    janela.resizable(False, False)

    # -------------------------------
    # CARREGA TURMAS DO BANCO
    # -------------------------------
    turmas = listarTodasTurmas()  # [{"id_turma": 1, "nome": "Turma A"}, ...]

    nomes_turmas = [t["nome"] for t in turmas]
    ids_turmas = [t["id_turma"] for t in turmas]

    # Turma atual
    try:
        index_atual = ids_turmas.index(aluno["id_turma"])
    except:
        index_atual = 0

    # -------------------------------
    # CAMPOS
    # -------------------------------
    ctk.CTkLabel(janela, text="Editar Aluno", font=("Arial", 18, "bold")).pack(pady=12)

    # Nome
    ctk.CTkLabel(janela, text="Nome:").pack(anchor="w", padx=25)
    nome_entry = ctk.CTkEntry(janela, width=330)
    nome_entry.insert(0, aluno["nome"])
    nome_entry.pack(pady=5)

    # Email
    ctk.CTkLabel(janela, text="Email:").pack(anchor="w", padx=25)
    email_entry = ctk.CTkEntry(janela, width=330)
    email_entry.insert(0, aluno["email"])
    email_entry.pack(pady=5)

    # Matrícula
    ctk.CTkLabel(janela, text="Matrícula:").pack(anchor="w", padx=25)
    matricula_entry = ctk.CTkEntry(janela, width=330)
    matricula_entry.insert(0, aluno["matricula"])
    matricula_entry.pack(pady=5)

    # Turma
    ctk.CTkLabel(janela, text="Turma:").pack(anchor="w", padx=25)
    turma_combo = ctk.CTkComboBox(janela, values=nomes_turmas, width=330)
    turma_combo.set(nomes_turmas[index_atual])
    turma_combo.pack(pady=5)

    # -------------------------------
    # SALVAR
    # -------------------------------
    def salvar():
        novos_dados = {
            "nome": nome_entry.get(),
            "email": email_entry.get(),
            "matricula": matricula_entry.get(),
            "id_turma": ids_turmas[nomes_turmas.index(turma_combo.get())]
        }

        # Chama sua função atualizada
        msg = editarAluno(aluno["id_aluno"], novos_dados)

        messagebox.showinfo("Alterações", msg)
        janela.destroy()
        callback_atualizar()

    # -------------------------------
    # BOTÕES
    # -------------------------------
    ctk.CTkButton(janela, text="Salvar Alterações", command=salvar).pack(pady=20)
    ctk.CTkButton(janela, text="Cancelar", fg_color="gray", command=janela.destroy).pack(pady=5)

def form_atribuir_nota(entrega, callback=None):
    from model.atividades_model import atualizarNotaEntrega  # usa id_atividade + id_aluno

    janela = ctk.CTkToplevel()
    janela.title("📝 Atribuir Nota")
    janela.geometry("450x650")
    janela.grab_set()
    janela.focus_force()
    janela.transient()
    janela.lift()
    janela.resizable(False, False)
    janela.configure(fg_color=COLORS["bg"])

    FONTS = get_fonts()

    # Header
    header = ctk.CTkFrame(janela, fg_color=COLORS["accent"], corner_radius=12)
    header.pack(fill="x", pady=(15, 10), padx=15)

    ctk.CTkLabel(
        header,
        text="📝 Atribuir Nota",
        font=FONTS["title"],
        text_color="white"
    ).pack(pady=10)

    # Body
    body = ctk.CTkFrame(janela, fg_color="white", corner_radius=12)
    body.pack(fill="both", expand=True, padx=15, pady=(5, 15))

    ctk.CTkLabel(
        body,
        text=f"📄 Atividade: {entrega['atividade']}",
        font=("Arial", 14, "bold"),
        anchor="w"
    ).pack(anchor="w", padx=15, pady=(15, 3))

    ctk.CTkLabel(
        body,
        text=f"👤 Aluno: {entrega['aluno']}",
        font=("Arial", 13),
        anchor="w"
    ).pack(anchor="w", padx=15)

    # Resposta do aluno
    ctk.CTkLabel(
        body,
        text="💬 Resposta do aluno:",
        font=("Arial", 13, "bold"),
    ).pack(anchor="w", padx=15, pady=(15, 3))

    resposta_box = ctk.CTkTextbox(body, height=120, fg_color="#F9FAFB")
    resposta_box.insert("1.0", entrega["resposta"])
    resposta_box.configure(state="disabled")
    resposta_box.pack(fill="x", padx=15)

    # Campo de Observação do professor
    ctk.CTkLabel(
        body,
        text="🗒 Observação do professor (opcional):",
        font=("Arial", 13, "bold")
    ).pack(anchor="w", padx=15, pady=(15, 3))

    entrada_obs = ctk.CTkTextbox(body, height=80, fg_color="#F9FAFB")
    entrada_obs.insert("1.0", entrega.get("observacao") or "")
    entrada_obs.pack(fill="x", padx=15)

    # Campo de Nota
    ctk.CTkLabel(
        body,
        text="📝 Nota:",
        font=("Arial", 13, "bold")
    ).pack(anchor="w", padx=15, pady=(15, 3))

    entrada_nota = ctk.CTkEntry(body, placeholder_text="Ex: 8.5")
    nota_atual = entrega.get("nota")
    if nota_atual is not None:
        entrada_nota.insert(0, str(nota_atual))
    entrada_nota.pack(fill="x", padx=15)

    # Botão salvar
    def salvar():
        try:
            nota = float(entrada_nota.get())
            observacao = entrada_obs.get("1.0", "end").strip()

            atualizarNotaEntrega(
                entrega["id_atividade"],
                entrega["id_aluno"],
                nota,
                observacao
            )

            messagebox.showinfo("Sucesso", "Nota salva com sucesso!")

            if callback:
                callback()

            janela.destroy()

        except Exception as e:
            messagebox.showerror("Erro", f"Insira uma nota válida.\n\n{e}")

    ctk.CTkButton(
        body,
        text="💾 Salvar Nota",
        fg_color=COLORS["accent"],
        hover_color=COLORS["accent_hover"],
        command=salvar
    ).pack(pady=20)



