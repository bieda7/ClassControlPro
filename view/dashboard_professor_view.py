import customtkinter as ctk
from view.ui_config import COLORS, get_fonts

class DashboardProfessor(ctk.CTkToplevel):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        self.title("ClassControlPro - Painel do Professor")
        self.geometry("1100x650")
        self.configure(fg_color=COLORS["bg"])
        self.resizable(False, False)

        FONTS = get_fonts()
        self.title_font = FONTS["title"]
        self.section_font = FONTS["section"]
        self.text_font = FONTS["text"]
        self.button_font = FONTS["button"]

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=220, fg_color=COLORS["sidebar_bg"])
        self.sidebar.grid(row=0, column=0, sticky="nswe")
        self.sidebar.grid_rowconfigure(8, weight=1)

        ctk.CTkLabel(self.sidebar, text="ClassControlPro", font=self.title_font, text_color=COLORS["text_dark"]).grid(row=0, column=0, padx=20, pady=(30, 30))

        self.create_sidebar_button("🏠  Início", self.show_home, 1, True)
        self.create_sidebar_button("🧑‍🏫  Minhas Turmas", self.show_turmas, 2)
        self.create_sidebar_button("📚  Atividades", self.show_atividades, 3)
        self.create_sidebar_button("🧾  Relatórios", self.show_relatorios, 4)

        self.btn_sair = ctk.CTkButton(self.sidebar, text="🚪  Sair", width=180, height=40, fg_color=COLORS["danger"], hover_color=COLORS["danger_hover"], text_color="white", corner_radius=8, command=self.quit)
        self.btn_sair.grid(row=9, column=0, padx=20, pady=(50, 20))

        self.main_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=15)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.show_home()

    def create_sidebar_button(self, text, command, row, active=False):
        color = COLORS["accent"] if active else COLORS["sidebar_bg"]
        text_color = "white" if active else COLORS["text_dark"]
        hover = COLORS["accent_hover"] if active else "#E5E7EB"
        btn = ctk.CTkButton(self.sidebar, text=text, width=180, height=40, fg_color=color, hover_color=hover, text_color=text_color, corner_radius=8, font=self.button_font, command=command)
        btn.grid(row=row, column=0, padx=20, pady=10)

    def clear_main(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_main()
        ctk.CTkLabel(self.main_frame, text="Visão Geral - Professor", font=self.title_font, text_color=COLORS["text_dark"]).grid(row=0, column=0, columnspan=3, pady=(20, 30))
        self.create_card(1, 0, "🏫 Minhas Turmas", "3 Ativas")
        self.create_card(1, 1, "📚 Atividades", "12 criadas")
        self.create_card(1, 2, "📊 Relatórios", "2 pendentes")

    def create_card(self, row, col, title, value):
        card = ctk.CTkFrame(self.main_frame, fg_color=COLORS["card_bg"], corner_radius=15, border_color=COLORS["accent_hover"], border_width=1)
        card.grid(row=row, column=col, padx=15, pady=10, sticky="nsew")
        ctk.CTkLabel(card, text=title, font=self.section_font, text_color=COLORS["text_dark"]).pack(pady=(15, 5))
        ctk.CTkLabel(card, text=value, font=self.text_font, text_color=COLORS["text_light"]).pack(pady=(0, 15))

    def show_turmas(self):
        self.clear_main()
        ctk.CTkLabel(self.main_frame, text="Minhas Turmas", font=self.title_font, text_color=COLORS["text_dark"]).pack(pady=50)

    def show_atividades(self):
        self.clear_main()
        ctk.CTkLabel(self.main_frame, text="Gerenciamento de Atividades", font=self.title_font, text_color=COLORS["text_dark"]).pack(pady=50)

    def show_relatorios(self):
        self.clear_main()
        ctk.CTkLabel(self.main_frame, text="Relatórios de Desempenho", font=self.title_font, text_color=COLORS["text_dark"]).pack(pady=50)


if __name__ == "__main__":
    app = DashboardProfessor()
    app.mainloop()
