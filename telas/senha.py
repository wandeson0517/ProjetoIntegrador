import customtkinter as ctk
from tkinter import messagebox

# Configuração global do tema
ctk.set_appearance_mode("light")  
ctk.set_default_color_theme("blue")

# Banco de dados simulado (substitua pelo seu banco real como SQLite, MySQL, etc.)
usuarios_db = {
    "admin": "12345"
}

class JanelaAlterarSenha(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configurações da Janela
        self.title("MecDesk - Alterar Senha")
        self.geometry("900x550")
        self.resizable(False, False)
        
        # --- LAYOUT PRINCIPAL (DIVISÃO EM DUAS COLUNAS) ---
        # Coluna da Esquerda (Menu Azul Escuro)
        self.frame_esquerdo = ctk.CTkFrame(self, width=280, corner_radius=0, fg_color="#102C44")
        self.frame_esquerdo.pack(side="left", fill="y")
        self.frame_esquerdo.pack_propagate(False)
        
        # Coluna da Direita (Área de Conteúdo Clara)
        self.frame_direito = ctk.CTkFrame(self, corner_radius=0, fg_color="#F0F2F5")
        self.frame_direito.pack(side="right", fill="both", expand=True)
        
        # --- ELEMENTOS DA ESQUERDA (MENU) ---
        # Logo placeholder
        self.lbl_logo = ctk.CTkLabel(self.frame_esquerdo, text="MECDESK", font=("Arial", 24, "bold"), text_color="white")
        self.lbl_logo.pack(pady=(40, 50))
        
        # Botões de navegação simulados
        self.btn_cadastrar = ctk.CTkButton(self.frame_esquerdo, text="👤 Cadastrar Usuário", fg_color="transparent", text_color="white", anchor="w", font=("Arial", 14))
        self.btn_cadastrar.pack(fill="x", padx=20, pady=10)
        
        self.btn_alterar = ctk.CTkButton(self.frame_esquerdo, text="🔒 Alterar a Senha", fg_color="#1E3E5A", text_color="white", anchor="w", font=("Arial", 14, "bold"))
        self.btn_alterar.pack(fill="x", padx=20, pady=10)

        # --- ELEMENTOS DA DIREITA (FORMULÁRIO DE ALTERAÇÃO) ---
        # Título superior da página
        self.lbl_titulo_pag = ctk.CTkLabel(self.frame_direito, text="Alterar Senha do Sistema", font=("Arial", 22, "bold"), text_color="#333333")
        self.lbl_titulo_pag.pack(anchor="w", padx=50, pady=(30, 5))
        
        self.lbl_subtitulo = ctk.CTkLabel(self.frame_direito, text="Preencha os campos abaixo para atualizar suas credenciais.", font=("Arial", 13), text_color="#666666")
        self.lbl_subtitulo.pack(anchor="w", padx=50, pady=(0, 20))
        
        # Card Centralizado Branco para o Formulário
        self.card_form = ctk.CTkFrame(self.frame_direito, width=500, height=380, fg_color="white", corner_radius=10)
        self.card_form.pack(pady=10, padx=50, fill="both", expand=True)
        self.card_form.pack_propagate(False)
        
        # Título interno do Formulário
        self.lbl_form_title = ctk.CTkLabel(self.card_form, text="REDEFINIR", font=("Arial", 18, "bold"), text_color="#111111")
        self.lbl_form_title.pack(pady=(25, 15), anchor="w", padx=40)
        
        # Campo: Nome do Usuário
        self.lbl_user = ctk.CTkLabel(self.card_form, text="🏷️ Nome do Usuário", font=("Arial", 13, "bold"), text_color="#333333")
        self.lbl_user.pack(anchor="w", padx=40, pady=(5, 2))
        self.entry_usuario = ctk.CTkEntry(self.card_form, placeholder_text="Informe o nome do usuário", width=420, height=35)
        self.entry_usuario.pack(padx=40, pady=(0, 15))
        
        # Campo: Senha Atual
        self.lbl_senha_atual = ctk.CTkLabel(self.card_form, text="🔑 Senha Atual", font=("Arial", 13, "bold"), text_color="#333333")
        self.lbl_senha_atual.pack(anchor="w", padx=40, pady=(5, 2))
        self.entry_senha_atual = ctk.CTkEntry(self.card_form, placeholder_text="Informe a senha atual", show="*", width=420, height=35)
        self.entry_senha_atual.pack(padx=40, pady=(0, 15))
        
        # Campo: Nova Senha
        self.lbl_nova_senha = ctk.CTkLabel(self.card_form, text="✨ Nova Senha", font=("Arial", 13, "bold"), text_color="#333333")
        self.lbl_nova_senha.pack(anchor="w", padx=40, pady=(5, 2))
        self.entry_nova_senha = ctk.CTkEntry(self.card_form, placeholder_text="Digite a nova senha", show="*", width=420, height=35)
        self.entry_nova_senha.pack(padx=40, pady=(0, 25))
        
        # Botão Alterar (Estilo MecDesk)
        self.btn_salvar = ctk.CTkButton(self.card_form, text="ALTERAR SENHA", command=self.executar_alteracao, fg_color="#102C44", hover_color="#1C466B", text_color="white", font=("Arial", 14, "bold"), height=40, width=420)
        self.btn_salvar.pack(padx=40)

    def executar_alteracao(self):
        usuario = self.entry_usuario.get().strip()
        senha_atual = self.entry_senha_atual.get()
        nova_senha = self.entry_nova_senha.get()
        
        # Validação de campos vazios
        if not usuario or not senha_atual or not nova_senha:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos do formulário.")
            return
            
        # Verificação do Usuário e Senha Atual no "banco de dados"
        if usuario in usuarios_db:
            if usuarios_db[usuario] == senha_atual:
                # Atualiza a senha
                usuarios_db[usuario] = nova_senha
                messagebox.showinfo("Sucesso", f"A senha do usuário '{usuario}' foi alterada com sucesso!")
                
                # Limpa os campos após o sucesso
                self.entry_usuario.delete(0, 'end')
                self.entry_senha_atual.delete(0, 'end')
                self.entry_nova_senha.delete(0, 'end')
            else:
                messagebox.showerror("Erro de Autenticação", "A senha atual informada está incorreta.")
        else:
            messagebox.showerror("Erro", "Usuário não encontrado no sistema.")

if __name__ == "__main__":
    app = JanelaAlterarSenha()
    app.mainloop()