import customtkinter as ctk
from tkinter import messagebox
from view.ui_config import COLORS, get_fonts
from PIL import Image

# Controllers
from controller.aulas_controller import listarTodasAulas, deletarAulasExistentes
from controller.atividades_controller import listarTodasAtividades, deletarAtividades

# Forms
from view.forms import form_cadastrar_aula, form_editar_aula, form_cadastrar_atividade, form_editar_atividade

class DashboardProfessor(ctk.CTkToplevel):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        self.title("ClassControlPro - Painel do Professor")
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

        # === MENU LATERAL ===
        self.sidebar = ctk.CTkFrame(self, width=220, fg_color=COLORS["sidebar_bg"])
        self.sidebar.grid(row=0, column=0, sticky="nswe")
        self.sidebar.grid_rowconfigure(8, weight=1)

        # Logotipo
        logo_img = ctk.CTkImage(
            light_image=Image.open("view/components/logotipo-classcontrolpro.png"),
            size=(150, 150)
        )

        self.logo_label = ctk.CTkLabel(self.sidebar, image=logo_img, text="")
        self.logo_label.grid(row=0, column=0, pady=(20, 0), padx=20)

        self.create_sidebar_button("🏠  Início", self.show_home, 1, active=True)
        self.create_sidebar_button("🧑‍🏫  Aulas", self.show_aulas, 2)
        self.create_sidebar_button("📚  Atividades", self.show_atividades, 3)
        self.create_sidebar_button("🧾  Relatórios", self.show_relatorios, 4)

        # Botão sair
        self.btn_sair = ctk.CTkButton(
            self.sidebar, text="🚪  Sair", width=180, height=40,
            fg_color=COLORS["danger"], hover_color=COLORS["danger_hover"],
            text_color="white", corner_radius=8, command=self.quit
        )
        self.btn_sair.grid(row=9, column=0, padx=20, pady=(50,20))

        # Main frame
        self.main_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=15)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure((0,1,2), weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Inicializa com home
        self.show_home()

    # === MÉTODOS ===

    # Criação dos botões do menu lateral
    def create_sidebar_button(self, text, command, row, active=False):
        """Cria um botão lateral padronizado."""
        color = COLORS["accent"] if active else COLORS["sidebar_bg"]
        text_color = "white" if active else COLORS["text_dark"]
        hover = COLORS["accent_hover"] if active else "#E5E7EB"

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
    def create_card(self, row, col, title, value):
        card = ctk.CTkFrame(
            self.main_frame,
            fg_color=COLORS["card_bg"],
            corner_radius=15,
            border_color=COLORS["accent_hover"],
            border_width=1
        )
        card.grid(row=row, column=col, padx=15, pady=10, sticky="nsew")

        # Define tamanho fixo e evita expansão
        card.grid_propagate(False)
        card.configure(width=250, height=140)

        # Título
        ctk.CTkLabel(
            card,
            text=title,
            font=self.section_font,
            text_color=COLORS["text_dark"]
        ).pack(pady=(15, 5))

        # Valor
        ctk.CTkLabel(
            card,
            text=value,
            font=self.text_font,
            text_color=COLORS["accent"]
        ).pack(pady=(0, 10))
     
    # === TELAS ===

    # ===== Tela Inicial =====
    def show_home(self):
        self.clear_main()

        # === Título de boas-vindas ===
        ctk.CTkLabel(
            self.main_frame,
            text=f"Bem-Vindo(a), {self.usuario['nome']}!",
            font=self.title_font,
            text_color=COLORS["accent"]
        ).grid(row=0, column=0, columnspan=3, pady=(20, 30))

        # === Cards ===
        self.create_card(1, 0, "🏫 Aulas", "3 Ativas")
        self.create_card(1, 1, "📚 Atividades", "12 criadas")
        self.create_card(1, 2, "📊 Relatórios", "2 pendentes")

        # Ajuste de espaçamento e colunas
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.main_frame.grid_rowconfigure(1, weight=0)

    
    # ===== Aulas =====
    def show_aulas(self):
        self.clear_main()

        ctk.CTkLabel(
            self.main_frame,
            text="📚 Gerenciamento de Aulas",
            font=self.title_font,
            text_color=COLORS["text_dark"]
        ).grid(row=0, column=0, columnspan=3, pady=(10, 20))

        # Botão de criar aula com callback para recarregar a lista
        ctk.CTkButton(
            self.main_frame,
            text="➕ Criar Nova Aula",
            fg_color=COLORS["accent"],
            command=lambda: form_cadastrar_aula(self, self.carregar_aulas)
        ).grid(row=1, column=0, columnspan=3, pady=10)

        # Scrollable frame para lista de aulas
        self.lista_frame = ctk.CTkScrollableFrame(
            self.main_frame,
            width=850,
            height=400,
            fg_color=COLORS["card_bg"]
        )
        self.lista_frame.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=20)

        self.carregar_aulas()

    # Função que carrega as aulas dinâmicamente para a lista
    def carregar_aulas(self):
        """Atualiza dinamicamente a lista de aulas."""
         # Limpa o conteúdo anterior
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        try:
            aulas = listarTodasAulas()
        except Exception as e:
            print("Erro ao carregar aulas:", e)
            aulas = []

        if not aulas:
            ctk.CTkLabel(
                self.lista_frame,
                text="Nenhuma aula cadastrada ainda.",
                text_color=COLORS["text_light"]
            ).pack(pady=10)
            return

        # Cria um card para cada aula
        for aula in aulas:
            frame = ctk.CTkFrame(
                self.lista_frame,
                fg_color="white",
                corner_radius=10,
                height=60
            )
            frame.pack(fill="x", pady=5, padx=5)

            ctk.CTkLabel(
                frame,
                text=f"{aula['id_aula']} - {aula['titulo']} | {aula['descricao']} | Data: {aula['data_aula']}",
                anchor="w",
                text_color="black"
            ).pack(side="left", padx=10)

            # Botões de ação (editar e excluir)
            ctk.CTkButton(
                frame,
                text="✏️",
                width=50,
                fg_color=COLORS["accent_hover"],
                command=lambda a=aula: form_editar_aula(self, a, self.carregar_aulas)
            ).pack(side="right", padx=5)

            ctk.CTkButton(
                frame,
                text="🗑️",
                width=50,
                fg_color=COLORS["danger"],
                command=lambda id_aula=aula['id_aula']: self.excluir_aula(id_aula)
            ).pack(side="right", padx=5)

    # Função que possibilita visualmente o professor excluir aulas o sistema
    def excluir_aula(self, id_aula):
        """Exclui aula e atualiza a lista imediatamente."""
        resposta = messagebox.askyesno("Confirmação", "Deseja realmente excluir essa aula?")
        if resposta:
            msg = deletarAulasExistentes(id_aula)
            messagebox.showinfo("Resultado", msg)
            self.carregar_aulas()

    # ===== Atividades =====
    def show_atividades(self):
        self.clear_main()

        # Título principal
        ctk.CTkLabel(
            self.main_frame,
            text="📘 Gerenciamento de Atividades",
            font=self.title_font,
            text_color=COLORS["text_dark"]
        ).grid(row=0, column=0, columnspan=3, pady=(10, 20))

        # Botão para criar nova atividade
        ctk.CTkButton(
            self.main_frame,
            text="➕ Criar Nova Atividade",
            fg_color=COLORS["accent"],
            hover_color=COLORS["accent_hover"],
            command=lambda: form_cadastrar_atividade(self, self.carregar_atividades)
        ).grid(row=1, column=0, columnspan=3, pady=10)

        # ScrollFrame para lista
        self.lista_frame = ctk.CTkScrollableFrame(
            self.main_frame,
            width=850,
            height=420,
            fg_color=COLORS["card_bg"],
            corner_radius=12
        )
        self.lista_frame.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=20)

        # Carrega as atividades
        self.carregar_atividades()

    # Função que carrega as atividades dinâmicamente para a lista
    def carregar_atividades(self):
        """Carrega e exibe as atividades cadastradas de forma visual e organizada."""
        import datetime

        # Limpa a lista anterior
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        try:
            atividades = listarTodasAtividades()
        except Exception as e:
            print("Erro ao carregar atividades:", e)
            atividades = []

        if not atividades:
            ctk.CTkLabel(
                self.lista_frame,
                text="Nenhuma atividade cadastrada ainda.",
                text_color=COLORS["text_light"],
                font=("Arial", 14, "italic")
            ).pack(pady=20)
            return

        # Criação dos cards de atividades
        for atv in atividades:
            # === Dados formatados ===
            data_entrega = atv.get("data_entrega", "")
            try:
                data_formatada = datetime.datetime.strptime(data_entrega, "%Y-%m-%d").strftime("%d/%m/%Y")
            except:
                data_formatada = data_entrega

            titulo = atv.get("titulo", "Sem título")
            descricao = atv.get("descricao", "Sem descrição")
            status = atv.get("status", "Em andamento")  # se houver campo de status

            # === Cor do status ===
            cor_status = {
                "Concluída": "#3BA55C",
                "Em andamento": "#F1C40F",
                "Atrasada": "#E74C3C"
            }.get(status, "#95A5A6")

            # === Card principal ===
            card = ctk.CTkFrame(
                self.lista_frame,
                fg_color="white",
                corner_radius=12,
                height=120
            )
            card.pack(fill="x", pady=8, padx=10, ipadx=5)

            # === Cabeçalho da atividade ===
            ctk.CTkLabel(
                card,
                text=f"📄 {titulo}",
                font=("Arial", 15, "bold"),
                text_color="#2C3E50",
                anchor="w"
            ).pack(anchor="w", padx=15, pady=(8, 0))

            # === Descrição ===
            ctk.CTkLabel(
                card,
                text=f"{descricao}",
                font=("Arial", 13),
                text_color="#34495E",
                anchor="w",
                justify="left",
                wraplength=750
            ).pack(anchor="w", padx=15, pady=(4, 0))

            # === Rodapé com data e status ===
            footer_frame = ctk.CTkFrame(card, fg_color="transparent")
            footer_frame.pack(fill="x", padx=15, pady=(6, 0))

            ctk.CTkLabel(
                footer_frame,
                text=f"📅 Entrega: {data_formatada}",
                text_color="#555",
                font=("Arial", 12)
            ).pack(side="left")

            ctk.CTkLabel(
                footer_frame,
                text=f"● {status}",
                text_color=cor_status,
                font=("Arial", 12, "bold")
            ).pack(side="left", padx=20)

            # === Botões (editar/excluir) ===
            botoes_frame = ctk.CTkFrame(card, fg_color="transparent")
            botoes_frame.pack(anchor="e", padx=10, pady=(4, 10))

            ctk.CTkButton(
                botoes_frame,
                text="✏️ Editar",
                width=90,
                fg_color=COLORS["accent_hover"],
                hover_color=COLORS["accent"],
                command=lambda a=atv: form_editar_atividade(self, a, self.carregar_atividades)
            ).pack(side="left", padx=5)

            ctk.CTkButton(
                botoes_frame,
                text="🗑️ Excluir",
                width=90,
                fg_color=COLORS["danger"],
                hover_color="#A93226",
                command=lambda id_atividade=atv["id_atividade"]: self.excluir_atividade(id_atividade)
            ).pack(side="left", padx=5)

    # Função que possibilita visualmente o professor excluir atividades do sistema
    def excluir_atividade(self, id_atividade):
        resposta = messagebox.askyesno("Confirmação", "Deseja realmente excluir essa atividade?")
        if resposta:
            msg = deletarAtividades(id_atividade)
            messagebox.showinfo("Resultado", msg)
            self.carregar_atividades()

    # ===== Relatórios =====
    def show_relatorios(self):
        self.clear_main()
        ctk.CTkLabel(
            self.main_frame, text="Relatórios de Desempenho",
            font=self.title_font, text_color=COLORS["text_dark"]
        ).grid(row=0, column=0, columnspan=3, pady=50)



