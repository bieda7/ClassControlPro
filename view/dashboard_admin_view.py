import customtkinter as ctk
from tkinter import messagebox
from view.ui_config import COLORS, get_fonts
from PIL import Image
# --- IMPORT DO CHATBOT ---
from view.chatbot_view import ChatBotFrame
from controller.chatbot_controller import set_usuario_tipo



class DashboardAdmin(ctk.CTkToplevel):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario  # usuário logado
        self.title("ClassControlPro - Painel do Administrador")
        self.geometry("1100x650")
        self.configure(fg_color=COLORS["bg"])
        self.resizable(True, True)

        # Fontes
        FONTS = get_fonts()
        self.title_font = FONTS["title"]
        self.section_font = FONTS["section"]
        self.text_font = FONTS["text"]
        self.button_font = FONTS["button"]

        # Layout principal
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ===== MENU LATERAL =====
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color=COLORS["sidebar_bg"])
        self.sidebar.grid(row=0, column=0, sticky="nswe")
        self.sidebar.grid_rowconfigure(8, weight=1)

        # Logotipo
        logo_img = ctk.CTkImage(
            light_image=Image.open("view/components/logotipo-classcontrolpro.png"),
            size=(150, 150)
        )

        self.logo_label = ctk.CTkLabel(self.sidebar, image=logo_img, text="")
        self.logo_label.grid(row=0, column=0, pady=(20, 0), padx=20)

        self.create_sidebar_button("🏠  Início", self.show_home, 1, True)
        self.create_sidebar_button("👥  Usuários", self.show_usuarios, 2)
        self.create_sidebar_button("🏫  Turmas/Alunos", self.show_turmas_alunos, 3)
        self.create_sidebar_button("📊  Relatórios", self.show_relatorios, 4)
        self.create_sidebar_button("🤖  Chatbot", self.show_chatbot, 5)


        # Botão sair
        self.btn_sair = ctk.CTkButton(
            self.sidebar, text="🚪  Sair", width=180, height=40,
            fg_color=COLORS["danger"], hover_color=COLORS["danger_hover"],
            text_color="white", corner_radius=8, command=self.quit
        )
        self.btn_sair.grid(row=9, column=0, padx=20, pady=(50, 20))

        # Main frame
        self.main_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=15)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Inicializa com home
        self.show_home()

    # ====== MÉTODOS ======

    # Criação dos botões do meun lateral
    def create_sidebar_button(self, text, command, row, active=False):
        color = COLORS["accent"] if active else COLORS["sidebar_bg"]
        text_color = "white" if active else COLORS["text_dark"]
        hover = COLORS["accent_hover"] if active else "#E5E7EB"  # tom mais vibrante no hover

        btn = ctk.CTkButton(
            self.sidebar,
            text=text,
            width=180,
            height=40,
            fg_color=color,
            hover_color=hover,
            text_color=text_color,
            corner_radius=8,
            font=self.button_font,
            command=command
        )
        btn.grid(row=row, column=0, padx=20, pady=10)

    # === UTILITÁRIOS ===
    # Função para limpar a tela sempre ao carregar conteúdos novos
    # Essa função é chamada dentr de muitas outras, para deixar um visual limpo sempre que necessário
    def clear_main(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # Criação dos cards exibidos na tela home
    def create_dashboard_card(self, row, column, titulo, valor, descricao):
        card = ctk.CTkFrame(
            self.main_frame,
            fg_color="#FFFFFF",
            corner_radius=15
        )
        card.grid(row=row, column=column, padx=20, pady=10, sticky="nsew")

        # Configura tamanho
        self.main_frame.grid_columnconfigure(column, weight=1)

        # Título do card
        label_titulo = ctk.CTkLabel(
            card,
            text=titulo,
            font=("Segoe UI", 20, "bold"),
            text_color="#34495e"
        )
        label_titulo.pack(pady=(15, 5))

        # Valor grande
        label_valor = ctk.CTkLabel(
            card,
            text=valor,
            font=("Segoe UI", 40, "bold"),
            text_color="#2980b9"
        )
        label_valor.pack(pady=5)

        # Descrição pequena
        label_desc = ctk.CTkLabel(
            card,
            text=descricao,
            font=("Segoe UI", 14),
            text_color="#7f8c8d"
        )
        label_desc.pack(pady=(0, 15))


    # === TELAS ===

    # ===== Tela Inicial =====
    def show_home(self, *args):
        from controller.relatorios_controller import obter_totais_dashboard

        self.clear_main()

        # === CARREGA DADOS REAIS DO BANCO ===
        totais = obter_totais_dashboard()

        total_usuarios = totais["usuarios"]
        total_turmas = totais["turmas"]
        # ----------------------------
        # 1. TEXTO DE BOAS-VINDAS
        # ----------------------------
        titulo = ctk.CTkLabel(
            self.main_frame,
            text=f"✨ Bem-vindo(a), {self.usuario['nome']}! ✨\n",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color=COLORS["accent"],
            justify="center"
        )
        titulo.grid(row=0, column=0, columnspan=3, pady=(10, 5), sticky="n")

        subtitulo = ctk.CTkLabel(
            self.main_frame,
            text=(
                "Este é o seu painel administrativo!\n\n"
                "Gerencie usuários, turmas, atividades e muito mais\n"
                "de forma rápida, intuitiva e centralizada."
            ),
            font=ctk.CTkFont(size=16),
            text_color="#030303",
            justify="center"
        )
        subtitulo.grid(row=1, column=0, columnspan=3, pady=(0, 25), sticky="n")

        # ----------------------------------------------------
        # 2. CARDS – DADOS REAIS E TOTALMENTE CENTRALIZADOS
        # ----------------------------------------------------

        card_fg = "#ffffff"
        card_corner = 18

        def criar_card(col, titulo, valor, cor):
            card = ctk.CTkFrame(self.main_frame, fg_color=card_fg, corner_radius=card_corner)
            card.grid(row=2, column=col, padx=25, pady=10, sticky="nsew")

            ctitulo = ctk.CTkLabel(card, text=titulo, text_color="#444444",font=ctk.CTkFont(size=18, weight="bold"))
            ctitulo.pack(pady=(15, 5))

            cvalor = ctk.CTkLabel(
                card,
                text=str(valor),
                font=ctk.CTkFont(size=32, weight="bold"),
                text_color=cor
            )
            cvalor.pack(pady=(0, 15))

        # Cards
        criar_card(0, "Usuários Cadastrados", total_usuarios, COLORS["accent"])
        criar_card(2, "Turmas Ativas", total_turmas, COLORS["accent"])

        # ----------------------------------------------------
        # GRID RESPONSIVO
        # ----------------------------------------------------
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)


    # ===== Usuários =======
    def show_usuarios(self):
        self.clear_main()
        from controller.usuarios_controller import listarTodosUsuarios
        from view.forms import form_cadastrar_usuario, form_editar_usuario

        ctk.CTkLabel(
            self.main_frame,
            text=" 👥 Gerenciamento de Usuários",
            font=self.title_font,
            text_color=COLORS["text_dark"]
        ).pack(pady=20)

        # Botão novo usuário
        btn_novo_usuario = ctk.CTkButton(
            self.main_frame,
            text="➕ Cadastrar novo usuário",
            width=200,
            height=32,
            command=lambda: form_cadastrar_usuario(self, self.show_usuarios)
        )
        btn_novo_usuario.pack(pady=10)

        # Lista usuários
        frame_lista = ctk.CTkScrollableFrame(self.main_frame, width=700, height=400)
        frame_lista.pack(pady=10, padx=20, fill="both", expand=True)

        usuarios = listarTodosUsuarios()

        if not usuarios:
            ctk.CTkLabel(frame_lista, text="⚠️ Nenhum usuário encontrado.", font=("Arial", 14)).pack(pady=20)
            return

        headers = ["ID", "Nome", "Tipo", "Ações"]
        for col, header in enumerate(headers):
            ctk.CTkLabel(frame_lista, text=header, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=10, pady=5, sticky="w")

        for i, usuario in enumerate(usuarios, start=1):
            ctk.CTkLabel(frame_lista, text=str(usuario['id_usuario']), width=50, anchor="w").grid(row=i, column=0, padx=10, sticky="w")
            ctk.CTkLabel(frame_lista, text=usuario['nome'], width=200, anchor="w").grid(row=i, column=1, padx=10, sticky="w")
            ctk.CTkLabel(frame_lista, text=usuario['tipo'], width=100, anchor="w").grid(row=i, column=2, padx=10, sticky="w")

            btn_editar = ctk.CTkButton(
                frame_lista, text="✏️ Editar", width=80,
                command=lambda u=usuario: form_editar_usuario(self, u, self.show_usuarios)
            )
            btn_editar.grid(row=i, column=3, padx=5)

            btn_excluir = ctk.CTkButton(
                frame_lista,
                text="🗑️ Excluir",
                fg_color="red",
                hover_color="#aa0000",
                width=80,
                command=lambda uid=usuario['id_usuario']: self.excluir_usuario(uid)
            )
            btn_excluir.grid(row=i, column=4, padx=5)

    # Função para excluir usuários
    def excluir_usuario(self, id_usuario):
        from controller.usuarios_controller import excluirUsuarios
        resposta = messagebox.askyesno("Confirmação", "Deseja realmente excluir este usuário?")
        if resposta:
            msg = excluirUsuarios(id_usuario)
            messagebox.showinfo("Resultado", msg)
            self.show_usuarios()  # Atualiza a lista

    # ====== Turmas ======    
    def show_turmas_alunos(self):
        self.clear_main()
        from controller.turmas_controller import listarTodasTurmas
        from controller.alunos_controller import listarTodosAlunos
        from view.forms import form_cadastrar_turma, form_editar_turma, form_cadastrar_aluno, form_editar_aluno
        

        # ---------------------- TÍTULO ----------------------
        ctk.CTkLabel(
            self.main_frame,
            text=" 🏫 Gerenciamento de Turmas e Alunos",
            font=self.title_font,
            text_color=COLORS["text_dark"]
        ).pack(pady=20)

        # ---------------------- BOTÕES SUPERIORES ----------------------
        top_buttons = ctk.CTkFrame(self.main_frame)
        top_buttons.pack(pady=10)

        btn_nova_turma = ctk.CTkButton(
            top_buttons,
            text="➕ Cadastrar nova turma",
            width=200,
            height=32,
            command=lambda: form_cadastrar_turma(self, self.show_turmas_alunos)
        )
        btn_nova_turma.grid(row=0, column=0, padx=10)

        # btn_novo_aluno = ctk.CTkButton(
        #     top_buttons,
        #     text="➕ Cadastrar novo aluno",
        #     width=200,
        #     height=32,
        #     command=lambda: form_cadastrar_aluno(self, self.show_turmas_alunos)
        # )
        # btn_novo_aluno.grid(row=0, column=1, padx=10)

        # ---------------------- SCROLL LISTA ----------------------
        frame_lista = ctk.CTkScrollableFrame(self.main_frame, width=700, height=500)
        frame_lista.pack(pady=10, padx=20, fill="both", expand=True)

        # ============================================================
        #               LISTAGEM DAS TURMAS
        # ============================================================

        turmas = listarTodasTurmas()

        ctk.CTkLabel(frame_lista, text="📘 TURMAS", font=("Arial", 14, "bold")).grid(
            row=0, column=0, columnspan=4, padx=10, pady=10, sticky="w"
        )

        headers = ["ID", "Nome", "", "Ações"]
        for col, header in enumerate(headers):
            ctk.CTkLabel(
                frame_lista, text=header, font=("Arial", 12, "bold")
            ).grid(row=1, column=col, padx=10, pady=5, sticky="w")

        linha = 2  # controla a linha atual dentro do grid

        if turmas:
            for turma in turmas:
                ctk.CTkLabel(frame_lista, text=str(turma['id_turma'])).grid(row=linha, column=0, padx=10, sticky="w")
                ctk.CTkLabel(frame_lista, text=turma['nome']).grid(row=linha, column=1, padx=10, sticky="w")

                btn_editar = ctk.CTkButton(
                    frame_lista, text="✏️ Editar", width=80,
                    command=lambda t=turma: form_editar_turma(self, t, self.show_turmas_alunos)
                )
                btn_editar.grid(row=linha, column=2, padx=5)

                btn_excluir = ctk.CTkButton(
                    frame_lista,
                    text="🗑️ Excluir",
                    fg_color="red",
                    hover_color="#aa0000",
                    width=80,
                    command=lambda tid=turma['id_turma']: self.excluir_turma(tid)
                )
                btn_excluir.grid(row=linha, column=3, padx=5)

                linha += 1
        else:
            ctk.CTkLabel(frame_lista, text="Nenhuma turma encontrada.").grid(row=linha, column=0, pady=5)
            linha += 1

        # ---------------------- LINHA DIVISÓRIA ----------------------
        ctk.CTkFrame(frame_lista, height=2, fg_color="#444444").grid(
            row=linha, column=0, columnspan=8, sticky="we", pady=20
        )
        linha += 1

        # ============================================================
        #               LISTAGEM DOS ALUNOS
        # ============================================================

        alunos = listarTodosAlunos()

        ctk.CTkLabel(frame_lista, text="👨‍🎓 ALUNOS", font=("Arial", 14, "bold")).grid(
            row=linha, column=0, columnspan=4, padx=10, pady=10, sticky="w"
        )
        linha += 1

        headers_alunos = ["ID", "Nome", "Email", "Matricula", "Turma", "Ações"]
        for col, header in enumerate(headers_alunos):
            ctk.CTkLabel(
                frame_lista, text=header, font=("Arial", 12, "bold")
            ).grid(row=linha, column=col, padx=10, pady=5, sticky="w")
        linha += 1

        if alunos:
            for aluno in alunos:
                ctk.CTkLabel(frame_lista, text=str(aluno['id_aluno'])).grid(row=linha, column=0, padx=10, sticky="w")
                ctk.CTkLabel(frame_lista, text=aluno['nome']).grid(row=linha, column=1, padx=10, sticky="w")
                ctk.CTkLabel(frame_lista, text=aluno['email']).grid(row=linha, column=2, padx=10, sticky="w")
                ctk.CTkLabel(frame_lista, text=aluno['matricula']).grid(row=linha, column=3, padx=10, sticky="w")

                # NOVO: nome da turma
                turma_nome = aluno.get("turma", "Sem turma")
                ctk.CTkLabel(frame_lista, text=turma_nome).grid(row=linha, column=4, padx=10, sticky="w")

                btn_editar = ctk.CTkButton(
                    frame_lista,
                    text="✏️ Editar",
                    width=80,
                    command=lambda a=aluno: form_editar_aluno(self, a, self.show_turmas_alunos)
                )
                btn_editar.grid(row=linha, column=5, padx=5)

                btn_excluir = ctk.CTkButton(
                    frame_lista,
                    text="🗑️ Excluir",
                    fg_color="red",
                    hover_color="#aa0000",
                    width=80,
                    command=lambda aid=aluno['id_aluno']: self.excluir_aluno(aid)
                )
                btn_excluir.grid(row=linha, column=6, padx=5)

                linha += 1
        else:
            ctk.CTkLabel(frame_lista, text="Nenhum aluno encontrado.").grid(row=linha, column=0, pady=5)

    # Função para excluir turmas
    def excluir_turma(self, id_turma):
        from controller.turmas_controller import excluirTurmas
        resposta = messagebox.askyesno("Confirmação", "Deseja realmente excluir esta turma?")
        if resposta:
            msg = excluirTurmas(id_turma)
            messagebox.showinfo("Resultado", msg)
            self.show_turmas_alunos()  # Atualiza a lista

    def excluir_aluno(self, id_aluno):
        from controller.alunos_controller import excluirAlunos
        resposta = messagebox.askyesno("Confirmação", "Deseja realmente excluir este aluno?")
        if resposta:
            msg = excluirAlunos(id_aluno)
            messagebox.showinfo("Resultado", msg)
            self.show_turmas_alunos()  # Atualiza a lista de alunos


    def show_relatorios(self):
        from controller.relatorios_controller import gerarRelatorioAdmin

        self.clear_main()

        # Título
        ctk.CTkLabel(
            self.main_frame,
            text="📊 Relatórios do Sistema",
            font=self.title_font,
            text_color=COLORS["text_dark"]
        ).pack(pady=30)

        # Frame para centralizar botões
        frame = ctk.CTkFrame(self.main_frame, fg_color="white")
        frame.pack(pady=20)

        # Botão para gerar relatório simples do Admin
        btn_rel_admin = ctk.CTkButton(
            frame,
            text="📄 Gerar Relatório Geral (Admin)",
            width=260,
            height=40,
            fg_color=COLORS["accent"],
            hover_color=COLORS["accent_hover"],
            text_color="white",
            font=self.button_font,
            command=lambda: self.gerar_relatorio_admin_action()
        )
        btn_rel_admin.pack(pady=15)

    def gerar_relatorio_admin_action(self):
        from controller.relatorios_controller import gerarRelatorioAdmin

        try:
            caminho = gerarRelatorioAdmin(self.usuario)
            messagebox.showinfo(
                "Relatório Gerado",
                f"Relatório PDF criado com sucesso!\n\nLocal:\n{caminho}"
            )
        except Exception as e:
            messagebox.showerror("Erro ao gerar relatório", str(e))

    def show_chatbot(self):
        from view.chatbot_view import ChatBotFrame
        try:
            self.clear_main()
            chat_frame = ChatBotFrame(self.main_frame, self.usuario)
            chat_frame.pack(fill="both", expand=True, padx=20, pady=20)

        
        except Exception as e:
        
            messagebox.showerror("Erro no Chatbot", str(e))
