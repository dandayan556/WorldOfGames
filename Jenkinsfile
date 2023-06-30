pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
             
               git 'https://github.com/dandayan556/WorldOfGames'
            }
        }

        stage('Build') {
            steps {
               
                sh 'docker build -t myflaskapp' .
            }
        }

        stage('Run') {
            steps {
                
                sh 'docker run -d -p 8777:8777 -v 'C:\Users\mgidy\PycharmProjects\pythonProject\DevOps2702\Scores.txt' myflaskapp'
            }
        }

        stage('Test') {
            steps {
               
                sh 'python e2e.py'
            }
        }

        stage('Finalize') {
            steps {
                
                sh 'docker stop $(docker ps -q --filter ancestor=myflaskapp)'
                
                sh 'docker push myflaskapp'
            }
        }
    }

    post {
        always {
            
            sh 'docker rm $(docker ps -a -q)'
            sh 'docker rmi myflaskapp'
        }
    }
}