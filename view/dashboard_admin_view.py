import customtkinter as ctk
from tkinter import messagebox
from view.ui_config import COLORS, get_fonts


class DashboardAdmin(ctk.CTkToplevel):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario  # usuário logado
        self.title("ClassControlPro - Painel do Administrador")
        self.geometry("1100x650")
        self.configure(fg_color=COLORS["bg"])
        self.resizable(False, False)

        # Fontes
        FONTS = get_fonts()
        self.title_font = FONTS["title"]
        self.section_font = FONTS["section"]
        self.text_font = FONTS["text"]
        self.button_font = FONTS["button"]

        # Estrutura principal
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ===== MENU LATERAL =====
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color=COLORS["sidebar_bg"])
        self.sidebar.grid(row=0, column=0, sticky="nswe")
        self.sidebar.grid_rowconfigure(8, weight=1)

        ctk.CTkLabel(
            self.sidebar, text="ClassControlPro",
            font=self.title_font, text_color=COLORS["text_dark"]
        ).grid(row=0, column=0, padx=20, pady=(30, 30))

        self.create_sidebar_button("🏠  Início", self.show_home, 1, True)
        self.create_sidebar_button("👥  Usuários", self.show_usuarios, 2)
        self.create_sidebar_button("🏫  Turmas", self.show_turmas, 3)
        self.create_sidebar_button("🧩  Permissões", self.show_permissoes, 4)
        self.create_sidebar_button("📊  Relatórios", self.show_relatorios, 5)

        # Botão sair
        self.btn_sair = ctk.CTkButton(
            self.sidebar, text="🚪  Sair", width=180, height=40,
            fg_color=COLORS["danger"], hover_color=COLORS["danger_hover"],
            text_color="white", corner_radius=8, command=self.sair
        )
        self.btn_sair.grid(row=9, column=0, padx=20, pady=(50, 20))

        # ===== ÁREA PRINCIPAL =====
        self.main_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=15)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.show_home()

    # ====== Métodos ======
    def create_sidebar_button(self, text, command, row, active=False):
        color = COLORS["accent"] if active else COLORS["sidebar_bg"]
        text_color = "white" if active else COLORS["text_dark"]
        hover = COLORS["accent_hover"] if active else "#E5E7EB"

        btn = ctk.CTkButton(
            self.sidebar, text=text, width=180, height=40,
            fg_color=color, hover_color=hover,
            text_color=text_color, corner_radius=8, font=self.button_font,
            command=command
        )
        btn.grid(row=row, column=0, padx=20, pady=10)

    def clear_main(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def create_card(self, row, col, title, value):
        card = ctk.CTkFrame(self.main_frame, fg_color=COLORS["card_bg"], corner_radius=15, border_color=COLORS["accent_hover"], border_width=1)
        card.grid(row=row, column=col, padx=15, pady=10, sticky="nsew")
        ctk.CTkLabel(card, text=title, font=self.section_font, text_color=COLORS["text_dark"]).pack(pady=(15, 5))
        ctk.CTkLabel(card, text=value, font=self.text_font, text_color=COLORS["text_light"]).pack(pady=(0, 15))

    # ====== Telas ======
    def show_home(self):
        self.clear_main()

        from controller.usuarios_controller import contarUsuarios
        from controller.turmas_controller import contarTurmas

        total_usuarios = contarUsuarios()
        total_turmas = contarTurmas()
        total_relatorios = 0 # Atualizar quando tiver o módulo relatórios feito

        ctk.CTkLabel(self.main_frame, text="Visão Geral do Sistema", font=self.title_font, text_color=COLORS["text_dark"]).grid(row=0, column=0, columnspan=3, pady=(20, 30))
        self.create_card(1, 0, "👥 Usuários", f"Total: {total_usuarios}") # Pode buscar dinamicamente do banco
        self.create_card(1, 1, "🏫 Turmas", f"Ativas: {total_turmas}")
        self.create_card(1, 2, "📊 Relatórios", "Hoje: 5")

    def show_usuarios(self):

        from controller.usuarios_controller import listarTodosUsuarios
        from view.forms import form_cadastrar_usuario, form_editar_usuario

        self.clear_main()

        ctk.CTkLabel(
            self.main_frame,
            text="Gerenciamento de Usuários",
            font=self.title_font,
            text_color=COLORS["text_dark"]
        ).pack(pady=20)

    
     # BOTÃO DE NOVO USUÁRIO
   
        btn_novo_usuario = ctk.CTkButton(
            self.main_frame,
            text="➕ Cadastrar novo usuário",
            width=200,
            height=32,
            command=lambda: form_cadastrar_usuario(self, self.show_usuarios)
        )
        btn_novo_usuario.pack(pady=10)

        # LISTAGEM USUÁRIO

        frame_lista = ctk.CTkScrollableFrame(self.main_frame, width=700, height=400)
        frame_lista.pack(pady=10, padx=20, fill="both", expand=True)

        usuarios = listarTodosUsuarios()

        if not usuarios:
            ctk.CTkLabel(frame_lista, text="⚠️ Nenhum usuário encontrado.", font=("Arial", 14)).pack(pady=20)
            return

        headers = ["ID", "Nome", "Tipo", "Ações"]
        for col, header in enumerate(headers):
            ctk.CTkLabel(frame_lista, text=header, font=("Arial", 12, "bold")).grid(
                row=0, column=col, padx=10, pady=5, sticky="w"
            )

        for i, usuario in enumerate(usuarios, start=1):
            ctk.CTkLabel(frame_lista, text=str(usuario['id_usuario']), width=50, anchor="w").grid(
                row=i, column=0, padx=10, sticky="w"
            )
            ctk.CTkLabel(frame_lista, text=usuario['nome'], width=200, anchor="w").grid(
                row=i, column=1, padx=10, sticky="w"
            )
            ctk.CTkLabel(frame_lista, text=usuario['tipo'], width=100, anchor="w").grid(
                row=i, column=2, padx=10, sticky="w"
            )

            btn_editar = ctk.CTkButton(
                frame_lista,
                text="✏️ Editar",
                width=80,
                command=lambda u=usuario: form_editar_usuario(
                    self, u, self.show_usuarios
                )
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

    def excluir_usuario(self, id_usuario):

        from controller.usuarios_controller import excluirUsuarios

        resposta = messagebox.askyesno("Confirmação", "Deseja realmente excluir este usuário?")
        if resposta:
            msg = excluirUsuarios(id_usuario)
            messagebox.showinfo("Resultado", msg)
            self.show_usuarios()  # Atualiza a lista

    def show_turmas(self):

        from controller.turmas_controller import listarTodasTurmas, cadastrarTurmas
        from view.forms import form_cadastrar_turma, form_editar_turma

        self.clear_main()

        ctk.CTkLabel(
            self.main_frame,
            text="Gerenciamento de Turmas",
            font=self.title_font,
            text_color=COLORS["text_dark"]
        ).pack(pady=20)

        btn_nova_turma = ctk.CTkButton(
            self.main_frame,
            text="➕ Cadastrar nova turma",
            width=200,
            height=32,
            command=lambda: form_cadastrar_turma(self, self.show_turmas)
        )
        btn_nova_turma.pack(pady=10)

        frame_lista = ctk.CTkScrollableFrame(self.main_frame, width=700, height=400)
        frame_lista.pack(pady=10, padx=20, fill="both", expand=True)

        # Lista todas as turmas
        turmas = listarTodasTurmas()

        if not turmas:
            ctk.CTkLabel(frame_lista, text="⚠️ Nenhuma turma encontrada.", font=("Arial", 14)).pack(pady=20)
            return

        # Cabeçalho
        headers = ["ID", "Nome", "Ações"]
        for col, header in enumerate(headers):
            ctk.CTkLabel(frame_lista, text=header, font=("Arial", 12, "bold")).grid(
                row=0, column=col, padx=10, pady=5, sticky="w"
            )

        # Linhas de turmas
        for i, turma in enumerate(turmas, start=1):
            ctk.CTkLabel(frame_lista, text=str(turma['id_turma']), width=50, anchor="w").grid(
                row=i, column=0, padx=10, sticky="w"
            )
            ctk.CTkLabel(frame_lista, text=turma['nome'], width=200, anchor="w").grid(
                row=i, column=1, padx=10, sticky="w"
            )

            # Botão de editar → chama form do forms.py
            btn_editar = ctk.CTkButton(
                frame_lista,
                text="✏️ Editar",
                width=80,
                command=lambda t=turma: form_editar_turma(
                    self, t, self.show_turmas
                )
            )
            btn_editar.grid(row=i, column=2, padx=5)

            # Botão de excluir → chama método da classe
            btn_excluir = ctk.CTkButton(
                frame_lista,
                text="🗑️ Excluir",
                fg_color="red",
                hover_color="#aa0000",
                width=80,
                command=lambda tid=turma['id_turma']: self.excluir_turma(tid)
            )
            btn_excluir.grid(row=i, column=3, padx=5)

    def excluir_turma(self, id_turma):

        from controller.turmas_controller import excluirTurmas

        resposta = messagebox.askyesno("Confirmação", "Deseja realmente excluir esta turma?")
        if resposta:
            msg = excluirTurmas(id_turma)
            messagebox.showinfo("Resultado", msg)
            self.show_turmas()  # Atualiza a lista
            
    def show_permissoes(self):
        self.clear_main()
        ctk.CTkLabel(self.main_frame, text="Controle de Acessos e Permissões", font=self.title_font, text_color=COLORS["text_dark"]).pack(pady=50)

    def show_relatorios(self):
        self.clear_main()
        ctk.CTkLabel(self.main_frame, text="Relatórios do Sistema", font=self.title_font, text_color=COLORS["text_dark"]).pack(pady=50)

    def sair(self):
    # """Fecha o dashboard e retorna à tela de login"""
        self.withdraw()
        from view.login_view import LoginApp
        LoginApp()

if __name__ == "__main__":
    usuario_dummy = {"nome": "Admin"}  # Exemplo de usuário logado
    app = DashboardAdmin(usuario_dummy)
    app.mainloop()
