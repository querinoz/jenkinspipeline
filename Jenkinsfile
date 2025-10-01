pipeline {
    agent any

    stages {
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
            }
        }
        stage('Run Application') {
            steps {
                echo '🚀 Subindo aplicação...'
            }
        }
    }

    post {
        failure {
            echo "❌ Pipeline falhou!"
        }
        success {
            echo "✅ Pipeline finalizado com sucesso!"
        }
    }
}
