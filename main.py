import customtkinter as ctk
from view.login_view import loginView

def main():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("orange")

    app = ctk.CTk()
    app.geometry("1100x650")
    app.title("ClassControlPro")

    loginView(app)
    app.mainloop()

if __name__ == "__main__":
    main()
    
