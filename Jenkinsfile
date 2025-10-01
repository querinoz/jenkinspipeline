pipeline {
    agent any

    stages {
<<<<<<< HEAD
        stage('Setup') {
            steps {
                echo '🔧 Configurando ambiente...'
            }
        }
        stage('Lint') {
            steps {
                echo '🔍 Rodando lint...'
            }
        }
        stage('Test') {
            steps {
                echo '🧪 Executando testes...'
=======
        stage('Checkout') {
            steps {
                echo '📥 Obtendo código do repositório...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Construindo imagem Docker...'
                sh 'docker build -t jenkinspipeline-app .'
            }
        }

        stage('Run Lint') {
            steps {
                echo '🔍 Rodando lint no container...'
                sh 'docker run --rm jenkinspipeline-app echo "Executando lint (ex: flake8, eslint...)"'
                // Exemplo real (se tiver flake8 instalado no container):
                // sh 'docker run --rm jenkinspipeline-app flake8 .'
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Executando testes no container...'
                sh 'docker run --rm jenkinspipeline-app echo "Rodando testes (ex: pytest)"'
                // Exemplo real (se tiver pytest no container):
                // sh 'docker run --rm jenkinspipeline-app pytest -v'
>>>>>>> 1fca130 (fix: removido checkout para test-pipeline.git)
            }
        }
        stage('Run Application') {
            steps {
<<<<<<< HEAD
                echo '🚀 Subindo aplicação...'
=======
                echo '🚀 Subindo aplicação no container...'
                sh 'docker run -d --name app-container -p 5000:5000 jenkinspipeline-app'
>>>>>>> 1fca130 (fix: removido checkout para test-pipeline.git)
            }
        }
    }

    post {
<<<<<<< HEAD
=======
        always {
            echo "🧹 Limpando containers antigos..."
            sh 'docker rm -f app-container || true'
        }
>>>>>>> 1fca130 (fix: removido checkout para test-pipeline.git)
        failure {
            echo "❌ Pipeline falhou!"
        }
        success {
            echo "✅ Pipeline finalizado com sucesso!"
        }
    }
}
