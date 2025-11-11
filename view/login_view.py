import customtkinter as ctk
from customtkinter import ThemeManager
from CTkMessagebox import CTkMessagebox
from tkinter import messagebox

# Configuração inicial
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

def get_theme_font(name, default_kwargs):
    theme_fonts = ThemeManager.theme.get("CTkFont", {})
    cfg = theme_fonts.get(name)
    if cfg:
        font_kwargs = {}
        if "family" in cfg:
            font_kwargs["family"] = cfg["family"]
        if "size" in cfg:
            font_kwargs["size"] = cfg["size"]
        if "weight" in cfg:
            font_kwargs["weight"] = cfg["weight"]
        return ctk.CTkFont(**font_kwargs)
    return ctk.CTkFont(**default_kwargs)

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ClassControlPro - Login")
        self.geometry("900x600")
        self.configure(fg_color="#F5F5F5")
        self.resizable(False, False)

        # === Fontes ===
        self.title_font = get_theme_font("title", {"family": "Inter", "size": 22, "weight": "bold"})
        self.button_font = get_theme_font("button", {"family": "Inter", "size": 14, "weight": "bold"})
        self.small_font = get_theme_font("small", {"family": "Inter", "size": 12, "weight": "normal"})

        # === Frame de login ===
        self.login_frame = ctk.CTkFrame(self, width=400, height=400, corner_radius=15, fg_color="white")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.login_label = ctk.CTkLabel(
            self.login_frame,
            text="Bem-vindo ao ClassControlPro",
            text_color="#1F2937",
            font=self.title_font
        )
        self.login_label.pack(pady=(40, 20))

        self.email_entry = ctk.CTkEntry(
            self.login_frame, placeholder_text="Email", width=300, height=35,
            fg_color="#F5F5F5", border_color="#FDBA74"
        )
        self.email_entry.pack(pady=(10, 15))

        self.password_entry = ctk.CTkEntry(
            self.login_frame, placeholder_text="Senha", show="*",
            width=300, height=35, fg_color="#F5F5F5", border_color="#FDBA74"
        )
        self.password_entry.pack(pady=(5, 25))

        self.login_button = ctk.CTkButton(
            self.login_frame, text="Entrar", width=200, height=40,
            fg_color="#F97316", hover_color="#FDBA74", text_color="white",
            font=self.button_font, command=self.loginView
        )
        self.login_button.pack(pady=(5, 15))

        self.forgot_label = ctk.CTkLabel(
            self.login_frame, text="Esqueceu a senha?",
            text_color="#6B7280", font=self.small_font
        )
        self.forgot_label.pack()

    def loginView(self):
        
        from controller.usuarios_controller import login
        from view.dashboard_admin_view import DashboardAdmin
        from view.dashboard_professor_view import DashboardProfessor
        from view.dashboard_aluno_view import DashboardAluno

        email = self.email_entry.get().strip()
        senha = self.password_entry.get().strip()

        if not email or not senha:
            CTkMessagebox(title="Erro", message="Por favor, preencha todos os campos.")
            return

        usuario, msg = login(email, senha)
        if usuario is None:
            # CTkMessagebox(title="Sucesso", message=f"Bem-vindo, {usuario['nome']} ({usuario['tipo']})!")
            messagebox.showerror("Erro", msg)
            self.email_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')
            self.email_entry.focus()
        else:
            # Fecha tela de login   
            self.withdraw()

            # Abre o dashboard específico
            if usuario["tipo"] == "admin":                              
                DashboardAdmin(usuario)
            elif usuario["tipo"] == "professor":
                DashboardProfessor(usuario)
            elif usuario["tipo"] == "aluno":
                DashboardAluno(usuario)

            else:
                CTkMessagebox(title="Erro", message="Tipo de usuário desconhecido.")

              


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
