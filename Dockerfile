# Usando imagem base Python 3.11 slim
FROM python:3.11-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando todos os arquivos do repositório para dentro do container
COPY . /app

# Atualizando pip e instalando dependências
RUN pip install --upgrade pip \
    && pip install --no-cache-dir requests

# Comando padrão (opcional)
CMD ["python3", "websitecheck.py"]
