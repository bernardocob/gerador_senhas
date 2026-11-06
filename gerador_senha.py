import secrets
import string

import customtkinter as ctk


def gerar_senha(quantidade_letras: int, quantidade_numeros: int, quantidade_especiais: int) -> str:
    letras = [secrets.choice(string.ascii_letters) for _ in range(quantidade_letras)]
    numeros = [secrets.choice(string.digits) for _ in range(quantidade_numeros)]
    especiais = [secrets.choice(string.punctuation) for _ in range(quantidade_especiais)]
    senha = letras + numeros + especiais
    secrets.SystemRandom().shuffle(senha)
    return "".join(senha)


def gerar_senhas() -> None:
    try:
        quantidade_letras = int(campo_letras.get())
        quantidade_numeros = int(campo_numeros.get())
        quantidade_especiais = int(campo_especiais.get())
    except ValueError:
        resultado.configure(text="Informe uma quantidade inteira em cada campo.")
        return

    if min(quantidade_letras, quantidade_numeros, quantidade_especiais) < 0:
        resultado.configure(text="As quantidades não podem ser negativas.")
        return

    if quantidade_letras + quantidade_numeros + quantidade_especiais != 8:
        resultado.configure(text="A soma das quantidades deve ser exatamente 8.")
        return

    senhas = [
        gerar_senha(quantidade_letras, quantidade_numeros, quantidade_especiais)
        for _ in range(5)
    ]
    resultado.configure(text="\n".join(senhas))


if __name__ == "__main__":
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")

    janela = ctk.CTk()
    janela.title("Gerador de senhas")
    janela.geometry("420x430")
    janela.resizable(False, False)

    titulo = ctk.CTkLabel(
        janela,
        text="Gerador de senhas",
        font=ctk.CTkFont(size=22, weight="bold"),
    )
    titulo.pack(pady=(24, 16))

    campo_letras = ctk.CTkEntry(janela, placeholder_text="Quantidade de letras")
    campo_letras.pack(padx=30, pady=6, fill="x")

    campo_numeros = ctk.CTkEntry(janela, placeholder_text="Quantidade de números")
    campo_numeros.pack(padx=30, pady=6, fill="x")

    campo_especiais = ctk.CTkEntry(
        janela,
        placeholder_text="Quantidade de caracteres especiais",
    )
    campo_especiais.pack(padx=30, pady=6, fill="x")

    botao_gerar = ctk.CTkButton(janela, text="Gerar 5 senhas", command=gerar_senhas)
    botao_gerar.pack(padx=30, pady=16, fill="x")

    resultado = ctk.CTkLabel(janela, text="", justify="left", font=ctk.CTkFont(size=14))
    resultado.pack(padx=30, pady=8)

    janela.mainloop()
