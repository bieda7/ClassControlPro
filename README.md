# 🎓 ClassControlPro — Sistema Acadêmico Inteligente

---

Bem-vindo(a) ao **ClassControlPro**, um sistema acadêmico modular desenvolvido com a arquitetura **MVC (Model-View-Controller)** para simplificar e modernizar o gerenciamento de **usuários, alunos, turmas, aulas e atividades escolares**.  
O projeto tem foco em **organização, escalabilidade e segurança**, sendo ideal para uso acadêmico e profissional. 💡  

---

## 🧩 Funcionalidades Principais

✅ **Gestão de Usuários** — controle de perfis (Admin, Professor, Aluno) com permissões específicas.  
📚 **Cadastro de Turmas e Aulas** — organização das classes e conteúdos lecionados.  
🧠 **Controle de Atividades** — criação, edição e acompanhamento de tarefas e avaliações.  
🧾 **Relatórios e Listagens** — exibição estruturada de dados diretamente do banco MySQL.  
🔐 **Controle de Acesso** — módulo de permissões e autenticação segura.  

---

## 🏗️ Arquitetura do Projeto (MVC)

O **ClassControlPro** segue o padrão **MVC**, garantindo separação clara entre regras de negócio, interface e controle.

- **Model (`model/`)** → Conexão com o banco e manipulação de dados.  
- **Controller (`controller/`)** → Regras de negócio e lógica do sistema.  
- **View (`view/`)** → Camada de interface e exibição de dados.  
- **Utils (`utils/`)** → Módulos auxiliares, como controle de permissões.  
- **Uploads (`uploads/`)** → Armazena arquivos e materiais enviados (ex: PDFs de aulas).  

---

## 💾 Estrutura Atual do Projeto

📂 CLASSCONTROLPRO/
├── controller/
│ ├── alunos_controller.py
│ ├── atividades_controller.py
│ ├── aulas_controller.py
│ ├── turmas_controller.py
│ └── usuarios_controller.py
│
├── model/
│ ├── alunos_model.py
│ ├── atividades_model.py
│ ├── aulas_model.py
│ ├── turmas_model.py
│ ├── usuarios_model.py
│ └── conexao.py # ⚠️ Contém dados sensíveis (não versionar)
│
├── uploads/
│ └── aulas/ # Materiais ou arquivos de aula
│
├── utils/
│ ├── permissoes.py # Sistema de permissões e autenticação
│ └── init.py
│
├── view/
│ └── login_view.py # Interface de login
│
├── venv/ # Ambiente virtual (não versionar)
├── .gitignore
├── README.md
└── main.py # Arquivo principal do sistema

---

## 💻 Tecnologias utilizadas

### Linguagens:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![MySQL](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

 ### Versionamento e Hospedagem:

![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SEUUSERNAME)


### Banco de Dados:

![MySQL Workbench](https://img.shields.io/badge/mysql--workbench-00758F?style=for-the-badge&logo=mysql&logoColor=white)


### Status:
![Em andamento](https://img.shields.io/badge/status-Em%20andamento-F2A900?style=for-the-badge&logoColor=white)

