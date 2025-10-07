// Define a imagem base do Docker para o Jenkins Agent, se necessário.
// Usamos 'agent any' pois a execução do Docker será feita no host.
pipeline {
    agent any 

    // Configuração do agendamento (Trigger) usando CRON.
    // O Jenkins CRON só suporta minutos, horas, dias, etc. Ele não suporta segundos.
    // Para simular a execução "a cada 20 segundos", a melhor prática é usar o agendamento
    // padrão para rodar a cada minuto, o que é o intervalo mínimo recomendado para pipelines.
    //
    // H/5 * * * * = Executa a cada 5 minutos (evita sobrecarga no Jenkins)
    // Se você realmente quer a cada minuto, use H * * * *
    triggers {
        // CRON para executar a cada minuto (o mínimo suportado)
        // Se você não definir a zona de tempo, ele usará a do servidor Jenkins.
        cron 'H * * * *'
    }

    environment {
        // Variáveis de ambiente para o Docker
        REPO_NAME = 'querinoz/website-check'
        IMAGE_NAME = "website-check-pipeline-app"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                echo "📥 Obtendo código do repositório..."
                // O Jenkins faz o checkout automaticamente, mas é bom ter o passo explícito.
                checkout scm 
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Construindo imagem Docker com Python e dependências..."
                // O websitecheck.py precisa de um ambiente Python. Construímos a imagem.
                // O Dockerfile deve estar na raiz do projeto.
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run WebsiteCheck') {
            steps {
                echo "▶️ Executando checagem do site no container..."
                // Executa o script Python dentro do container recém-construído.
                // O script websitecheck.py deve ser o ponto de entrada.
                sh "docker run --rm ${IMAGE_NAME}"
            }
        }
    }

    post {
        always {
            // Garante que containers antigos sejam limpos após a execução.
            echo "🧹 Limpando containers e imagens não utilizados..."
            sh 'docker container prune -f || true'
            // O '|| true' garante que a pipeline não falhe caso o comando prune falhe.
        }
        success {
            echo '✅ Pipeline concluída com sucesso. Site checado.'
        }
        failure {
            echo '❌ Pipeline falhou! Verifique os logs do Docker ou do script Python.'
        }
    }
}
