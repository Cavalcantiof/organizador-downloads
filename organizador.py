import shutil
from pathlib import Path

# Pasta que será organizada
PASTA_ALVO = Path.home() / "Downloads"

CATEGORIAS = {
    "Imagens":     [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp"],
    "Documentos":  [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    "Videos":      [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Musicas":     [".mp3", ".wav", ".flac", ".ogg", ".m4a"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programas":   [".exe", ".msi", ".jar"],
    "Codigos":     [".py", ".js", ".html", ".css", ".json", ".sql"],
}

# Arquivos que o script NUNCA deve mexer
EXTENSOES_IGNORADAS = [".crdownload", ".part", ".tmp"]
NOMES_IGNORADOS = ["desktop.ini"]


def descobrir_categoria(arquivo):
    """Recebe um arquivo e devolve o nome da pasta onde ele deve ficar."""
    extensao = arquivo.suffix.lower()
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria
    return "Outros"


def caminho_livre(destino):
    """Se já existir um arquivo com esse nome, gera 'nome (1).ext', 'nome (2).ext'..."""
    if not destino.exists():
        return destino

    contador = 1
    while True:
        novo = destino.with_name(f"{destino.stem} ({contador}){destino.suffix}")
        if not novo.exists():
            return novo
        contador += 1


def deve_ignorar(arquivo):
    return (arquivo.suffix.lower() in EXTENSOES_IGNORADAS
            or arquivo.name.lower() in NOMES_IGNORADOS)


def main():
    if not PASTA_ALVO.exists():
        print(f"Erro: a pasta '{PASTA_ALVO}' não foi encontrada.")
        return

    # list() tira uma "foto" da pasta ANTES de começar a mexer nela
    itens = list(PASTA_ALVO.iterdir())
    movidos = 0

    for item in itens:
        if not item.is_file() or deve_ignorar(item):
            continue

        categoria = descobrir_categoria(item)
        pasta_categoria = PASTA_ALVO / categoria
        pasta_categoria.mkdir(exist_ok=True)

        destino = caminho_livre(pasta_categoria / item.name)
        shutil.move(item, destino)

        print(f"{item.name}  ->  {categoria}/{destino.name}")
        movidos += 1

    print("-" * 40)
    print(f"Pronto! {movidos} arquivo(s) organizado(s).")


if __name__ == "__main__":
    main()