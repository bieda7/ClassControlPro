import customtkinter as ctk

# ========= PALETA DE CORES =========
COLORS = {
    "bg": "#F5F5F5",
    "accent": "#F97316",
    "accent_hover": "#FDBA74",
    "text_dark": "#1F2937",
    "text_light": "#6B7280",
    "card_bg": "#F9FAFB",
    "danger": "#DC2626",
    "danger_hover": "#EF4444",
    "sidebar_bg": "white"
}


# ========= FUNÇÃO DE FONTES =========
def get_fonts():
    """Cria as fontes APÓS a janela principal (CTk) existir."""
    return {
        "title": ctk.CTkFont(family="Inter", size=22, weight="bold"),
        "section": ctk.CTkFont(family="Inter", size=16, weight="bold"),
        "text": ctk.CTkFont(family="Inter", size=13),
        "button": ctk.CTkFont(family="Inter", size=14, weight="bold"),
    }
