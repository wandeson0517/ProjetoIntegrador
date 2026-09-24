import customtkinter as ctk
from PIL import Image
from tkinter import ttk, messagebox

### Configurações globais de estilo

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

### Inicialização da Janela

app = ctk.CTk()
app.title("MecDesk - Login")
app.geometry("1200x700")
app.resizable(False, False)

### Paleta de Cores (Azul-petróleo / Teal)

COR_PRIMARIA = "#122B43"
COR_HOVER = "#294967"
COR_TEXTO_SECUNDARIO = "#52677F"

### ===========================================

### PAINEL ESQUERDO

### ===========================================

frame_esquerdo = ctk.CTkFrame(
app,
width=300,
fg_color=COR_PRIMARIA,
corner_radius=0)
frame_esquerdo.place(x=0, y=0, relheight=1)

###============================
### IMAGENS DO LOGOTIPO

logotipo= ctk.CTkImage(
    dark_image=Image.open("assents/mecdesk_img.jpg"),
    size=(200, 100),
)
label_imagem= ctk.CTkLabel(app, image=logotipo, text="", fg_color=COR_PRIMARIA)
label_imagem.place(x=50,y=30)

### Título da Marca

# titulo_sistema = ctk.CTkLabel(
# frame_esquerdo,
# # text="MecDesk Sistema",
# font=ctk.CTkFont(size=23, weight="bold"),
# text_color="white")
# titulo_sistema.place(anchor="w", x=27, y=50)

### Botões de Navegação Secundária (Definidos diretamente com width no construtor)

btn_cadastrar_usuario = ctk.CTkButton(
frame_esquerdo,
text="🪛 Cadastrar Usuário",
font=ctk.CTkFont(size=16, weight="bold"),
text_color="white",
fg_color="transparent",
hover_color=COR_HOVER,
anchor="w",
width=250,
height=40)
btn_cadastrar_usuario.place(x=27, y=150)

btn_alterar_senha = ctk.CTkButton(
frame_esquerdo,
text="🪛 Alterar a Senha",
font=ctk.CTkFont(size=16, weight="bold"),
text_color="white",
fg_color="transparent",
hover_color=COR_HOVER,
anchor="w",
width=250,
height=40)
btn_alterar_senha.place(x=27, y=200)

### Checkbox

chk_lembrar = ctk.CTkCheckBox(
frame_esquerdo,
text="Lembrar-se da senha",
text_color="white",
fg_color="white",
checkmark_color=COR_PRIMARIA,
border_color="white",
font=ctk.CTkFont(size=13))
chk_lembrar.place(x=27, y=630)

### =======================================

### PAINEL DIREITO (Cabeçalho)

### =======================================

titulo_principal = ctk.CTkLabel(
app,
text="Acessar o Sistema",
font=ctk.CTkFont(size=28, weight="bold"),
text_color="black",)
titulo_principal.place(x=350, y=40)

subtitulo_principal = ctk.CTkLabel(
app,
text="Soluções inteligentes para gerenciamento de sua oficina mecânica.",
font=ctk.CTkFont(size=15),
text_color=COR_TEXTO_SECUNDARIO)
subtitulo_principal.place(x=350, y=75)

### ========================================

### CAIXA CENTRAL DE LOGIN

### ========================================

frame_login = ctk.CTkFrame(
app,
width=645,
height=420,
fg_color="white",
corner_radius=12,
border_width=1,
border_color="#E0E0E0")
frame_login.place(x=430, y=160)

### Títulos Internos

label_titulo_login = ctk.CTkLabel(
frame_login,
text="LOGIN",
text_color="black",
font=ctk.CTkFont(size=22, weight="bold"))
label_titulo_login.place(x=45, y=30)

label_entrar_sub = ctk.CTkLabel(
frame_login,
text="ENTRAR",
text_color=COR_TEXTO_SECUNDARIO,
font=ctk.CTkFont(size=14, weight="bold"))
label_entrar_sub.place(x=45, y=65)

### Linha divisória (Definida diretamente com width e height no construtor)

linha_divisoria = ctk.CTkFrame(
frame_login,
width=555,
height=2,
fg_color="#E0E0E0")
linha_divisoria.place(x=45, y=95)

### Campo: Usuário

label_usuario = ctk.CTkLabel(
frame_login,
text="🪛 Nome do Usuário",
text_color="black",
font=ctk.CTkFont(size=14, weight="bold"))
label_usuario.place(x=45, y=120)

entry_usuario = ctk.CTkEntry(
frame_login,
placeholder_text="Informe o nome do usuário",
border_width=1,
border_color="#CCCCCC",
fg_color="#FAFAFA",
text_color="black",
width=555,
height=40,
corner_radius=6)
entry_usuario.place(x=45, y=145)

### Campo: Senha

label_senha = ctk.CTkLabel(
frame_login,
text="🪛 Senha",
text_color="black",
font=ctk.CTkFont(size=14, weight="bold"))
label_senha.place(x=45, y=205)

entry_senha = ctk.CTkEntry(
frame_login,
placeholder_text="Informe a senha do usuário",
show="*",
border_width=1,
border_color="#CCCCCC",
fg_color="#FAFAFA",
text_color="black",
width=555,
height=40,
corner_radius=6)
entry_senha.place(x=45, y=230)

### Botão Entrar Principal

btn_entrar = ctk.CTkButton(
frame_login,
text="ENTRAR",
font=ctk.CTkFont(size=14, weight="bold"),
width=190,
height=42,
fg_color=COR_PRIMARIA,
hover_color=COR_HOVER,
text_color="white",
corner_radius=6)
btn_entrar.place(x=45, y=300)

app.mainloop()