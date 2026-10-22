# Organizador de Downloads

Script em Python que organiza automaticamente a pasta Downloads,
movendo cada arquivo para uma subpasta de acordo com o tipo
(Imagens, Documentos, Vídeos, Músicas, etc.).

## Funcionalidades

- Classifica arquivos pela extensão (sem diferenciar maiúsculas de minúsculas)
- Nunca sobrescreve arquivos: nomes repetidos viram `arquivo (1).ext`
- Ignora downloads em andamento (`.crdownload`, `.part`) e arquivos de sistema
- Pode ser executado várias vezes sem bagunçar o que já foi organizado
- Usa apenas a biblioteca padrão do Python, sem dependências

## Como usar

Requisito: Python 3.9 ou superior.

    python organizador.py

No Windows, também é possível dar dois cliques no arquivo `organizador.bat`.

## Personalização

As categorias ficam no dicionário `CATEGORIAS`, no início do
`organizador.py`. Para adicionar uma extensão ou criar uma categoria
nova, basta editar esse dicionário.

## Tecnologias

- Python (`pathlib`, `shutil`)