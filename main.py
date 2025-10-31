import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# Models
from model.conexao import conectar
from utils.permissoes import acessos
from model.alunos_model import inserirAlunos, listarAlunos, listarAlunosPorTurma, deletarAlunos, atualizarAlunos
from model.atividades_model import inserirAtividades, atualizarAtividades, listarAtividadePorAula, deletarAtividades
from model.aulas_model import inserirAulas, listarAulasPorTurma , deletarAulas, atualizarAulas, salvarArquivoAulas
from model.turmas_model import inserirTurmas, listarProfessoresDaTurma, listarTurmas, deletarTurmas, associarProfessor, atualizarTurmas
from model.usuarios_model import inserirUsuarios, listarUsuarios, deletarUsuarios, atualizarUsuarios, buscarUsuarioPorEmail

# Controllers
from controller.alunos_controller import cadastrarAlunos, listarTodosAlunos, atualizarAlunoExistente, excluirAlunos
from controller.atividades_controller import cadastrarAtividades, listarAtividadesDaAula, atualizarAtividadeExistente, excluirAtividades
from controller.aulas_controller import cadastrarAulas, listarTodasAulas, atualizarAulasExistentes, deletarAulasExistentes
from controller.turmas_controller import cadastrarTurmas, listarTodasTurmas, atualizarTurmaExistente, exibirProfessoresDaTurma, excluirTurmas
from controller.usuarios_controller import cadastrarUsuarios, login, listarTodosUsuarios, excluirUsuarios



if __name__ == "__main__":

    # --------------------------
    # 1️⃣ CADASTRO DE USUÁRIOS
    # --------------------------
    # usuario_admin = cadastrarUsuarios('admin', "Admin", "admin@email.com", "1234", "admin")
    # usuario_professor = cadastrarUsuarios('admin', "Prof1", "prof1@email.com", "abcd", "professor")
    # usuario_aluno = cadastrarUsuarios('admin', "Aluno1", "aluno1@email.com", "pass", "aluno")

    # --------------------------
    # 2️⃣ CADASTRO DE TURMAS
    # --------------------------
    # turma1 = cadastrarTurmas('aluno', "DS2R33")
    # turma2 = cadastrarTurmas('admin',"DS1Q33")

    # --------------------------
    # 3️⃣ CADASTRO DE ALUNOS
    # --------------------------
    aluno1 = cadastrarAlunos("Guilherme SN", "guilherme@email.com", "T25525Y", 3)
    aluno2 = cadastrarAlunos("Maria Silva", "maria@email.com", "R8907T", 3)

    # # --------------------------
    # # 4️⃣ CADASTRO DE AULAS
    # # --------------------------
    # aula1 = cadastrarAulas("Matemática - Álgebra", "Introdução à Álgebra", turma1)
    # aula2 = cadastrarAulas("Ciências - Biologia", "Células e DNA", turma1)

    # # --------------------------
    # # 5️⃣ CADASTRO DE ATIVIDADES
    # # --------------------------
    # atividade1 = cadastrarAtividades("Exercícios Álgebra", "Resolva as equações", aula1, "2025-11-05")
    # atividade2 = cadastrarAtividades("Estudo de Células", "Resumo sobre mitocôndrias", aula2, "2025-11-10")

    # # --------------------------
    # # 6️⃣ LISTAGEM DE DADOS
    # # --------------------------
    # print("\n--- Lista de Usuários ---")
    # listarTodosUsuarios()

    # print("\n--- Lista de Turmas ---")
    # listarTodasTurmas()

    # print("\n--- Lista de Alunos ---")
    # listarTodosAlunos()

    # print("\n--- Lista de Aulas ---")
    # listarTodasAulas()

    # print("\n--- Lista de Atividades da Aula 1 ---")
    # listarAtividadesDaAula(aula1)

    # # --------------------------
    # # 7️⃣ ATUALIZAÇÕES DE TESTE
    # # --------------------------
    # atualizarAlunoExistente(aluno1, {"nome": "Guilherme SN Atualizado", "idade": 22}, usuario_professor)
    # atualizarAtividadeExistente(atividade1, {"titulo": "Exercícios Álgebra Atualizado", "prazo": "2025-11-12"}, usuario_professor)
    # atualizarAulasExistentes(aula1, {"titulo": "Matemática - Álgebra Avançada"}, usuario_professor)
    # atualizarTurmaExistente(turma1, {"nome": "Turma A - Atualizada"}, usuario_admin)

    # # --------------------------
    # # 8️⃣ EXCLUSÕES DE TESTE
    # # --------------------------
    # # Você pode comentar essas linhas se quiser manter os dados para verificação
    # excluirAlunos(aluno2, usuario_professor)
    # excluirAtividades(atividade2, usuario_professor)
    # deletarAulasExistentes(aula2, usuario_professor)
    # excluirTurmas(turma2, usuario_admin)
    # excluirUsuarios(usuario_aluno)