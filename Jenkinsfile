pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/querinoz/test-pipeline.git'
            }
        }

        stage('Setup') {
            steps {
                sh '''
                    echo "==> Criando ambiente virtual..."
                    python3 -m venv venv

                    echo "==> Ativando ambiente virtual..."
                    . venv/bin/activate

                    echo "==> Instalando dependências (se existir requirements.txt)..."
                    if [ -f requirements.txt ]; then
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    else
                        echo "Nenhum requirements.txt encontrado. Pulando instalação."
                    fi
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    echo "==> Rodando lint..."
                    . venv/bin/activate
                    pip install flake8
                    flake8 --ignore=E501 ContaBancaria-System.py || true
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    echo "==> Rodando testes (se existirem)..."
                    . venv/bin/activate
                    if ls test_*.py > /dev/null 2>&1; then
                        pytest -v
                    else
                        echo "Nenhum teste encontrado. Pulando etapa."
                    fi
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh '''
                    echo "==> Executando aplicação..."
                    . venv/bin/activate
                    python ContaBancaria-System.py || echo "⚠️ Atenção: Aplicação terminou com erro."
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline concluído com sucesso!"
        }
        failure {
            echo "❌ Pipeline falhou!"
        }
    }
}

