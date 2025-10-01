pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkinspipeline-app"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Obtendo código do repositório...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Construindo imagem Docker com Python...'
                sh '''
                    docker build -t $IMAGE_NAME .
                '''
            }
        }

        stage('Run WebsiteCheck') {
            steps {
                echo '🧪 Executando websitecheck.py dentro do container...'
                sh '''
                    docker run --rm $IMAGE_NAME python3 websitecheck.py
                '''
            }
        }
    }

    post {
        always {
            echo '🧹 Limpando containers antigos...'
            sh 'docker container prune -f || true'
        }
        failure {
            echo '❌ Pipeline falhou!'
        }
        success {
            echo '✅ Pipeline finalizado com sucesso!'
        }
    }
}
