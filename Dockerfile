# Base oficial do Jenkins LTS
FROM jenkins/jenkins:lts

# Mudar para root para poder instalar pacotes
USER root

# Atualizar e instalar dependências
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Voltar para usuário jenkins (boa prática)
USER jenkins

