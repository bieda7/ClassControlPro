def acessos(tipo_usuario, modulo, acao):
    regras = {
        'admin': {
            'alunos': ['read', 'create', 'update', 'grade'],
            'turmas': ['read', 'create', 'update', 'grade'],
            'aulas': ['read', 'create', 'update', 'grade'],
            'atividades': ['create', 'read', 'update', 'grade'],
            'usuarios': ['read', 'create', 'update', 'grade'],
        },
        'professor': {
            'alunos': ['read'],
            'turmas': ['read'],
            'aulas': ['create', 'read'],
            'atividades': ['create', 'read', 'update', 'grade'],
        },
        'aluno': {
            'alunos': ['read'],
            'turmas': ['read'],
            'aulas': ['read'],
            'atividades': ['read', 'submit'],
        }
    }

    return acao in regras.get(tipo_usuario, {}).get(modulo, [])

