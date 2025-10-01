# Usando Python 3.11 como base
FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copia o código do repositório para o container
COPY . /app

# Instala dependências, se houver requirements.txt
RUN pip install --upgrade pip
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Comando padrão (opcional)
CMD ["python3", "websitecheck.py"]
