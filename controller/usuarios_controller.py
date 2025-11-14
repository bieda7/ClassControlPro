from model.usuarios_model import inserirUsuarios, listarUsuarios, buscarUsuarioPorEmail, deletarUsuarios, atualizarUsuarios
from utils.permissoes import acessos
import hashlib  # Módulo para criptografar senha

# === Cadastro de Usuários ===
def cadastrarUsuarios(nome, email, senha, tipo):
    usuario_existente = buscarUsuarioPorEmail(email)
    if usuario_existente:
        return "❌ Já existe um usuário com este email, cadastre um novo endereço de email!"

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    inserirUsuarios(nome, email, senha_hash, tipo)
    return "✅ Usuário cadastrado com sucesso!"

# === Login ===
def login(email, senha):
    usuario = buscarUsuarioPorEmail(email)
    if not usuario:
        return None, "❌ Usuário não encontrado!"

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    if usuario["senha"] == senha_hash:
        return usuario, "✅ Login bem-sucedido! {usuario['nome']}!"
    else:
        return None, "❌ Senha incorreta."

# === Listar Todos os Usuários ===
def listarTodosUsuarios():
    usuarios = listarUsuarios()
    return usuarios  # retorna lista de usuários, mesmo que vazia

# === Editar Usuários ===
def editarUsuarios(id_usuario, nome=None, email=None, tipo=None):
    novos_dados = {}
    if nome: novos_dados["nome"] = nome
    if email: novos_dados["email"] = email
    if tipo: novos_dados["tipo"] = tipo

    sucesso = atualizarUsuarios(id_usuario, novos_dados)
    if sucesso:
        return f"✅ Usuário {id_usuario} atualizado com sucesso!"
    else:
        return "❌ Erro ao atualizar o usuário."

# === Excluir Usuários ===
def excluirUsuarios(id_usuario):
    deletarUsuarios(id_usuario)
    return f"🗑️ Usuário {id_usuario} deletado com sucesso!"

def contarUsuarios():
    usuarios = listarTodosUsuarios()  # <-- adiciona os parênteses
    return len(usuarios)
