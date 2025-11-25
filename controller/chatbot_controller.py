# chatbot_controller.py

# ----------------------------
# TIPO DO USUÁRIO LOGADO
# ----------------------------
usuario_tipo_atual = None

def set_usuario_tipo(tipo):
    """Define o tipo do usuário logado (admin, professor, aluno)."""
    global usuario_tipo_atual
    usuario_tipo_atual = tipo

def get_usuario_tipo():
    """Retorna o tipo do usuário logado."""
    return usuario_tipo_atual


# ----------------------------
# HISTÓRICO DO CHAT
# ----------------------------
historico_chat = []   # futura persistência em JSON

def adicionar_ao_historico(tipo, mensagem):
    if mensagem:
        historico_chat.append({
            "tipo": tipo,
            "mensagem": mensagem
        })

def obter_historico():
    return historico_chat


# ----------------------------
# PERGUNTAS POR TIPO DE USUÁRIO
# ----------------------------

PERGUNTAS_ADMIN = [
    "📋 Como cadastrar um aluno?",
    "🧑‍🏫 Como cadastrar um professor?",
    "🏫 Como cadastrar uma turma?",
    "🔐 Permissões de cada tipo de usuário",
    "📔 Como emitir relatórios?"
]

PERGUNTAS_PROFESSOR = [
    "📚 Como criar uma aula para meus alunos?",
    "📝 Como criar uma atividade?",
    "📤 Como ver as entregas dos alunos?",
    "📔 Como emitir relatórios?"
]

PERGUNTAS_ALUNO = [
    "📚 Como ver o conteúdo das aulas?",
    "📝 Como acessar minhas atividades?",
    "📤 Como entregar uma atividade?",
    "📔 Como emitir relatórios?"
]


# ----------------------------
# RESPOSTAS POR TIPO DE USUÁRIO
# ----------------------------

RESPOSTAS_ADMIN = {
    "📋 Como cadastrar um aluno?":
        "Admins podem cadastrar alunos em:\n**Menu > Usuários > Cadastrar novo usuario**. \n Ao definir o tipo de usuario como *aluno*, um aluno é criado automaticamente na tabela alunos. Recebendo uma matricula automatica e precisando que apenas que seja vinculado a uma turma através do gerenciamento de alunos",

    "🧑‍🏫 Como cadastrar um professor?":
        "Admins podem criar professores em:\n**Menu > Usuários > Cadastrar novo usuario**. \n Ao definir um usuário como *professor*, um professor é criado automaticamente",

    "🏫 Como cadastrar uma turma?":
        "Admins podem criar turmas em:\n**Menu > Turmas > Cadastrar nova turma**.",

    "🔐 Permissões de cada tipo de usuário":
        "📌 *Admin:* cria usuários, turmas e gerencia tudo.\n"
        "📌 *Professor:* cria aulas, atividades e corrige entregas.\n"
        "📌 *Aluno:* acessa aulas, atividades e envia entregas.",

    "📔 Como emitir relatórios?":
        "Entre em Menu > Relatórios > Gerar Relatório Geral (Admin)"
    
}

RESPOSTAS_PROFESSOR = {
    "📚 Como criar uma aula para meus alunos?":
        "Professores podem criar aulas em:\n**Menu > Aulas > Criar Nova Aula**.",

    "📝 Como criar uma atividade?":
        "Professores criam atividades em:\n**Menu > Atividades > Criar Nova Atividade**.",

    "📤 Como ver as entregas dos alunos?":
        "Acesse:\n**Menu > Entregas** para visualizar respostas dos alunos.",

    "📔 Como emitir relatórios?":
        "Entre em Menu > Relatórios > Gerar Relatório do Professor"
}

RESPOSTAS_ALUNO = {
    "📚 Como ver o conteúdo das aulas?":
        "Acesse:\n**Menu > Minhas Aulas** para ver conteúdos disponíveis.",

    "📝 Como acessar minhas atividades?":
        "Entre em:\n**Menu > Minhas Atividades**.",

    "📤 Como entregar uma atividade?":
        "Entre em:\n**Menu > Minhas Atividades**. Lá você poderá selecionar uma atividade em clicar em *Enviar Atividade*",
        
    "📔 Como emitir relatórios?":
        "Entre em Menu > Relatórios > Gerar Meu Relatório (Atividades)"

}


# ----------------------------
# FUNÇÃO PARA RETORNAR PERGUNTAS
# ----------------------------

def obter_perguntas(tipo_usuario=None):

    if tipo_usuario is None:
        tipo_usuario = usuario_tipo_atual

    if tipo_usuario == "admin":
        return PERGUNTAS_ADMIN

    elif tipo_usuario == "professor":
        return PERGUNTAS_PROFESSOR

    elif tipo_usuario == "aluno":
        return PERGUNTAS_ALUNO

    return ["Erro: tipo de usuário inválido."]


# ----------------------------
# FUNÇÃO PARA RETORNAR RESPOSTAS
# ----------------------------

def obter_resposta(pergunta, tipo_usuario=None):

    if tipo_usuario is None:
        tipo_usuario = usuario_tipo_atual

    if tipo_usuario == "admin":
        return RESPOSTAS_ADMIN.get(pergunta, "❌ Pergunta não encontrada para admins.")

    if tipo_usuario == "professor":
        return RESPOSTAS_PROFESSOR.get(pergunta, "❌ Pergunta não encontrada para professores.")

    if tipo_usuario == "aluno":
        return RESPOSTAS_ALUNO.get(pergunta, "❌ Pergunta não encontrada para alunos.")

    return "❌ Tipo de usuário inválido."
