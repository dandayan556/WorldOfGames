pipeline {
    agent any
    stages {
        stage('Checkout') { 
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'WorldOfGames_credentials', url: 'https://github.com/dandayan556/WorldOfGames.git']]])
            }
        }
        stage('Build') { 
            steps {
                bat 'docker build -t jenkinsdocker:latest .'
            }
        }
        stage('Run') { 
            steps {
                bat 'docker compose up -d'
            }
        }
        stage('Test') { 
            steps {
                git branch: 'main', credentialsId: 'WorldOfGames_credentials', url: 'https://github.com/dandayan556/WorldOfGames.git'
                bat 'python e2e.py'
            }
        }
        stage('Finalize') { 
            steps {
                bat 'docker compose stop'
                bat 'docker tag jenkinsdocker dandayan556/jenkinsdocker:latest'
                bat 'docker push dandayan556/jenkinsdocker:latest'
            }
        }
    }
        post {
            always {
                bat 'docker logout'
            }
        }
}
