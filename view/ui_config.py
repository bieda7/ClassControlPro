import customtkinter as ctk

# ========= PALETA DE CORES =========
COLORS = {
    # Fundo geral da aplicação
    "bg": "#FFFAFA",

    # Tons principais (laranja moderno, vibrante e quente)
    "accent": "#FF6B00",          # Laranja principal (vibrante e mais profundo)
    "accent_hover": "#FF8C33",    # Hover mais claro, suave e quente

    # Texto (claro e escuro)
    "text_dark": "#1E1E1E",       # Texto padrão escuro — melhora contraste
    "text_light": "#FFFFFF",      # Texto claro (usado em botões ativos)

    # Elementos de cartão / painel
    "card_bg": "#FFFFFF",

    # Botões de perigo
    "danger": "#DC2626",
    "danger_hover": "#EF4444",

    # Sidebar
    "sidebar_bg": "#FFFFFF",      # Fundo branco puro — limpo e leve
    "sidebar_border": "#E5E7EB",  # Linha sutil de separação (cinza claro)
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
