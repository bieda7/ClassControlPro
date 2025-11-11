import customtkinter as ctk
from tkinter import messagebox

from controller.usuarios_controller import cadastrarUsuarios, editarUsuarios, excluirUsuarios, listarTodosUsuarios
from controller.turmas_controller import cadastrarTurmas, editarTurmas, excluirTurmas

import customtkinter as ctk
from tkinter import messagebox


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
