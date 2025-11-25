import customtkinter as ctk
from tkinter import messagebox
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
        self.create_sidebar_button("📊  Meu Desempenho", self.show_relatorios, 4)
        self.create_sidebar_button("📥  Entregas / Devoluções", self.show_entregas, 5)
        self.create_sidebar_button("📊  Chatbot", self.show_chatbot, 6  )


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
    # def create_card(self, row, col, title, value):
    #     """Cria um card informativo no painel principal."""
    #     card = ctk.CTkFrame(
    #         self.main_frame,
    #         fg_color=COLORS["card_bg"],
    #         corner_radius=15,
    #         border_color=COLORS["accent_hover"],
    #         border_width=1
    #     )
    #     card.grid(row=row, column=col, padx=15, pady=10, sticky="nsew")

    #     ctk.CTkLabel(
    #         card, text=title, font=self.section_font, text_color=COLORS["text_dark"]
    #     ).pack(pady=(15, 5))
    #     # use accent para o valor (texto claro com bom contraste)
    #     ctk.CTkLabel(
    #         card, text=value, font=self.text_font, text_color=COLORS["accent"]
    #     ).pack(pady=(0, 15))

    # === UTILITÁRIOS ===
    # Função para limpar a tela sempre ao carregar conteúdos novos
    # Essa função é chamada dentr de muitas outras, para deixar um visual limpo sempre que necessário
    def clear_main(self):
        """Remove todos os widgets do main_frame antes de carregar nova tela."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # === TELAS ===

    # ===== Tela Inicial ======
    def show_home(self, *args):
        from controller.relatorios_controller import obter_totais_dashboard

        self.clear_main()

        # === CARREGA DADOS REAIS DO BANCO ===
        totais = obter_totais_dashboard()

        total_atividades = totais["atividades"]
        total_aulas = totais["aulas"]
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
                "Este é o seu painel do Estudante!\n\n"
                "Acompanhe aulas e atividades em um só lugar\n"
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
        criar_card(0, "Total Atividades", total_atividades, COLORS["accent"])
        criar_card(2, "Aulas Disponíveis", total_aulas, COLORS["accent"])

        # ----------------------------------------------------
        # GRID RESPONSIVO
        # ----------------------------------------------------
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)
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
    def show_relatorios(self):
        from controller.relatorios_controller import gerarRelatorioAluno

        self.clear_main()

        # Título
        ctk.CTkLabel(
            self.main_frame,
            text="📊 Meus Relatórios",
            font=self.title_font,
            text_color=COLORS["text_dark"]
        ).pack(pady=30)

        # Frame central
        frame = ctk.CTkFrame(self.main_frame, fg_color="white")
        frame.pack(pady=20)

        # Botão relatório do aluno
        btn_rel_aluno = ctk.CTkButton(
            frame,
            text="📗 Gerar Meu Relatório (Atividades)",
            width=260,
            height=40,
            fg_color=COLORS["accent"],
            hover_color=COLORS["accent_hover"],
            text_color="white",
            font=self.button_font,
            command=self.gerar_relatorio_aluno_action
        )
        btn_rel_aluno.pack(pady=15)

    def gerar_relatorio_aluno_action(self):
        from controller.relatorios_controller import gerarRelatorioAluno
        try:
            caminho = gerarRelatorioAluno(self.usuario)
            messagebox.showinfo(
                "Relatório Gerado",
                f"Seu relatório foi criado com sucesso!\n\nLocal:\n{caminho}"
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

    def show_entregas(self):
        """
        Monta a tela principal e chama carregar_entregas().
        Inspirada na sua versão do professor, adaptada para o aluno.
        """
        from model.atividades_model import listarAtividadesCorrigidasAluno

        self.clear_main()

        # Título
        ctk.CTkLabel(
            self.main_frame,
            text="📥 Minhas Entregas / Devoluções",
            font=("Arial Bold", 22),
            text_color=COLORS["text_dark"]
        ).pack(pady=20)

        # Lista com scroll (onde os cards serão adicionados)
        self.lista_scroll = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color="white",
            width=850,
            height=450,
            corner_radius=12
        )
        self.lista_scroll.pack(fill="both", expand=True, padx=20, pady=10)

        # Carrega e renderiza as entregas (corrigidas)
        self.carregar_entregas()


    def carregar_entregas(self):
        """
        Busca as entregas corrigidas do aluno e renderiza cards dentro de self.lista_scroll.
        Usa listarAtividadesCorrigidasAluno(self.usuario['id_aluno']).
        """
        from model.atividades_model import listarAtividadesCorrigidasAluno
        import datetime
        from tkinter import messagebox

        # Proteção: se por acaso lista_scroll não existir, cria um fallback (evita crash)
        try:
            lista_parent = self.lista_scroll
        except AttributeError:
            # cria um scroll temporário (fallback)
            self.lista_scroll = ctk.CTkScrollableFrame(
                self.main_frame,
                fg_color="white",
                width=850,
                height=450,
                corner_radius=12
            )
            self.lista_scroll.pack(fill="both", expand=True, padx=20, pady=10)
            lista_parent = self.lista_scroll

        # limpa o conteúdo anterior
        for w in lista_parent.winfo_children():
            w.destroy()

        # Busca dados
        try:
            entregas = listarAtividadesCorrigidasAluno(self.usuario["id_aluno"])
        except Exception as e:
            print("Erro ao carregar entregas:", e)
            entregas = []

        if not entregas:
            ctk.CTkLabel(
                lista_parent,
                text="Nenhuma entrega corrigida até o momento.",
                font=("Arial", 15),
                text_color=COLORS["text_dark"]
            ).pack(pady=20)
            return

        # helper para formatar datas
        def formatar_data(dt):
            if not dt:
                return "—"
            for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
                try:
                    return datetime.datetime.strptime(dt, fmt).strftime("%d/%m/%Y %H:%M")
                except:
                    continue
            return str(dt)

        # função para abrir modal de detalhes
        def abrir_detalhes(entrega):
            modal = ctk.CTkToplevel(self)
            modal.title("Detalhes da Entrega")
            modal.geometry("800x600")
            modal.configure(fg_color=COLORS["bg"])

            # Cabeçalho
            ctk.CTkLabel(modal, text=f"📄 {entrega.get('titulo') or entrega.get('atividade', 'Atividade')}",
                        font=("Arial Bold", 18), text_color=COLORS["text_dark"]).pack(pady=(15, 5))

            # Informações (datas, nota)
            info_frame = ctk.CTkFrame(modal, fg_color="white", corner_radius=8)
            info_frame.pack(fill="x", padx=20, pady=(5, 10))

            ctk.CTkLabel(info_frame, text=f"📅 Enviado: {formatar_data(entrega.get('data_envio'))}",
                        font=self.text_font, text_color="#444").pack(anchor="w", padx=12, pady=(8, 0))
            ctk.CTkLabel(info_frame, text=f"✅ Corrigido em: {formatar_data(entrega.get('data_correcao'))}",
                        font=self.text_font, text_color="#444").pack(anchor="w", padx=12, pady=(2, 8))

            nota_text = entrega.get("nota")
            nota_text = f"⭐ Nota: {nota_text}" if nota_text is not None else "⭐ Nota: —"
            ctk.CTkLabel(info_frame, text=nota_text, font=self.text_font, text_color="#111").pack(anchor="w", padx=12, pady=(0, 12))

            # Resposta (texto grande)
            ctk.CTkLabel(modal, text="📝 Resposta enviada:", font=("Arial", 14, "bold"),
                        text_color=COLORS["text_dark"]).pack(anchor="w", padx=20, pady=(8, 4))
            resposta_text = ctk.CTkTextbox(modal, height=200, corner_radius=10, fg_color="white",
                                        border_color="#D1D5DB", border_width=1, font=("Arial", 13))
            resposta_text.insert("1.0", entrega.get("resposta") or "")
            resposta_text.configure(state="disabled")
            resposta_text.pack(fill="both", expand=False, padx=20, pady=(0, 12))

            # Observação do professor
            ctk.CTkLabel(modal, text="🧾 Observação do professor:", font=("Arial", 14, "bold"),
                        text_color=COLORS["text_dark"]).pack(anchor="w", padx=20, pady=(4, 4))
            observ_txt = entrega.get("observacao") or "Nenhuma observação registrada."
            obs_box = ctk.CTkTextbox(modal, height=120, corner_radius=10, fg_color="white",
                                    border_color="#D1D5DB", border_width=1, font=("Arial", 13))
            obs_box.insert("1.0", observ_txt)
            obs_box.configure(state="disabled")
            obs_box.pack(fill="both", expand=False, padx=20, pady=(0, 12))

            # Arquivo (se existir)
            arquivo = entrega.get("arquivo_url")
            if arquivo:
                ctk.CTkLabel(modal, text=f"📎 Arquivo: {arquivo}", font=self.text_font, text_color="#111").pack(anchor="w", padx=20, pady=(0, 12))

            # Botão fechar
            ctk.CTkButton(modal, text="Fechar", width=120, height=36, fg_color=COLORS["accent"],
                        hover_color=COLORS["accent_hover"], command=modal.destroy).pack(pady=10)

        # renderiza cards
        for entrega in entregas:
            card = ctk.CTkFrame(lista_parent, fg_color="#F8FAFC", corner_radius=12)
            card.pack(fill="x", padx=10, pady=10)

            # Título (atividade)
            titulo = entrega.get("titulo") or entrega.get("atividade") or "Sem título"
            ctk.CTkLabel(
                card,
                text=f"📘 {titulo}",
                font=("Arial", 16, "bold"),
                text_color="#1F2937",
                anchor="w"
            ).pack(anchor="w", padx=15, pady=(10, 4))

            # Data de envio / correção
            envio = formatar_data(entrega.get("data_envio"))
            correcao = formatar_data(entrega.get("data_correcao"))
            ctk.CTkLabel(card, text=f"🕒 Enviado: {envio}   •   ✅ Corrigido em: {correcao}",
                        font=("Arial", 13), text_color="#4B5563", anchor="w").pack(anchor="w", padx=15)

            # Resposta curta (textbox desabilitado)
            ctk.CTkLabel(card, text="📝 Resposta enviada:", font=("Arial", 14, "bold"),
                        text_color="#1F2937").pack(anchor="w", padx=15, pady=(8, 0))

            resposta_box = ctk.CTkTextbox(
                card,
                height=110,
                corner_radius=10,
                fg_color="white",
                border_color="#D1D5DB",
                border_width=1,
                font=("Arial", 13)
            )
            resposta_box.insert("1.0", entrega.get("resposta") or "")
            resposta_box.configure(state="disabled")
            resposta_box.pack(fill="x", padx=15, pady=(4, 10))

            # Nota e observação
            nota_txt = "⭐ Nota ainda não atribuída" if entrega.get("nota") is None else f"⭐ Nota: {entrega.get('nota')}"
            ctk.CTkLabel(card, text=nota_txt, font=("Arial", 14, "bold"),
                        text_color="#111827", anchor="w").pack(anchor="w", padx=15, pady=(0, 6))

            if entrega.get("observacao"):
                ctk.CTkLabel(card, text=f"📝 Observação: {entrega.get('observacao')}",
                            font=("Arial", 13), text_color="#374151", wraplength=760, justify="left").pack(anchor="w", padx=15, pady=(0, 10))

            # Botão Ver Detalhes (abre modal)
            ctk.CTkButton(
                card,
                text="🔍 Ver Detalhes",
                fg_color=COLORS["accent"],
                hover_color=COLORS["accent_hover"],
                width=160,
                height=35,
                corner_radius=8,
                command=lambda e=entrega: abrir_detalhes(e)
            ).pack(padx=15, pady=(0, 15), anchor="e")
