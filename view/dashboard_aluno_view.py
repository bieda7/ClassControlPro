import customtkinter as ctk
from PIL import Image
from view.ui_config import COLORS, get_fonts

from controller.atividades_controller import listarTodasAtividades
from controller.aulas_controller import listarTodasAulas
from view.forms import form_entregar_atividade  # assume função existente com assinatura (master, atividade, usuario)


class DashboardAluno(ctk.CTkToplevel):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario  # usuário logado
        self.title("ClassControlPro - Painel do Aluno")
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

        # Botões do menu lateral
        self.create_sidebar_button("🏠  Início", self.show_home, 1, active=True)
        self.create_sidebar_button("📚  Minhas Atividades", self.show_atividades, 2)
        self.create_sidebar_button("📅  Conteúdo Aulas", self.show_aulas, 3)
        self.create_sidebar_button("📊  Meu Desempenho", self.show_desempenho, 4)

        # Botão Sair
        self.btn_sair = ctk.CTkButton(
            self.sidebar, text="🚪  Sair", width=180, height=40,
            fg_color=COLORS["danger"], hover_color=COLORS["danger_hover"],
            text_color="white", corner_radius=8, command=self.quit
        )
        self.btn_sair.grid(row=9, column=0, padx=20, pady=(50,20))

        # Main frame
        self.main_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=15)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)
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

    # Criação dos cards exibidos na tela home
    def create_card(self, row, col, title, value):
        """Cria um card informativo no painel principal."""
        card = ctk.CTkFrame(
            self.main_frame,
            fg_color=COLORS["card_bg"],
            corner_radius=15,
            border_color=COLORS["accent_hover"],
            border_width=1
        )
        card.grid(row=row, column=col, padx=15, pady=10, sticky="nsew")

        ctk.CTkLabel(
            card, text=title, font=self.section_font, text_color=COLORS["text_dark"]
        ).pack(pady=(15, 5))
        # use accent para o valor (texto claro com bom contraste)
        ctk.CTkLabel(
            card, text=value, font=self.text_font, text_color=COLORS["accent"]
        ).pack(pady=(0, 15))

    # === UTILITÁRIOS ===
    # Função para limpar a tela sempre ao carregar conteúdos novos
    # Essa função é chamada dentr de muitas outras, para deixar um visual limpo sempre que necessário
    def clear_main(self):
        """Remove todos os widgets do main_frame antes de carregar nova tela."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # === TELAS ===

    # ===== Tela Inicial ======
    def show_home(self):
        self.clear_main()
        ctk.CTkLabel(
            self.main_frame,
            text=f"Bem-vindo(a), {self.usuario['nome']}!",
            font=self.title_font,
            text_color=COLORS["accent"]  # Destaque vibrante no título
        ).grid(row=0, column=0, columnspan=3, pady=(20, 30))

        # === Cards ===
        self.create_card(1, 0, "📚 Atividades", "5 Pendentes")
        self.create_card(1, 1, "🏫 Aulas", "2 Ativas")
        self.create_card(1, 2, "⭐ Desempenho", "87%")

        # Ajuste de espaçamento e colunas
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.main_frame.grid_rowconfigure(1, weight=0)

    # ===== Atividades =====
    def show_atividades(self):
        self.clear_main()

        # Título principal
        ctk.CTkLabel(
            self.main_frame,
            text="📘 Acompanhamento de Atividades",
            font=self.title_font,
            text_color=COLORS["text_dark"]
        ).grid(row=0, column=0, columnspan=3, pady=(10, 20))

        # ScrollFrame para lista
        self.lista_frame = ctk.CTkScrollableFrame(
            self.main_frame,
            width=850,
            height=420,
            fg_color=COLORS["card_bg"],
            corner_radius=12
        )
        self.lista_frame.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=10)

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

        # debug rápido (retire em produção se quiser)
        # print("DEBUG - atividades retornadas:", type(atividades), atividades)

        if not atividades:
            ctk.CTkLabel(
                self.lista_frame,
                text="Nenhuma atividade cadastrada ainda.",
                text_color=COLORS["text_dark"],
                font=self.text_font
            ).pack(pady=20)
            return

        # Criação dos cards de atividades (mais compactos: pady pequeno)
        for atv in atividades:
            # === Dados formatados ===
            data_entrega = atv.get("data_entrega") or atv.get("data") or ""
            try:
                data_formatada = datetime.datetime.strptime(data_entrega, "%Y-%m-%d").strftime("%d/%m/%Y")
            except Exception:
                data_formatada = data_entrega

            # tenta tirar título de chaves possíveis
            titulo = atv.get("titulo") or atv.get("id_titulo") or "Sem título"
            descricao = atv.get("descricao") or "Sem descrição"
            status = atv.get("status") or "Em andamento"

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
                corner_radius=12
            )
            # espaço vertical menor para cards ficarem compactos
            card.pack(fill="x", pady=6, padx=10, ipadx=5)

            # === Cabeçalho da atividade ===
            ctk.CTkLabel(
                card,
                text=f"📄 {titulo}",
                font=self.section_font,
                text_color=COLORS["text_dark"],
                anchor="w"
            ).pack(anchor="w", padx=15, pady=(10, 0))

            # === Descrição ===
            ctk.CTkLabel(
                card,
                text=f"{descricao}",
                font=self.text_font,
                text_color="#34495E",
                anchor="w",
                justify="left",
                wraplength=760
            ).pack(anchor="w", padx=15, pady=(6, 6))

            # === Rodapé com data e status e botões ===
            footer_frame = ctk.CTkFrame(card, fg_color="transparent")
            footer_frame.pack(fill="x", padx=15, pady=(0, 8))

            # Data à esquerda
            ctk.CTkLabel(
                footer_frame,
                text=f"📅 Entrega: {data_formatada}",
                text_color="#555",
                font=self.text_font
            ).pack(side="left")

            # Status próximo à data
            ctk.CTkLabel(
                footer_frame,
                text=f"● {status}",
                text_color=cor_status,
                font=self.text_font
            ).pack(side="left", padx=12)

            # Botões à direita (Enviar primeiro, depois futuros botões)
            botoes_frame = ctk.CTkFrame(footer_frame, fg_color="transparent")
            botoes_frame.pack(side="right")

            # Botão Enviar — passa a atividade completa e usuário logado ao formulário
            
            ctk.CTkButton(
                card,
                text="📤 Enviar Atividade",
                fg_color=COLORS["accent"],
                hover_color=COLORS["accent_hover"],
                text_color="white",
                corner_radius=10,
                font=self.button_font,
                command=lambda atv_id=atv["id_atividade"]: form_entregar_atividade(self.usuario, atv_id)
            ).pack(pady=(10, 15))

            # (se quiser, coloque aqui botões extras — ex.: ver entrega, cancelar, etc.)
   
    # ===== Aulas ======
    def show_aulas(self):
        self.clear_main()
        ctk.CTkLabel(
            self.main_frame,
            text=" 📚 Conteúdo das Aulas",
            font=self.title_font,
            text_color=COLORS["text_dark"]
        ).grid(row=0, column=0, columnspan=3, pady=(10, 20))

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
    
    # Visualização de desempenho individual
    def show_desempenho(self):
        self.clear_main()
        ctk.CTkLabel(
            self.main_frame,
            text="Meu Desempenho",
            font=self.title_font,
            text_color=COLORS["text_dark"]
        ).pack(pady=50)

