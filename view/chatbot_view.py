import customtkinter as ctk
import time
import threading
from controller.chatbot_controller import (
    obter_perguntas,
    obter_resposta,
    adicionar_ao_historico,
    obter_historico
)

class ChatBotFrame(ctk.CTkFrame):

    def __init__(self, master, usuario):
        super().__init__(master)

        self.usuario = usuario
        self.tipo_usuario = usuario["tipo"]

        # Título
        titulo = ctk.CTkLabel(self, text="🤖 Assistente do Sistema", font=("Arial", 22, "bold"))
        titulo.pack(pady=10)

        # Área do chat (com scroll)
        self.chat_frame = ctk.CTkScrollableFrame(self, width=550, height=350, fg_color="#f1f1f1")
        self.chat_frame.pack(pady=10)

        # Histórico
        self.exibir_historico()

        # Opções rápidas
        self.opcoes_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.opcoes_frame.pack(pady=10)

        self.exibir_opcoes()



    # -----------------------------------------
    # HISTÓRICO
    # -----------------------------------------
    def exibir_historico(self):
        historico = obter_historico()
        for msg in historico:
            if msg["tipo"] == "user":
                self.mostrar_msg_usuario(msg["mensagem"])
            else:
                self.mostrar_msg_bot(msg["mensagem"])


    # -----------------------------------------
    # BOTÕES DE PERGUNTAS RÁPIDAS
    # -----------------------------------------
    def exibir_opcoes(self):
        perguntas = obter_perguntas(self.tipo_usuario)

        # limpa antes de recriar, evita duplicações
        for widget in self.opcoes_frame.winfo_children():
            widget.destroy()

        for pergunta in perguntas:
            btn = ctk.CTkButton(
                self.opcoes_frame,
                text=pergunta,
                command=lambda p=pergunta: self.enviar_pergunta(p),
                width=500
            )
            btn.pack(pady=5)


    # -----------------------------------------
    # UI → MENSAGEM DO USUÁRIO
    # -----------------------------------------
    def mostrar_msg_usuario(self, texto):
        frame = ctk.CTkFrame(self.chat_frame, fg_color="white")
        frame.pack(fill="x", pady=5, padx=5, anchor="e")

        ctk.CTkLabel(frame, text="🧑‍💻", font=("Arial", 28)).pack(side="right", padx=5)
        ctk.CTkLabel(frame, text=texto, anchor="e", justify="right", wraplength=400).pack(side="right", padx=5)


    # -----------------------------------------
    # UI → MENSAGEM DO BOT
    # -----------------------------------------
    def mostrar_msg_bot(self, texto):
        frame = ctk.CTkFrame(self.chat_frame, fg_color="#e9e9e9")
        frame.pack(fill="x", pady=5, padx=5, anchor="w")

        ctk.CTkLabel(frame, text="🤖", font=("Arial", 28)).pack(side="left", padx=5)
        ctk.CTkLabel(frame, text=texto, anchor="w", justify="left", wraplength=400).pack(side="left", padx=5)


    # -----------------------------------------
    # ANIMAÇÃO DE DIGITAÇÃO
    # -----------------------------------------
    def digitar_texto(self, texto):
        frame = ctk.CTkFrame(self.chat_frame, fg_color="#e9e9e9")
        frame.pack(fill="x", pady=5, padx=5, anchor="w")

        ctk.CTkLabel(frame, text="🤖", font=("Arial", 28)).pack(side="left", padx=5)
        label = ctk.CTkLabel(frame, text="", anchor="w", justify="left", wraplength=400)
        label.pack(side="left", padx=5)

        def animar():
            texto_final = ""
            for char in texto:
                texto_final += char
                label.configure(text=texto_final)
                time.sleep(0.02)

        threading.Thread(target=animar, daemon=True).start()


    # -----------------------------------------
    # ENVIAR PERGUNTA E OBTER RESPOSTA
    # -----------------------------------------
    def enviar_pergunta(self, pergunta):

        self.mostrar_msg_usuario(pergunta)
        adicionar_ao_historico("user", pergunta)

        resposta = obter_resposta(pergunta, self.tipo_usuario)
        adicionar_ao_historico("bot", resposta)

        self.digitar_texto(resposta)

        self.after(150, lambda: self.chat_frame._parent_canvas.yview_moveto(1))
