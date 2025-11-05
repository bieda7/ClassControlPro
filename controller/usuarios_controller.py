from model.usuarios_model import inserirUsuarios, listarUsuarios, buscarUsuarioPorEmail, deletarUsuarios
from utils.permissoes import acessos
import hashlib #Modulo para criptografar senha

# Função de cadastro de usuários
def cadastrarUsuarios(tipo_usuario, nome, email, senha, tipo):
    if acessos(tipo_usuario, 'usuarios','create'):
        # Verifica se o usuario já existe no sistema
        usuario_existente = buscarUsuarioPorEmail(email)
        if usuario_existente:
            print("❌ Já existe um usuário com este email, cadastre um novo endereço de email!")
            return False
        # Criptografia da senha registrada pelo usuário
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
            
        inserirUsuarios(nome, email, senha_hash, tipo)
        print("✅ Usuário cadastrado com sucesso!")
        return True
    else:
        print(f"Seu perfil de usuário não permite a realização de novos cadastros!")
        return False

def login(email, senha):
    usuario = buscarUsuarioPorEmail(email)
    if not usuario:
        print("❌ Usuario não encontrado!")
    
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    if usuario["senha"] == senha_hash: #Verifica se a senha informada é a mesma senha armazenada no DB 
        print(f"✅ Login bem-sucedido! Bem-vindo, {usuario["nome"]} ({usuario["tipo"]})")
        return usuario
    else: 
        print("❌ Senha incorreta.")
        return None
    
def listarTodosUsuarios():
    usuarios = listarUsuarios()
    if usuarios:
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(f"ID: {usuario['id_usuario']} | Nome: {usuario['nome']} | Tipo: {usuario['tipo']}")
    else:
        print("⚠️ Nenhum usuário encontrado!")
            
def excluirUsuarios(id_usuario, usuario):
    if acessos(usuario, "usuario", "delete"):
        deletarUsuarios(id_usuario)
        return f"🗑️ Usuario {id_usuario} deletado com sucesso!"
    else:
        return "❌ Acesso não permitido: Apenas administradores podem deletar usuários!"
