pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkinspipeline-app"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                echo "📥 Obtendo código do repositório..."
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/querinoz/jenkinspipeline.git',
                        credentialsId: 'github-credential'
                    ]]
                ])
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Construindo imagem Docker com Python e dependências..."
                sh """
                    docker build -t $IMAGE_NAME . 
                """
            }
        }

        stage('Run WebsiteCheck') {
            steps {
                echo "🧪 Executando websitecheck.py dentro do container..."
                sh """
                    docker run --rm $IMAGE_NAME python3 websitecheck.py
                """
            }
        }
    }

    post {
        always {
            echo "🧹 Limpando containers antigos..."
            sh 'docker container prune -f'
        }
        success {
            echo "✅ Pipeline finalizada com sucesso!"
        }
        failure {
            echo "❌ Pipeline falhou!"
        }
    }
}
